import sys
import jpype


class RsaSign():
    def encrypted(cls, body):
        """
        获取jvm路径 -> 启动jvm以及jar包 -> 指定mainclass -> 创建实例对象 -> 引用jar包类中的方法 -> 关闭jvm

        """
        jvmpath = jpype.getDefaultJVMPath()
        jarpath = r"D:\Dev\apiTest\util\restaurant.jar"
        try:
            jpype.startJVM(jvmpath, "-ea", f"-Djava.class.path={jarpath}", convertStrings=False)
        except:
            pass
        """
        验证环境
        jpype.java.lang.System.out.println("hello world")

        """
        jarrskcls = jpype.JClass("org.example.utils.RsaUtil")
        jarrskobj = jarrskcls()
        pubkey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzUFYcmTavISBR5anAk/1j0qjqE/ft/ASzVuNcmZeBxrarAn48qVq/S/1Qc0OTNtbcTgLGwwKCHVe5nIhsvoVRA2aLU0Bi6G8IFQiBRhFjomf/VfRS3bcLYYAZMUtggNqDygsITtXo+qgWeHA+QTA6cUq4NrbyCAcAynAG6ODItkRJf44v0b3ujiHkhzRW2nyo9aC6ncbIUcJvZiOJ/8akcA3HbkFDGyb/KMfFITC5lI/XGPmz65bANYzI7rsjUd8N1pWlGPJEEWa6omXooQPp0yVYDHdX2cGqBn0qlGNXlUafH99nxl6Y5qoWXCFlgDoQVfuTTGCrBsYQZ/S6UFtUwIDAQAB"
        cryptedobj = str(jarrskobj.encryptContentByPublickey(body, pubkey))

        return cryptedobj


    def decrypted(self, response):
        jvmpath = jpype.getDefaultJVMPath()
        jarpath = r"D:\Dev\apiTest\util\restaurant.jar"
        try:
            jpype.startJVM(jvmpath, "-ea", f"-Djava.class.path={jarpath}", convertStrings=False)
        except:
            pass
        jarrskcls = jpype.JClass("org.example.utils.RsaUtil")
        jarrskobj = jarrskcls()
        pubkey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzUFYcmTavISBR5anAk/1j0qjqE/ft/ASzVuNcmZeBxrarAn48qVq/S/1Qc0OTNtbcTgLGwwKCHVe5nIhsvoVRA2aLU0Bi6G8IFQiBRhFjomf/VfRS3bcLYYAZMUtggNqDygsITtXo+qgWeHA+QTA6cUq4NrbyCAcAynAG6ODItkRJf44v0b3ujiHkhzRW2nyo9aC6ncbIUcJvZiOJ/8akcA3HbkFDGyb/KMfFITC5lI/XGPmz65bANYzI7rsjUd8N1pWlGPJEEWa6omXooQPp0yVYDHdX2cGqBn0qlGNXlUafH99nxl6Y5qoWXCFlgDoQVfuTTGCrBsYQZ/S6UFtUwIDAQAB"
        decryptedobj = str(jarrskobj.decryptContentByPublickey(response, pubkey))
        """
        jpype.shutdownJVM()

        """

        return decryptedobj


if __name__ == "__main__":
    rs = RsaSign()
    body = '{"machineNum":"2161AF600051","bizContent":{"account":"emp2","password":"123456"}}'
    response = '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'
    print(rs.encrypted(body))
    print("-"*10)
    print(rs.decrypted(response))
