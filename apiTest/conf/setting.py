import  os, sys
import  logging

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(DIR_PATH)

# 日志输出级别
LOG_LEVEL = logging.DEBUG
STREAM_LOG_LEVEL = logging.DEBUG

# 文件路径
FILE_PATH = {
    'testcase': os.path.join(DIR_PATH, 'testcase','login','login.yaml'),
    'extract': os.path.join(DIR_PATH, 'extract.yaml'),
    'config': os.path.join(DIR_PATH, 'conf', 'conf.ini'),
    'log':os.path.join(DIR_PATH, 'log')
}

print(FILE_PATH['config'])
