class Test:
    def test(self):
        return {'1': 1, '2': 2}

a = Test()
print(dict(list(a.test().items())))

# def creat(dir, step, pox=[0, 0]):
#     new_x = pox[0] + dir[0] * step
#     new_y = pox[1] + dir[1] * step
#     pox[0] = new_x
#     pox[1] = new_y
#     return pox
#
#
# print(creat([1, 0], 10))
# print(creat([0, 1], 20, [10, 10]))
# print(creat([-1, 0], 10))

# def turn(matrix):
#     newmat = []
#     row = len(matrix)
#     col = len(matrix[0])
#     for i in range(col):
#         newmat1 = []
#         for j in range(row):
#             newmat1.append(matrix[j][i])
#         newmat.append(newmat1)
#     newmat.reverse()
#     return newmat
# print(turn(a))
# import random
#
#
# def send_money(total_yuan, num):
#     """
#     send_money
#     :param total: 元为单位，转成分
#     :param num: ⼈数
#     """
#     # 分为单位
#     total = total_yuan * 100
#     cur_total = 0
#     for i in range(num-1):
#         remain = total - cur_total
#         money = random.randint(1, int(remain/(num-i)*2))
#         cur_total += money
#         yield round(money/100.0, 2)
#     yield round((total - cur_total)/100.0, 2)
#
#
# def test():
#     t = 0
#     for i in send_money(100, 10):
#         t += i
#         print(i)
#     print('sum:', t)
#
#
# if __name__ == '__main__':
#     test()



#-*- coding:utf-8 -*-
# class A(object):
#     def f(self):
#         print("AAAA")
#
#
# class B(object):
#     def f(self):
#         print("BBBB")
#
#
# class C(B, A):
#     def f(self):
#         print "ccc"
#
#
# new = C()
# new.f()

# class A():
#     def foo1(self):
#         print "A"
# class B(A):
#     def foo2(self):
#         pass
# class C(A):
#     def foo1(self):
#         print "C"
# class D(B, C):
#     pass
#
# d = D()
# d.foo1()
# a = "asdfghjkl"
# b = a[::-1]
# print b
#
# def kmp(mom_string, son_string):
#     # 传入一个母串和一个子串
#     # 返回子串匹配上的第一个位置，若没有匹配上返回-1
#     test = ''
#     if type(mom_string) != type(test) or type(son_string) != type(test):
#         return -1
#     if len(son_string) == 0:
#         return 0
#     if len(mom_string) == 0:
#         return -1
#     # 求next数组
#     next = [-1] * len(son_string)
#     if len(son_string) > 1:# 这里加if是怕列表越界
#         next[1] = 0
#         i, j = 1, 0
#         while i < len(son_string) - 1:  # 这里一定要-1，不然会像例子中出现next[8]会越界的
#             if j == -1 or son_string[i] == son_string[j]:
#                 i += 1
#                 j += 1
#                 next[i] = j
#             else:
#                 j = next[j]
#
#     # kmp框架
#     m = s = 0  # 母指针和子指针初始化为0
#     while s < len(son_string) and m < len(mom_string):
#         # 匹配成功,或者遍历完母串匹配失败退出
#         if s == -1 or mom_string[m] == son_string[s]:
#             m += 1
#             s += 1
#         else:
#             s = next[s]
#
#     if s == len(son_string):  # 匹配成功
#         return m - s
#     # 匹配失败
#     return -1
#
#
# # 测试
# mom_string = 'ababababca'
# son_string = 'abababca'
# print(kmp(mom_string, son_string))
#
# a = "BBC ABCDAB ABCDABCDABDE"
# b = "ABCDABD"
# print(kmp(a, b))





# def quicksort(list):
#     if len(list) < 2:
#         return list
#     else:
#         tmp = list[0]
#         less = [i for i in list[1:] if i <= tmp]
#         bigger = [i for i in list[1:] if i > tmp]
#         end_list = quicksort(less) + [tmp] + quicksort(bigger)
#         return end_list
#
#
# a = [1, 2, 5, 10, 11, 3, 9, 4]
# print(quicksort(a))


