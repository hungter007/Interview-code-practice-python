# chat/views.py
from django.shortcuts import render
from django.views.generic.base import View
from django.utils.safestring import mark_safe
from django.http import JsonResponse, HttpResponse
import json
import logging
import functools
import redis
import random
import string

r.setex
def catch_exception(func, code=500, *args, **kwargs):
    '''
    :param func:
    :return:
    '''

    @functools.wraps(func, *args, **kwargs)
    def nefen(request, *args, **kwargs):
        try:
            back = func(request, *args, **kwargs)
            return back
        except Exception as e:
            # string = "捕获到异常"
            # x = type(e)
            #
            # if x == ValueError:
            #     string = "数值转换异常:" + str(e)
            log2 = logging.getLogger("print2")
            log2.error(e)
            # return JsonResponse(error_string=str(e), code=code)
            return JsonResponse({'fault': 'xxx'})
    return nefen


class Index(View):
    #@catch_exception
    def get(self, request):
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)

        if r.exists("key"):
            # 已经存在房间且房间未过期
            # print("have exists hash1")
            if r.hexists("hash1", "count"):
                r.hincrby("hash1", "count", amount=-1)
                # print(r.hget("hash1", "count"))
                # print(type(r.hget("hash1", "count")))
                if int(r.hget("hash1", "count")) == 0:
                    room_name = r.hget("hash1", "room_name")
                    count = r.hget("hash1", "count")
                    # 做一个room_name 随机数
                    # salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                    # print(salt)
                    # r.hset("hash1", "room_name", salt)
                    # r.hset("hash1", "count", 7)
                    r.delete("key")
                else:
                    room_name = r.hget("hash1", "room_name")
                    count = r.hget("hash1", "count")
                # with open("test.txt", "a") as f:
                #     f.write(room_name + '\n')
                return JsonResponse({"data": room_name})
            else:
                salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                print(salt)
                r.hset("hash1", "room_name", salt)
                r.hset("hash1", "count", 7)
                r.setex("key", 20, salt)
                room_name = r.hget("hash1", "room_name")
                # with open("test.txt", "a") as f:
                #     f.write(room_name + '\n')
                return JsonResponse({"data": room_name})
        else:
            # 房间已过期
            # 做一个room_name 随机数
            #print("not exists hash1")
            salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            #print(salt)
            r.hset("hash1", "room_name", salt)
            r.hset("hash1", "count", 7)
            r.setex("key", 20, salt)
            room_name = r.hget("hash1", "room_name")
            # with open("test.txt", "a") as f:
            #     f.write(room_name + '\n')
            return JsonResponse({"data": room_name})

        # return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
