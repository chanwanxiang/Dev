import subprocess

def getlogcat(packName=None):
    command = f'adb logcat | grep "{packName}"'
    try:
        logcatprocess = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        logcatoutput, _ = logcatprocess.communicate()
        return logcatoutput.decode('utf-8')
    except Exception as e:
        print(f"获取日志失败: {e}")
        return None

logcatoutput = getlogcat('com.yuuwei.gsfaceview')
print(logcatoutput)