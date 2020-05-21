#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import uuid
import datetime
from .WXBizDataCrypt import WXBizDataCrypt
import base64
from requests.exceptions import RequestException


class WXAppData:
    def __init__(self, appId, secret):
        self.appId = appId
        self.secret = secret
    # 用小程序的appid和app_secret获取小程序的openid和session_key

    def get_openid(self, code):
        url = 'https://api.q.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code'\
              % (self.appId, self.secret, code)
        try:
            response = requests.get(url)
            r = response.json()
            if r['openid'] and len(r['openid']) > 8:
                openid = r['openid']
                return {
                        'ok': 'success',
                        'openid': openid
                }
            elif r['errcode'] and r['errmsg']:
                return {
                    'ok': 'fail',
                    'msg': r['errmsg']
                }
            else:
                return {
                    'ok': 'fail',
                    'msg': '微信返回值错误'
                }
        except RequestException:
            return {
                'ok': 'fail',
                'msg': '网络错误'
            }

    def get_session(self, code, encrypt_data='', iv=''):
        url = 'https://api.q.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code'\
              % (self.appId, self.secret, code)

        try:
            response = requests.get(url)
            r = response.json()
            print("从接口获得的信息是")
            print(r)
            if r['openid'] and len(r['openid']) > 8 and r['session_key'] and len(r['session_key']) > 2:
                # 创建时间
                create_time = datetime.datetime.now()
                # 最后登录的时间
                last_vist_time = datetime.datetime.now()
                openid = r['openid']
                session_key = r['session_key']
                print("原始获得的session_key是"+session_key)
                # 加密后的用户唯一标志
                u_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, openid)
                skey = uuid.uuid3(uuid.NAMESPACE_DNS, session_key)
                user_info = ''
                print("out decrypt----------------------->")
                if encrypt_data and iv and len(encrypt_data) > 50 and len(iv) > 5:
                    print("in decrypt----------------------->")
                    pc = WXBizDataCrypt(self.appId, session_key)
                    print("开始获取用户信息")
                    user_info = pc.decrypt(encrypt_data, iv)
                return {
                    'ok': 'success',
                    'session': {
                        'uuid': u_uuid,
                        'skey': skey,
                        'create_time': create_time,
                        'last_vist_time': last_vist_time,
                        'openid': openid,
                        'session_key': session_key,
                        'user_info': user_info
                    }
                }
            elif r['errcode'] and r['errmsg']:
                return {
                    'ok': 'fail',
                    'msg': r['errmsg']
                }

            else:
                return {
                    'ok': 'fail',
                    'msg': '微信返回值错误'
                }
        except RequestException:
            return {
                'ok': 'fail',
                'msg': '网络错误'
            }



