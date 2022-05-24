import redis

class ReidsPool():

    def __init__(self):
        # 建立redis连接 host='127.0.0.1', port=3333, user='root', password='123456', database='xdclass'
        self.conn = redis.Redis(host='47.97.41.159', port='6379', password='FvDev@2020-yuuwei', decode_responses=True,charset='utf-8', encoding='utf-8')

    def __del__(self):
        # 关闭连接
        self.conn.close()
    
    def setVal(self, key, val):
        # 在redis中创建值，默认不存在就创建，存在就修改
        self.conn.set(key, val)

    def query(self, key):
        return self.conn.get(key)

    def delVal(self, key):
        self.conn.delete(key)


if __name__ == "__main__":
    rediconn = ReidsPool()
    print(rediconn.query('FORBIDDEN_FOR_INCORRECT_ANSWER_CLIENTID'))
    rediconn.delVal('FORBIDDEN_FOR_INCORRECT_ANSWER_CLIENTID:330122199408143218')
