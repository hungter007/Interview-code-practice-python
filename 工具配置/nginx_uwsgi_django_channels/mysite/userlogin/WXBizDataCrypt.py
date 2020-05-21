import base64
import json
import ast

import chardet
from Cryptodome.Cipher import AES


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        print("原来的session_key"+self.sessionKey)
        print("原来的敏感信息"+encryptedData)
        print("原来的iv信息" + iv)
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        print(99999999999999999)
        print("base64加密后的敏感字段"+str(encryptedData))
        print("base64加密后session_key"+str(sessionKey))

        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        print(8888888888888888888888888888)
        decrypted = cipher.decrypt(encryptedData)
        print(decrypted)
        split_list = str(decrypted, encoding="utf-8").split("}}")
        split_list[-1] = ''
        mydata = "}}".join(split_list)
        # mydata = str(decrypted,encoding="utf-8").strip()
        # thedata = mydata.encode("utf-8").decode("utf-8")
        print("解密后的用户敏感信息"+mydata)
        # print(type(mydata))
        # print("编码解码后的用户敏感信息" + thedata)
        # print("解密出来的用户信息"+str(self._unpad(cipher.decrypt(encryptedData))))
        decrypted = json.loads(mydata)
        print(222222222222)
        #decrypted = eval(mydata)
        # decrypted = json.loads(decrypted)
        # decrypted = json.loads(self._unpad(decrypted))
        print(11111111111111111)
        print(decrypted)
        print(type(decrypted))
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')

        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
