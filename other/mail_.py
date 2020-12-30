from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# 邮件服务器地址
server = 'smtp.163.com'
# 邮件服务器端口号
port = 25

# 发件人地址-登陆账号
sender = 'jingying0037@163.com'
# 邮箱密码
pwd = 'AVNCNFWSUJQEALFA'
# 收件人
receivers = 'jingying0037@163.com;houfujun07@163.com;maoalei666@163.com'

# 创建邮件对象
mail = MIMEMultipart()
# 填写发件人
mail['from'] = sender
# 填写收件人
mail['to'] = receivers
# 主题
mail['subject'] = 'Ranzhi自动化测试报告！'

# 读取报告的内容
path = r'report\report_2020-11-18_11-19-08.html'
with open(path,'rb') as file:
    report = file.read()

# 邮件正文
# 创建HTML格式的消息对象
body = MIMEText(report,'html','utf-8')
# 将报告作为正文添加到邮件中
mail.attach(body)

# 邮件附件
attch = MIMEText(report,'base64','utf-8')
# 指定附件内容的类型
attch['Content-Type'] = 'application/octet-stream'
# 指定附件的处理方式
filename = path.split('/')[-1]
print(filename)
attch['Content-Disposition'] = 'attachment;filename=%s'%filename
# 添加附件
mail.attach(attch)

'''发送邮件'''
# 创建服务器对象
smtp = smtplib.SMTP()
# 连接服务器
smtp.connect(server,port)
# 登陆
smtp.login(sender,pwd)
# 发送
smtp.sendmail(sender,receivers.split(';'),mail.as_string())
# 关闭服务器
smtp.close()
print('邮件发送完毕！')
