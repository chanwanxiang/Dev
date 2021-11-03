# -*- coding: utf-8 -*-

import base64
from gmssl import sm2

pubKey = "+0463f587e346663a7bafd85a41e8ade713bd3c3a2168b4891671fcd3b2ea3686f5fb0847a113b1931a630157d5ba335eb173b805f378655ca1c440138390972786"
priKey = "5fd0febfd7ce7546bc23bce5fe0e6b25df1490d9fe7bd84f479a182272906495"
sm2Crypt = sm2.CryptSM2(priKey, pubKey)

class Sm2():
    def encryptinfo(self, info):
        """
        将utf-8编码的info信息编码为unicode -> sm2加密 -> 加密密文解码
        """
        sm2info = sm2Crypt.encrypt(info.encode('utf-8'))
        b64info = base64.b64encode(sm2info).decode()
        return b64info

    def decryptinfo(self, info):
        b64info = base64.b64decode(info.encode())
        sm2info = sm2Crypt.decrypt(b64info).decode(encoding="utf-8")
        return sm2info

sm2Obj = Sm2()
info = '123456'
print(sm2Obj.encryptinfo(info))
print(sm2Obj.decryptinfo(sm2Obj.encryptinfo(info)))
