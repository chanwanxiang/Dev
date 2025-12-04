import os
import time
import logging
from conf import setting
from logging.handlers import RotatingFileHandler


logpath = setting.FILE_PATH['LOG']
if not os.path.exists(logpath):
    os.makedirs(logpath)

logfile = logpath + r'/test.{}.log'.format(time.strftime("%Y%m%d"))


class LogUtil:

    def logoutput(self):
        logger = logging.getLogger(__name__)
        if not logger.handlers:
            logger.setLevel(setting.LOG_LEVEL)
            logformatter = logging.Formatter(
                '\n%(asctime)s - %(levelname)s - %(name)s - %(filename)s : %(lineno)d - [%(module)s:%(funcName)s] - %(message)s')
            fh = RotatingFileHandler(filename=logfile, mode='a', maxBytes=5242800, backupCount=7, encoding='utf-8')
            fh.setLevel(setting.LOG_LEVEL)
            fh.setFormatter(logformatter)
            logger.addHandler(fh)

            # 日志输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(setting.STREAM_LOG_LEVEL)
            sh.setFormatter(logformatter)
            logger.addHandler(sh)

        return logger

lg = LogUtil()
logs = lg.logoutput()
