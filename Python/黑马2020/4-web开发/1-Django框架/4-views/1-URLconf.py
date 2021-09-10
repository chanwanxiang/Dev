# URLconf
#     用户通过在浏览器的地址栏中输入网址请求网站
#     对于django开发的网站,由哪一个视图进行处理请求,是由url匹配完成

# 配置URLconf
#     项目setting.py中
#         指定url配置
#             ROOT_URLCONF = '项目.urls'
#     项目中的urls.py
#         匹配成功后,包含到应用的urls.py
#             url(正则,include('应用.urls'))
#     应用中的urls.py
#         匹配成功后,调用views.py对应函数
#             url(正则,views.函数名)
#     提示
#         正则部分推荐使用r,表示字符串不转义,这样在正则表达式中使用\只写一个就可以
#         不能再开始加反斜杠,推荐在结束加反斜杠
#             正确    path/ path
#             错误    /path /path/
#         请求的url被看做一个普通的python字符串,进行匹配时不包括域名,get或post参数
#             如请求地址如下:
#                 https:127.0.0.1:8000/index/?search=`唐诗`
#             去掉域名和参数部分之后,剩下如下部分进行正则匹配
#                 index/
