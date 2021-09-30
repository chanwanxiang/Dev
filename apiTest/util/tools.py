from datetime import datetime


def createOrderNum():
    return datetime.now().strftime('%Y%m%d%H%M%S') + '1'.zfill(5)

if __name__ == '__main__':
    print(createOrderNum())
