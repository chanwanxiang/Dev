import openpyxl

wb = openpyxl.Workbook()
sheet1 = wb.worksheets[0]
sheet1.title = 'case'

sheet2 = wb.create_sheet('config')

listwrite1 = [('id', 'app', 'module', 'title', 'method', 'url', 'run', 'headers', 'pre_case_id', 'pre_fields', 'request_body', 'expect_result', 'assert_type', 'pass', 'msg', 'update_time', 'response'),
            (1,'小滴课堂','user','用户登录','post','/pub/api/v1/web/web_login','yes','{\"Content-Type\": \"application/x-www-form-urlencoded\"}',-1,'[]','{\"phone\": \"13113777555\", \"pwd\": \"1234567890\"}','0','code','True','模块:user, 标题:用户登录,断言类型:code,响应:None','2020-07-04 12:01:25',''),
            (4,'小滴课堂','order','用户订单列表','get','/user/api/v1/order/find_orders','yes','{\"token\":\"$token$\"}',1,'[{\"field\":\"token\",\"scope\":\"header\"}]','{}','0','data_json','True','模块:order, 标题:用户订单列表,断言类型:data_json,响应:None','2020-07-04 12:01:25',''),
            (5,'小滴课堂','video','首页视频卡片','get','/pub/api/v1/web/index_card','yes','{}',-1,'[]','{}','0','data_json_array','True','模块:video, 标题:首页视频卡片,断言类型:data_json_array,响应:None','2020-07-04 12:01:25',''),
            (6,'小滴课堂','user','用户个人信息','get','/pub/api/v1/web/user_info','yes','{\"token\":\"$token$\"}',1,'[{\"field\":\"token\",\"scope\":\"header\"}]','{}','0','data_json','True','模块:user, 标题:用户个人信息,断言类型:data_json,响应:None','2020-07-04 12:01:25',''),
            (7,'小滴课堂','favorate','新增收藏','post','/user/api/v1/favorite/save','yes','{\"token\":\"$token$\", \"Content-Type\": \"application/x-www-form-urlencoded\"}',1,'[{\"field\":\"token\",\"scope\":\"header\"}]','{\"video_id\":53}','0','code','True','模块:favorate, 标题:新增收藏,断言类型:code,响应:None','2020-07-04 12:01:25',''),
            (8,'小滴课堂','category','分类列表','get','/pub/api/v1/web/all_category','yes','{}',-1,'[]','{}','0','data_json_array','True','模块:category, 标题:分类列表,断言类型:data_json_array,响应:None','2020-07-04 12:01:26',''),
            (9,'小滴课堂','video','视频详情','get','/pub/api/v1/web/video_detail','yes','{}',-1,'[]','{\"video_id\":53}','0','data_json','True','模块:video, 标题:视频详情,断言类型:data_json,响应:None','2020-07-04 12:01:26',''),
            (10,'小滴课堂','favorate','我的收藏','get','/user/api/v1/favorite/page','yes','{\"token\":\"$token$\"}',1,'[{\"field\":\"token\",\"scope\":\"header\"}]','{}','0','data_json','True','模块:favorate, 标题:我的收藏,断言类型:data_json,响应:None','2020-07-04 12:01:26','')]

listwrite2 = [('id', 'app', 'dict_key', 'dict_value'),
            (1,'小滴课堂','host','https://api.xdclass.net'),
            (2,'小滴课堂','mail_sender','waitforxy@126.com'),
            (3,'小滴课堂','mail_auth_code','HDPLOKWBQMVTVISG'),
            (4,'小滴课堂','mail_receivers','794666918@qq.com,waitforxy@126.com'),
            (5,'小滴课堂','mail_host','smtp.126.com')]

for x in listwrite1:
    sheet1.append(x)

for y in listwrite2:
    sheet2.append(y)

app = '小滴课堂'

# allCase = [x for x in list(sheet1.values) if x[1] == app]
# keyvalue = list(list(sheet1.values)[0])
# # print(keyvalue)
# listN = []
# dictN = {}
# for x in allCase:
#     listdict = list(zip(list(sheet1.values)[0],x))
#     for x in listdict:
#         dictN[x[0]] = x[1]
#     listN.append(dictN)
#     dictN = {}
    
# # for x in listN:
# #     print(x)

# col1 = sheet1['A']
# print([x.row for x in col1])

# for x in allCase:
#     if x[1] == '小滴课堂':
#         print(x)

# wb.save('测试用例.xlsx')
