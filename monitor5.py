import psutil
import smtplib

# function to send an email alert
def send_alert(subject, body):
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

# function to check usage and send alerts
def check_usage():
    # get system-wide information
    info = psutil.info()

    # check if storage is over 80%
    if info.memory_percent > 80.0:
        send_alert('Storage Alert', 'Storage is over 80% on the server')

    # check if RAM is over 80%
    if info.memory_percent > 80.0:
        send_alert('RAM Alert', 'RAM usage is over 80% on the server')

    # check if CPU is over 80%
    if info.cpu_percent > 80.0:
        send_alert('CPU Alert', 'CPU usage is over 80% on the server')

# check usage periodically (every 5 minutes)
while True:
    check_usage()
    time.sleep(300)
