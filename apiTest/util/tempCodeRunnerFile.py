# coding = utf-8

import os
import smtplib
# from email.mime.text import MIMETest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

fileSendName = '../测试附件.txt'

# 定义发送邮箱对象
class sendMail:

    def __init__(self,mailhost):
        self.mailhost = mailhost

    def send(self,title,content,sender,code,receivers):

        # message = MIMEText(content,'html','utf-8')
        # message['From'] = '{}'.format(sender)
        # message['To'] = ','.join(receivers)
        # message['Subject'] = title

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = '{}'.format(sender)
        message['To'] = ','.join(receivers)
        message['Subject'] = title

        # 添加邮件正文
        message.attach(MIMEText('测试报告详见附件', 'plain', 'utf-8'))
        print(os.getcwd())

        # 构造附件1，传送当前目录下的fileName文件 # TODO: 存在发送邮件附件文件NONAME问题
        addfile = MIMEText(open(fileSendName, 'rb').read(), 'base64', 'utf-8')
        addfile['Content-Type'] = 'application/octet-stream'
        addfile['Content-Disposition'] = 'attachment; filename={}'.format(fileSendName.split('/')[-1])
        message.attach(addfile)

        try:
            # 连接SMTP
            smtpObj = smtplib.SMTP_SSL(self.mailhost,465) # 启用ssl发信,端口一般是465
            smtpObj.login(sender,code) # 登录
            smtpObj.sendmail(sender,receivers,message.as_string())
            print('Send Succeed')
        except Exception as e:
            print('Error:Send Fail' + e)

if __name__ == "__main__":
    # 加载邮箱配置
    mail = sendMail('smtp.qq.com')
    sender = '595366700@qq.com'
    receivers = ['chanwanxiang@yuuwei.com']
    title = '小滴课堂 邮箱测试'
    content = '小滴课堂 xdclass.net'
    code = 'ckuylgvsimotbfgb'

    mail.send(title,content,sender,code,receivers)