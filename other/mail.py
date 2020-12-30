from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# 邮件服务器地址
server = 'smtp.163.com'
# 邮件服务器端口号
port = 25

# 发件人地址-登录账户
sender = 'ming111333555@163.com'
# 邮箱密码
pwd = 'zm123456'
# 收件人
receivers = 'zhang111333111@126.com;maolei666@163.com;ming111333555@163.com'

# 创建邮件对象
mail = MIMEMultipart()
# 填写发件人
mail['from'] = sender
# 填写收件人
mail['to'] = receivers
# 主题
mail['subject'] = 'Ranzhi自动化测试'

# 读取报告内容
path = 'report\report_2020-11-18_11-31-01.html'
with open(path,'rb') as file:
    report = file.read()

# 邮件正文
# 创建HTML格式的报告
body = MIMEText(report,'html','utf-8')
# 将报告作为正文添加到邮件中
mail.attach(body)

#邮件附件
attch = MIMEText(report,'base64','utf-8')
# 指定附件的类型
attch['Content-Type'] = 'application/octet-stream'
# 指定附件的处理方式
filename = path.split('/')[-1]
attch['Content-Disposition'] = 'attachment;filename=%s'%filename
# 添加附件
mail.attach(attch)

'''发送邮件'''
# 创建服务器对象
smtp = smtplib.SMTP()
# 连接服务器
smtp.connect(server,port)
# 登录
smtp.login(sender,pwd)
# 发送
smtp.sendmail(sender,receivers.split(';'),mail.as_string())
# 关闭服务器
smtp.close()
print('邮件发送完毕')

