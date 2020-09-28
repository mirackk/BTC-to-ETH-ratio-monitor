import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
mail_user = 'mirack_cty'
mail_pass = 'KKTHFWVNRDGUYHDX'
sender = 'mirack_cty@163.com'
receivers = ['872645693@qq.com']

message = MIMEText('test content', 'plain', 'utf-8')
message['Subject'] = 'title'
message['From'] = sender
message['To'] = receivers[0]

try:
    print('start')
    smtpObj = smtplib.SMTP()
    print('start1')
    smtpObj.connect(mail_host, 25)
    print('start2')
    smtpObj.login(mail_user, mail_pass)
    print('start3')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('start4')
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)
