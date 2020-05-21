#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AppInfo, SessionInfo, UserInfo
from aiguess.models import ImageInfo
from .WXAppData import WXAppData
import logging
import json


from datetime import datetime, timezone
logger = logging.getLogger(__name__)


# utils
def check_session_for_login(params):
    ss = SessionInfo.objects.filter(open_id=params['openid'])
    if ss.exists():
        s = ss.first()
        if s and s.create_time:
            return True
        else:
            return False
    else:
        s = SessionInfo(uuid=params['uuid'], skey=params['skey'],
                        create_time=params['create_time'],
                        last_vist_time=params['last_vist_time'],
                        open_id=params['openid'],
                        session_key=params['session_key'],
                        user_info=params['user_info'])
        s.save()
        return True


def check_session_for_auth(params):
    ss = SessionInfo.objects.filter(uuid=params['uuid'], skey=params['skey'])
    print('check_session_for_auth')
    if ss.exists():
        s = ss.first()
        now_time = datetime.now(timezone.utc)
        create_time = s.create_time
        last_vist_time = s.last_vist_time
        if int((now_time - create_time).days) > params['login_duration']:
            print('login_duration-------')
            return False
        elif int((now_time - last_vist_time).total_seconds()) > params['session_duration']:
            print('session_duration-------')
            return False
        else:
            s.last_vist_time = now_time
            s.save()
            return s.user_info
    else:
        return False


def change_session(params):
    # if check_session_for_login(params):
    ss = SessionInfo.objects.filter(open_id=params['openid'])
    print(ss)
    if ss.exists():
        print(ss.exists())
        s = ss.first()
        if not s.uuid:
            s.uuid = params['uuid']
            s.session_key = params['session_key']
            s.create_time = params['create_time']
            s.last_vist_time = params['last_vist_time']
            s.skey = params['skey']
            s.user_info = params['user_info']
            s.save()
            return s.uuid
        else:
            s.session_key = params['session_key']
            s.create_time = params['create_time']
            s.last_vist_time = params['last_vist_time']
            s.skey = params['skey']
            s.user_info = params['user_info']
            s.save()
            return s.uuid
    else:
        s = SessionInfo(uuid=params['uuid'], skey=params['skey'],
                        create_time=params['create_time'],
                        last_vist_time=params['last_vist_time'],
                        open_id=params['openid'],
                        session_key=params['session_key'],
                        user_info=params['user_info'])
        s.save()
        new_s = SessionInfo.objects.get(uuid=params['uuid'])
        UserInfo.objects.create(session=new_s)
        return True
    # else:
    #     return False


# Create your views here.
def index(request):
    return JsonResponse({'msg': 'welcome'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        print(request.body)
        print(type(request.body))
        mydata = (str(request.body,encoding="utf-8"))
        #print(request.POST.get("code"))
        data = json.loads(mydata)
        print(type(data))
        app_id = 1
        encrypt_data = data.get('encrypt_data', '').strip()
        code = data.get('code', '').strip()
        iv = data.get('iv', '').strip()
        if app_id and app_id > 0 and code and len(code) > 6:
            apps = AppInfo.objects.filter(pk=app_id)
            if apps.exists():
                app_info = apps.first()
                wxapp_data = WXAppData(appId=app_info.appid, secret=app_info.secret)
                result = wxapp_data.get_session(code=code, encrypt_data=encrypt_data, iv=iv)
                ss = SessionInfo.objects.filter(open_id=result['session']['openid'])
                print("out------->change_session")
                print(ss.exists())
                if result['ok'] == 'fail':
                    return JsonResponse(result)
                else:
                    s = result['session']
                    result_s = change_session(params=s)
                    if result_s is False:
                        return JsonResponse({'ok': 'fail', 'msg': '更新session出错'})
                    elif result_s is True:
                        return JsonResponse({'ok': 'success', 'msg': '新增session成功',
                                             'data': {
                                                 'uuid': s['uuid'],
                                                 'skey': s['skey'],
                                                 'user_info': s['user_info']
                                             }})
                    else:
                        return JsonResponse({'ok': 'success', 'msg': '更新session成功',
                                             'data': {
                                                 'uuid': result_s,
                                                 'skey': s['skey'],
                                                 'user_info': s['user_info']
                                             }})
            else:
                return JsonResponse({'ok': 'fail', 'msg': '获取app相关参数出错'})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})
    else:
        return JsonResponse({'ok': 'fail', 'msg': 'not post method'})

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        mydata = str(request.body,encoding='utf-8')
        data = json.loads(mydata)
        app_id = 1
        code = data.get('code', '').strip()
        if app_id and app_id > 0 and code and len(code) > 6:
            apps = AppInfo.objects.filter(pk=app_id)
            if apps.exists():
                # 1 means default '你画我猜'
                app_info = apps.first()
                wxapp_data = WXAppData(appId=app_info.appid, secret=app_info.secret)
                result = wxapp_data.get_openid(code=code)
                if result['ok'] == 'fail':
                    return JsonResponse({'ok': 'fail', 'msg': '请注册'})
                else:
                    print(result['openid'])
                    user = SessionInfo.objects.get(open_id=result['openid'])
                    return JsonResponse({'ok': 'success', 'msg': '验证成功',
                                         'data': {
                                             'uuid': user.uuid,
                                             'skey': user.skey,
                                             'user_info': user.user_info
                                         }})
            else:
                return JsonResponse({'ok': 'fail', 'msg': '获取app相关参数出错'})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '请求参数错误'})
    else:
        return JsonResponse({'ok': 'fail', 'msg': 'not post method'})


