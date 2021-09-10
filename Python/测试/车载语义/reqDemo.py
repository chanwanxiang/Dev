import json,requests
from openpyxl import Workbook

# 请求地址 现网地址 测试环境
urlOnline = r'http://aquadev.iflytekauto.cn/athena/iss?ver=3.1&method=query&appid=587ed53b&text=%E6%89%93%E5%BC%80%E5%AF%BC%E8%88%AA&uid=8dbejh'

urlSample = r'http://dfirresgray.iflytekauto.cn/dragon/iss?ver=3.1&method=query&open.dialog=true&text=%E6%89%93%E5%BC%80%E5%AF%BC%E8%88%AA&uid=001&appid=587ed53b'

# 发送get请求
responseOnline = requests.get(urlOnline)
responseSample = requests.get(urlSample)

# rltOnline,rltSample = responseOnline.json(),responseSample.json()


rltOnline = json.loads(responseOnline.text)
print(rltOnline)



# # 现网 测试环境 业务 操作 语义
# serOnline,opeOnline,semOnline = rltOnline['service'],rltOnline['operation'],rltOnline['semantic']
# serSample,opeSample,semSample = rltSample['service'],rltSample['operation'],rltSample['semantic']

# lsWrite = list(map(str,[serOnline,opeOnline,semOnline,serSample,opeSample,semSample]))

# # 创建写入文件
# wb = Workbook()
# sheet = wb.worksheets[0]
# sheet.title = 'result'

# lstitle = ['appid','usrid','自定义参数','uid','user_data','text','service标注','operation标注','semantic标注','service','operation','semantic','service对比','operation对比','semantic对比'] 

# sheet.append(lstitle)

# sheet.append(lsWrite)

# wb.save('result.xls')

# # 获取数据
# print(serOnline,serSample)
# print(opeOnline,opeSample)
# print(semOnline,semSample)
