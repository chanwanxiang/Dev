from base64 import b64encode, b64decode
import json, requests
from gmssl import sm2

resp = json.loads(requests.get("https://gzdev.yuuwei.com/user/getSm2").text)
pubKey = resp['data']

priKey = "311861d5046d647c698930992b7d2614956d267f46419223714913cf5e0a7150"
sm2Crypt = sm2.CryptSM2(public_key=pubKey, private_key=priKey)

class Sm2():
    def encryptinfo(self, info):
        # 将utf-8编码的info信息编码为unicode -> sm2加密 -> 加密密文解码
        sm2info = sm2Crypt.encrypt(info.encode(encoding="utf-8"))
        b64info = b64encode(sm2info).decode()
        return b64info

    def decryptinfo(self, info):
        b64info = b64decode(info.encode())
        deinfo = sm2Crypt.decrypt(b64info).decode("utf8", "ignore")
        return deinfo

sm2Obj = Sm2()
pswd = 'Ab@123456'
enpswd = sm2Obj.encryptinfo(pswd)
print(enpswd, len(enpswd))
depswd = sm2Obj.decryptinfo(enpswd)
print(depswd)
