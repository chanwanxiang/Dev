# logging日志

# 1. logging日志的介绍
#     1. 可以很方便的了解程序运行情况
#     2. 可以分析用户操作行为喜好等信息
#     3. 方便开发检查bug

# 2. logging日志及别介绍

import logging

# 设置logging日志的配置信息
# %(asctime)s       当前时间
# %(filename)s      程序文件名称
# %(lineno)d        行号
# %(levelname)s     日志级别
# %(message)s       日志信息
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s',
                    filename = 'log.txt',
                    filemode = 'a') 

logging.debug('debug info')
logging.info('info info')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')

# 默认是warning,只有大于等于warning级别的日志才会输出显示
