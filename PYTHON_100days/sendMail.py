# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText

# def main():
#     sender = 'chenyisha37@126.com'
#     receivers = ['chenchen9037@126.com']
#     message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
#     message['From'] = Header('王大锤', 'utf-8')
#     message['To'] = Header('骆昊', 'utf-8')
#     message['Subject'] = Header('示例代码实验邮件', 'utf-8')
#     smtper = SMTP('smtp.126.com')
#     smtper.login(sender, 'c82e69bby3')
#     smtper.sendmail(sender, receivers, message.as_string())
#     print('邮件发送完成！')

# if __name__ == '__main__':
#     main()

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)
    # attachments

    # 创建SMTP对象
    smtper = SMTP('smtp.126.com')
    sender = 'chenyisha37@126.com'
    receivers = ['chenchen9037@126.com']
    # 登录到SMTP服务器
    smtper.login(sender, 'xxxxx')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('mail is send!')

if __name__ == '__main__':
    main()