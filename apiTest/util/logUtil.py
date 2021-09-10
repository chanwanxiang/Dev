import os
import sys

from loguru import logger


class LoggerUtil:
    logsPath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'logs/')
    logstyle = "<green>{time:YYYY-MM-DD HH:mm:ss,SSS}</green> <red>[{thread}]</red> <blue>{level}</blue> <cyan>名称:{name}</cyan> <green>方法:{function}</green> {line}\n<red>{message}</red>"

    logsFile = False

    def __init__(self, logsFile):
        # 重新开始
        logger.remove()
        if logsFile:
            # 文件输出
            logger.add(self.logsPath + '{time:YYYY-MM-DD}.log', format=self.logstyle, 
                rotation='00:00', retention='30 days', colorize=True, enqueue=True)
            
        # 控制台输出
        logger.add(sys.stdout, colorize=True, level='debug', format=self.logstyle)
