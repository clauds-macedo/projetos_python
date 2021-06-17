import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar(email_from, senha, email_to, email_subject, corpo_msg):
    # email c/ relatório
    smtp = 'smtp.gmail.com'

    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_from, senha)
    email_msg = MIMEMultipart()
    email_msg['From'] = email_from
    email_msg['To'] = email_to
    email_msg['Subject'] = email_subject
    email_msg.attach(MIMEText(corpo_msg, 'html'))
    #enviar
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()