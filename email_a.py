#!/usr/bin/env python3

#antuor:Alan



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# to_add = input('请输入收件邮箱:')
# msg = MIMEText('喂,我啊', 'plain', 'utf-8')       #邮件内容可以加载文件
# msg['From'] = formataddr(["吕毅",'37172515@qq.com'])
# msg['To'] = to_add
# msg['Subject'] = "自动化测试"
#
# server = smtplib.SMTP_SSL('smtp.qq.com',465)
# server.connect('smtp.qq.com',465)
# server.login("371725153@qq.com", "python")
# server.sendmail('371725153@qq.com', [to_add], msg.as_string())
# server.quit()


########################################测试成功#######################################
from_mail = '371725153@qq.com'       #发件人
to_mail = input('请输入收件邮箱:')   #收件人
email_text = input('请输入发信内容:')  #邮件内容

msg = MIMEText(email_text,'plain','utf-8')  #文本内容
msg['Subject'] = email_text         #主题
msg['from'] = from_mail             #收件人



try:         #补抓异常,只显示不处理
    mail = smtplib.SMTP_SSL('smtp.qq.com',465)
    mail.connect('smtp.qq.com',465)
    mail.login('371725153@qq.com','python')
    mail.sendmail(from_mail,to_mail,msg.as_string())
    mail.close()

    print ('发送提醒邮件成功')

except :
    pass