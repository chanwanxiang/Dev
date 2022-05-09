from datetime import datetime
from stat import SF_SNAPSHOT
from prestool.Tool import Tool

tool = Tool()

def createOrderNum():
    return datetime.now().strftime('%Y%m%d%H%M%S') + '0'.zfill(2)





if __name__ == '__main__':
    for i in range(20):
        name = tool.random_name()
        phone = tool.random_phone()
        id = tool.random_ssn()
        print(name, phone, id)
