from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

#urname=argv[1] # first arguement as sender's username
urname='**@**.com'
#pwd=argv[2] # second arguement as sender's password
# send message
pwd='**'
#mess=argv[1]
message=MIMEText('mess',_charset='utf-8')
message['Subject']=Header('Test mail subject','utf-8')
From=urname
to='@qq.com' # To address
s=SMTP_SSL('smtp.qq.com',465,timeout=10)
try:
    s.login(urname,pwd)
    s.sendmail(From,to,message.as_string())
finally:
    s.quit()
