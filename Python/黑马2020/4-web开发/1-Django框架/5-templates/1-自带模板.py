# django使用自带模板
#     配置
#         1)在工程创建目录templates
#         2)在settings.py配置文件中修改TEMPLATES配置项的DIRS值
#             TEMPLATES = [
#                 ...
#                 'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 此处修改
#                 ...
#             ]
#     定义模板
#         templates文件夹下新建.html文件
#     渲染模板
#         django提供了一个render函数将数据传入模板之中

#         from django.shortcuts import render
        
#         def index(request):
#             context = {
#                 'name':'mass'
#             }

#             return render(request,'index.html',context=context)

#     模板语法
#         1)模板变量
#             变量名必须由字母、数字、下划线(不能以下划线开头)和点组成
#             语法
#                 {{变量}}
#             模板变量可以是python的内建类型，也可以是对象

#         2)模板语句
#             for循环
#             {% for i in iterable %}

#             循环逻辑
#             {{forloop。counter}}表示当前是第几次循环，从1开始
#             {{%empty%}}列表为空或者不存在时执行此逻辑

#             {% endfor %}

#             if 语句
#             {% if ... %}
#             逻辑1
#             {% elif ... %}
#             逻辑2
#             {% else %}
#             逻辑3
#             {% endif %}
            
#             TODO:运算符左右两侧不能紧挨变量或者常量,必须要有空格

#         3)注释
#             单行
#             {# 注释内容 #}
#             多行
#             {% comment %}
#             注释内容
#             {% endcomment%}

# 过滤器
#     语法
#         使用管道符号|来应用过滤器,用于计算、转换操作,可以使用在变量、标签中
#         如果过滤器需要参数,则使用:传递参数
#             变量|过滤器:参数
#             详见main.html

# 模板继承
#     详见base.html(父) & goods.html(子)
