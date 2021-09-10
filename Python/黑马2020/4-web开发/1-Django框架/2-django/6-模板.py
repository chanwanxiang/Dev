# 模板
#     在django中,将前端的内容定义在模板中,然后将模板交给视图调用,返回由模板渲染好的界面

# 模板使用步骤
#     1)创建模板
#     2)设置模板查找路径
#     3)模板接收视图传入数据
#     4)模板处理数据

# 创建模板
#     在应用同级目录创建模板文件夹templates
#     在templates文件夹下,创建应用同名文件夹
#     在应用同名文件夹下创建网页模板文件

# 设置模板查找路径
#     setting.py
#         TEMPLATES[
#             {
#                 'DIRS':[os.path.join(BASE_DIR,'templates')]
#             }
#         ]

# 模板接收视图传入数据
#     def index(request):
#         context = {
#             'name':'Flask'
#         }
#         return reder(request,'Books/index.html',context)

# 模板处理数据
#     {{ name }}
