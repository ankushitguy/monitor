import psutil
import smtplib

# function to send an email notification
def send_email(subject, body):
    # configure SMTP server
    server = smtplib.SMTP('smtp.example.com')
    server.starttls()
    server.login('username', 'password')

    # build and send the email
    msg = MIMEMultipart()
    msg['From'] = 'server-monitor@example.com'
    msg['To'] = 'admin@example.com'
    msg['Subject'] = subject
    msg.attach(MIMEText(body))
    server.send_message(msg)

# get system-wide information
info = psutil.info()

# check if storage is over 80%
if info.memory_percent > 80.0:
    send_email('Storage Alert', 'Storage is over 80% on the server')

# check if RAM is over 80%
if info.memory_percent > 80.0:
    send_email('RAM Alert', 'RAM usage is over 80% on the server')

# check if CPU is over 80%
if info.cpu_percent > 80.0:
    send_email('CPU Alert', 'CPU usage is over 80% on the server')
