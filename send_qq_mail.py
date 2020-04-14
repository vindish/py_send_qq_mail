# -*- coding: utf-8 -*-
# import smtplib
from email.mime.text import MIMEText
import time
# import MySQLdb
from email.header import Header
from smtplib import SMTP_SSL
import pymysql
import random

# 从数据库中获取ip地址列表
def get_addr():
    # 连接数据库
    # conn = MySQLdb.Connection('localhost', 'root', '123456', 'muchmail', port=3306)
    conn = pymysql.connect('localhost', 'root', '123456', 'muchmail', port=3306)
    cursor = conn.cursor()
    # 执行SQL语句，获取邮箱地址
    cursor.execute("SELECT * FROM mail")
    result = cursor.fetchall()
    return result


def send_qq_email(to_list, title, content):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = '551295296'
    # pwd为qq邮箱的授权码
    pwd = 'hhdqasdasfasfeh'
    # 发件人的邮箱
    sender_qq_mail = '551295296@qq.com'
    # 收件人邮箱
    receiver = to_list
    # receiver = ""

    # 邮件的正文内容
    mail_content = content
    # 邮件标题
    mail_title = title
    try:
        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(0)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        # msg = MIMEText(mail_content, "plain", 'utf-8')
        msg = MIMEText(mail_content, "html", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        # msg["To"] = ';'.join(receiver)
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        print('发送 邮件成功 ')
    except Exception as e:
        print('发送 邮件失败,原因是 {}'.format(e))
        # 只需要更改 host_server 、sender_qq、pwd、sender_qq_mail、receiver、mail_content、mail_title等数据，就可以实现简单的发送任务。
        # MIMEText函数中的第二个参数为“plain”时，发送的是text文本。如果为“html”，则能发送网页格式文本邮件。



if __name__ == '__main__':

    result = get_addr()
    for record in result:
        title = "Hi!"+(record[1])+"您好！"

        line1 = "这是第一行"
        # 邮件正文第一行内容
        line2 = "这是第二行"
        # 邮件正文第二行内容
        line3 = "这是第三行"
        # 邮件正文第三方内容

        content = "Hi!"+(record[1])+"您好！"+'''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8" />
<title>--------</title>
<style>
    .p1{text-indent: 40px;}
    .p2{text-indent: 2em;}
</style>
</head>
<body>
    <p class="p2">依据《安全生产法》、《企业安全生产标准化基本规范》、《企业安全生产标准化评审工作管理办法（试行）》等有关法律法规规定，企业必须开展安全生产标准化活动。</p>
    <p class="p2">“党政同责，一岗双责，尽职免责，失职追责”。</p>
    <p class="p2">我司可免费为贵公司进行安全生产标准化评估、安全生产培训，如有需要请发邮件到<a href="mailto:5519296@qq.com">5519296@qq.com</a>或致电<a href="tel:17683789069">17683789069</a>。</p>
    <p class="p2">------------------------------</p>
    <p align="right"><a href="http://www.hbkykc.com/">湖北开源</a><br>聂工</p>
    <p class="p2">------------------------------</p>
    <p class="p2">公司在大地国际23楼，期待您的光临！</p>
    <p class="p2">------------------------------</p>
</body>
</html>
'''
        reciver = record[5]
        print("发邮件给：", reciver)
        send_qq_email(reciver, title, content)
        # 休眠5秒，短时间大量发送邮件可能会造成发送失败或者账号被封
        time.sleep(random.randint(5, 10))
        break

    # 也可以直接填写对方的邮箱账号
    # send_mail("17704628364@163.com")