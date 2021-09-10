from django.template.defaultfilters import date
from jinja2 import Environment

def environment(**option):
    
    # 创建Environment实例
    env = Environment(**option)

    # 指定(更新)jinja2函数指向django指定过滤器
    env.globals.update({
        'date':date
    })

    # 返回环境实例
    return env