import rsa
import base64

class RsaSign(object):
    def crypted(cls, body):
        """
        https://testerhome.com/topics/30849
        
        创建pubkey对象 -> 生成密文 -> 密文转为base64编码 -> 字节类型base64编码解码为字符串
        
        """
        publicKey = ("-----BEGIN PUBLIC KEY-----" + "\n" + "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzUFYcmTavISBR5anAk/1j0qjqE/ft/ASzVuNcmZeBxrarAn48qVq/S/1Qc0OTNtbcTgLGwwKCHVe5nIhsvoVRA2aLU0Bi6G8IFQiBRhFjomf/VfRS3bcLYYAZMUtggNqDygsITtXo+qgWeHA+QTA6cUq4NrbyCAcAynAG6ODItkRJf44v0b3ujiHkhzRW2nyo9aC6ncbIUcJvZiOJ/8akcA3HbkFDGyb/KMfFITC5lI/XGPmz65bANYzI7rsjUd8N1pWlGPJEEWa6omXooQPp0yVYDHdX2cGqBn0qlGNXlUafH99nxl6Y5qoWXCFlgDoQVfuTTGCrBsYQZ/S6UFtUwIDAQAB" + "\n" + "-----END PUBLIC KEY-----").encode('utf-8')
        pubKeyObj = rsa.PublicKey.load_pkcs1_openssl_pem(publicKey)
        cryptedObj = base64.b64encode(rsa.encrypt(body.encode('utf-8'), pubKeyObj))
 
        cryptedBody =  cryptedObj.decode('utf-8')

        return cryptedBody

    def decrypt(cls, response):
        """
        创建prikey对象 -> 字符串解码为base64编码 -> 解密密文 -> 字节类型base64编码解码为字符串

        """
        privateKey = ("-----BEGIN RSA PRIVATE KEY-----" + "\n" + "MIIEowIBAAKCAQEAzUFYcmTavISBR5anAk/1j0qjqE/ft/ASzVuNcmZeBxrarAn48qVq/S/1Qc0OTNtbcTgLGwwKCHVe5nIhsvoVRA2aLU0Bi6G8IFQiBRhFjomf/VfRS3bcLYYAZMUtggNqDygsITtXo+qgWeHA+QTA6cUq4NrbyCAcAynAG6ODItkRJf44v0b3ujiHkhzRW2nyo9aC6ncbIUcJvZiOJ/8akcA3HbkFDGyb/KMfFITC5lI/XGPmz65bANYzI7rsjUd8N1pWlGPJEEWa6omXooQPp0yVYDHdX2cGqBn0qlGNXlUafH99nxl6Y5qoWXCFlgDoQVfuTTGCrBsYQZ/S6UFtUwIDAQABAoIBACSQnowKcXkh9dHmAayEyA8V0d/bEtS2vPK+e41EtT14yDnbsPCxDUU7dOqa+BAzB7A8tqXD2Em3dweAj4ZNzNoJvkyRqlPQpS3xLvpPX5zL4aeFLHDQJNsrQwiwo7HEn/FBS9NDuhImaxh4AiOaeC9tA315H6wgJD1gA6wozeS4CwmeAvEW9CehaJlKNr+piNKJluKOyiJjIWweRHASiToWA1unvN8T96durMJQhkV2t+Rx7yu1DodM4mGst2ySt00swTYa4FO71ZYC2npsEHT7SL/H2Gd4q4tXNCZqoXoElNgRA8oQN+gzryUib4jtX4tkew4F3TTJAn4Y2iuFsxkCgYEA6VpmvllO5z5f9+G3QDb7rEYoNkm0HTVjCQhlpcrDPo+rN2pvk6qooLUu7xwlBVksw9EqiI8hqtv95eomMiRUqkoF7zOXi3DbXui2+WZWZTOpQxiBP0QLePFZXj+aFPU3kud+2mCQZm+NxD3GMv0fj4qvh3a0HboTsxyvwidntH0CgYEA4SzcE3hHzuidSXwawCKPjLqOMEt410KKhaWdjKKiS/Rqhu7AV6/whYV07cAUphyHUF2Y73Chg4OmKUCHnRClBmxUri8he/LHVIwKyOvY4EKSEhNnBqB520rEMd34h9rk8EUrLfnWXzhczt1V42V8JGZ9zy2m9pfyfg0eBN1OYg8CgYAR6Ar8TlQcsI+isOJj/hQf6x5I1C0LFL6twcQzDbUfxtyHmxZGyZC5DE42sP0yRN6HhDR0WC9oMgtwqiAWNu18R8Pe0CGv5JAg31CzIKQ+jdFOQcIhPbJ3rGWEMvM66npCPptgXIqYIbVKOsdLwFq8pBLGHVjC8zVxyCDAkE+H7QKBgF68lfcnEuctnQdOzJ5rrAOkdbBCAJxoZYlnLYr+3dOhCLSufIQoBMTYamKg/s8Ij7GzP2X1+C4x1FXkzWm6mAPEzjfeonLYqR6cMOlpuPxZZcVvHlh+aeZmZXcpkafu44VnRIx6YcP8Haf3HWynxPw3ltT0uxtiwGZiNHANgC3nAoGBAK/7++BMjL7JGuTE+c5AMWHjedl3OBSyhRmz1k2UZxxc0/ZrlbYgAxBi3U1VRG42xxpeDo0kg03k2iHMvy/UnS306bh6t0XtMTrkY5Q9zn98Ju2j6LaEmXSpSOU20JnEiPoN/V9/SQNkylAJ8D7nUB3yzBNAXKO2T7j5oFiYGiFZ" + "\n" + "-----END RSA PRIVATE KEY-----").encode('utf-8')
        prikeyobj = rsa.PrivateKey.load_pkcs1(privateKey)
        decryptRes = rsa.decrypt(base64.b64decode(response), prikeyobj)

        return decryptRes.decode('utf-8')

if __name__ == "__main__":
    rs = RsaSign()
    print(rs.crypted('{"machineNum":"2161AF600051","bizContent":{"account":"emp1","password":"123456"}}'))
    print(rs.decrypt("wFAz7aO5HOxSkIXMQwHEU6sSePQhQf7l2Y7CGhAzrAhESV2edPXZfmALQlpyP0iJK6qsHnr9qC5R7B789aBMJIgUf8vndylmJTYYaFr+l13k2/ZaZgJvhIOSVm3s6k9xijbeUz5u3h3n8ly3yySV6MVJgeNT6JrppXOZFBSRiogLIVBnftoZ1ZLYihwqsdcYRAG/iP+kNjhJBdjMiETcvO/BeqabD/aDqAOPpdLEBCWPTetsGq+uD0WVatw9Bld4lfua2b+dyY6D7ZbpHEHlYf4tnhEPcGFnWcxGfxMGo1+Zy/FImaA/UQ3b9br1HV1WeBPmGTpm4eDb1olxzk1SnQ=="))