# a = None
# b = []
# c = ""
# d = 0
# if a is None:
#     print("a is None")
# if not a:
#     print("not a")
# if b is None:
#     print("b is None")
# if not b:
#     print("not b")
# if c is None:
#     print("c is None")
# if not c:
#     print("not c")
# if d is None:
#     print("d is None")
# if not d:
#     print("not d")
#
# e = [1,2,3]
# f = [1,2,3]
# print(f. pop(-1))
# print(f)
# if e == f:
#     print("e == f")
# if e is f :
#     print("e is f")
# g = {"a" : 1, "b": 2, "c": 3}
# print(g.items())
# for k, v in g.items():
#     print(k, v)





# #_*_coding:utf-8_*_
# from wsgiref.simple_server import make_server
#
#
# def application(environ, start_response):
#     print(environ)
#     status = "200 OK"
#     headers = [("Conten-Type", "text/html; charset=utf8")]
#     start_response(status, headers)
#     return [b"<h1>Hello, world</h1>"]
#
#
# if __name__ == "__main__":
#     httpd = make_server("127.0.0.1", 8000, application)
#     httpd.serve_forever()



# from functools import wraps
#
# def cache(func):
#     store = {}
#
#     @wraps(func)
#     def _(n):
#         if n in store:
#             return store[n]
#         else:
#             res = func(n)
#             store[n] = res
#             return res
#     return _
#
# @cache
# def f(n):
#     if n <= 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
#
# for i in range(10):
#     print(f(i))


# # 发布订阅模式
# class Publisher:
#     def __init__(self):
#         self.observers = []
#
#     def add(self, observer):
#         if observer not in self.observers:
#             self.observers.append(observer)
#         else:
#             print("Faile to add : {}".format(observer))
#
#     def delete(self, observer):
#         if observer in self.observers:
#             self.observers.remove(observer)
#         else:
#             print("Faile to delete : {}".format(observer))
#
#     def notify(self):
#         [o.notify_by(self) for o in self.observers]
#
# class Formatter(Publisher):


# 适配器模式
# class Computer:
#     def __init__(self):
#         self.name = "computer"
#
#     def power65(self):
#         print("need 65V")
#
#
# class Phone:
#     def __init__(self):
#         self.name = "phone"
#
#     def power5(self):
#         print("need 5v")
#
#
# class Adapter:
#     def __init__(self, obj, **adapter_method):
#         self.obj = obj
#         self.__dict__.update(adapter_method)
#
#     def __getattr__(self, item):
#         return getattr(self.obj, item)
#
#
# object = []
# computer = Computer()
# object.append(Adapter(computer, getPower=computer.power65))
# phone = Phone()
# object.append(Adapter(phone, getPower=phone.power5))
# for obj in object:
#     print("from {} get method {}".format(obj.name, obj.getPower))


# from collections import deque
# from heapq import heapify, heappop
#
# class Queue(object):
#     def __init__(self):
#         self.queue = deque()
#
#     def push(self, value):
#         self.queue.append(value)
#
#     def pop(self):
#         res = self.queue.popleft()
#         return res
#
# myqueue = Queue()
# for i in range(5):
#     myqueue.push(i)
#
# print(myqueue.pop())












# import heapq
#
#
# class TopK:
#     def __init__(self, iterable, k):
#         self.minheap = []
#         self.capacity = k
#         self.iterable = iterable
#
#     def push(self, value):
#         if len(self.minheap) > self.capacity:
#             minValue = self.minheap[0]
#             if value < minValue:
#                 pass
#             else:
#                 heapq.heapreplace(self.minheap, value) # 删除minheap[0] 将新元素加入后重新排序，最小放置在[0]
#         else:
#             heapq.heappush(self.minheap, value)
#
#     def get_top_k(self):
#         for val in self.iterable:
#             self.push(val)
#         return self.minheap
#
#
# def test():
#     import random
#     i = list(range(1000)) # 可迭代元素，节省内存
#     random.shuffle(i)
#     _ = TopK(i, 10)
#     print(_.get_top_k())
#
# test()








# from collections import OrderedDict
#
#
# class LRUCache(object):
#     def __init__(self, capacity=128):
#         self.od = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key):
#         if key in self.od:
#             value = self.od[key]
#             self.od.move_to_end(key)
#             return value
#         else:
#             return -1
#
#     def put(self, key, value):
#         if key in self.od:
#             del self.od[key]
#             self.od[key] = value
#         else:
#             self.od[key] = value
#             if len(self.od) > self.capacity:
#                 self.od.popitem(last=False)
# od.move_to_end()
# od.popitem()


