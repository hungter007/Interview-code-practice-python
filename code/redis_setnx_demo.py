#连接redis
import time
import uuid
from threading import Thread

import redis

redis_client = redis.Redis(host="localhost",
                           port=6379,
                           # password=123,
                           db=10)

#获取一个锁
# lock_name：锁定名称
# acquire_time: 客户端等待获取锁的时间
# time_out: 锁的超时时间
def acquire_lock(lock_name, acquire_time=10, time_out=10):
    """获取一个分布式锁"""
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    while time.time() < end:
        # 方式一，分步执行设置锁和超时时间
        # if redis_client.setnx(lock, identifier):
        #     # 给锁设置超时时间, 防止进程崩溃导致其他进程无法获取锁
        #     redis_client.expire(lock, time_out)
        #     return identifier
        # 优化方式一步执行，原子操作
        if redis_client.set(lock, identifier, ex=time_out, nx=True):
            return identifier
        elif not redis_client.ttl(lock):
            # 延长锁的时间
            redis_client.expire(lock, time_out)
        time.sleep(0.001)
    return False

#释放一个锁
def release_lock(lock_name, identifier):
    """通用的锁释放函数"""
    lock = "string:lock:" + lock_name
    pip = redis_client.pipeline(True)
    # redis 事务
    while True:
        try:
            pip.watch(lock)
            lock_value = redis_client.get(lock)
            if not lock_value:
                return True

            if lock_value.decode() == identifier:
                pip.multi()
                pip.delete(lock)
                pip.execute()
                return True
            pip.unwatch()
            break
        except redis.excetions.WacthcError:
            pass
    return False


count = 10

def seckill(i):
    identifier = acquire_lock('resource')
    if not identifier:
        print("线程:{}--超时，没有获取到资源".format(i))
        return
    print("线程:{}--获得了锁".format(i))
    time.sleep(3)
    global count
    if count < 1:
        print("线程:{}--没抢到，票抢完了".format(i))
        return
    count -= 1
    print("线程:{}--抢到一张票，还剩{}张票".format(i,count))
    release_lock('resource', identifier)


for i in range(5):
    t = Thread(target=seckill,args=(i,))
    t.start()
