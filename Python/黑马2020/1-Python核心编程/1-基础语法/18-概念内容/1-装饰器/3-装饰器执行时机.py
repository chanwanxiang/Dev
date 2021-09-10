# 装饰器的执行时机:当前模块加载完成之后,装饰器会立即执行,对已有函数进行装饰

import myDecorator

myDecorator.comment()  #登录验证完成\r\n 发表评论 结果并非单一comment()函数执行之后发表评论