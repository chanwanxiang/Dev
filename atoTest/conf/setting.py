import os
import sys
import logging

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(DIR_PATH)

# 日志输出级别
LOG_LEVEL = logging.DEBUG
STREAM_LOG_LEVEL = logging.DEBUG

# 文件路径
FILE_PATH = {
    'CONFIG': os.path.join(DIR_PATH, 'conf', 'conf.ini'),
    'LOG': os.path.join(DIR_PATH, 'logs')
}
