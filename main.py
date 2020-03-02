import subprocess
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
emails = ["venance@right-com.com", "divyam@right-com.com", "osee@right-com.com", "durandelegba@gmail.com"]
while True:
    for mail in emails:
        me = "support@rightcomtech.com"
        you = mail
        os.system('./jota-cert-checker.sh -f sitelist -o html')
        fp = open('certs_check.html', 'r')
        HTML_BODY = MIMEText(fp.read(), 'html', 'utf-8')
        msg = MIMEMultipart('alternative')
        fp.close()
        msg['Subject'] = 'SSL Certificates Status'
        msg['From'] = me
        msg['To'] = you
        msg.attach(HTML_BODY)
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login("support@rightcomtech.com","jrdulurkgclezdyl")
        s.sendmail(me, [you], msg.as_string())
        s.quit()
    time.sleep(604800)