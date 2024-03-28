import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart  # contains both textual and attachements , which allows you to construct complex email messages
from email.mime.text import MIMEText # it creates only the plains text
 
from_addr = 'tarapranay134@gmaill.com'

data = pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\PYTHON_CWH\Mini_projects\kpkp.csv" , encoding='utf-8')
to_addr = data['EMAIL'].tolist()
# name = data['name'].tolist()

l = len(to_addr)
email = "tarapranay134@gmail.com"
password = "dups lwsa aatl ekdm"

for i in range (l):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr[i]
    msg['subject'] = 'Just to Check'

    body = "Hello , How are you . I love you so much yrr . SEX KROGEE? Call:7780451128"

    msg.attach(MIMEText(body,'plain'))

    mail = smtplib.SMTP('smtp.gmail.com' , 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)
    text = msg.as_string()
    mail.sendmail(from_addr , to_addr[i] , text)
    mail.quit()