@csrf_exempt
def leader_board(request):
    # 需要增加缓存，一天查询数据库一次，当天内直接返回首次查询的结果。
    if request.method == 'POST':
        leaders = UserInfo.objects.order_by("-success_count")
        data = []
        re_dict = {}
        if leaders:
            if len(leaders) >= 10:
                for leader in leaders[:10]:
                    my_info = eval(leader.session.user_info)
                    re_dict['avatarUrl'] = my_info['avatarUrl']
                    re_dict['success_count'] = leader.success_count
                    re_dict['nickName'] = my_info['nickName']
                    data.append(re_dict)
                    re_dict = {}
            else:
                for leader in leaders:
                    my_info = eval(leader.session.user_info)
                    re_dict['avatarUrl'] = my_info['avatarUrl']
                    re_dict['success_count'] = leader.success_count
                    re_dict['nickName'] = my_info['nickName']
                    data.append(re_dict)
                    re_dict = {}
            return JsonResponse({'ok': 'success', 'msg': '成功', 'data': data})
        else:
            return JsonResponse({'ok': 'success', 'msg': '还未有人完成画作', 'data': []})
    else:
        return JsonResponse({'ok': 'fail', 'msg': 'not post method'})


@csrf_exempt
def my_creation(request):
    if request.method == 'POST':
        mydata = str(request.body,encoding="utf-8")
        data = json.loads(mydata)
        uuid = data.get('uuid', '').strip()
        if uuid:
            my_info = UserInfo.objects.filter(session__uuid=uuid)
            print(my_info)
            my_images = ImageInfo.objects.filter(uuid=uuid)
            print(my_images)
            if my_info:
                grade_data = {}
                grade_data['grade'] = my_info[0].grade
                grade_data['success_count'] = my_info[0].success_count
                grade_data['remainder'] = my_info[0].remainder
                grade_data['avatarUrl'] = eval(my_info[0].session.user_info)['avatarUrl']
                back = []
                dict_info = {}
                if my_images:
                    for image in my_images:
                        # 拼接图片路径
                        src = "https://qien.xyz/static/guessimage/{}".format(image.image_path)
                        dict_info['src'] = src
                        dict_info['image_name'] = image.imageKey.image_name
                        dict_info['image_id'] = image.imageKey.image_id
                        back.append(dict_info)
                        dict_info = {}
                    # 后期考虑做成缓存，每当用户图片存储的时候push到缓存中
                    return JsonResponse({'ok': 'success', 'msg': 'success', 'image_data': back, 'grade_data': grade_data})
                else:
                    return JsonResponse({'ok': 'success', 'msg': 'success', 'image_data': back, 'grade_data': grade_data})
            else:
                return JsonResponse({'ok': 'fail', 'msg': 'no this person data'})
        else:
            return JsonResponse({'ok': 'fail', 'msg': 'uuid or skey error'})
    else:
        return JsonResponse({'ok': 'fail', 'msg': 'not post method'})
