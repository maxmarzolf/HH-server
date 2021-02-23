#!/usr/bin/python3.8
import smtplib
import requests
from email.message import EmailMessage


page = requests.get('http://aws1.harrishillsoaring.org/wordpress/', auth=('user', 'pass'))
if page.status_code != 200:

    msg = EmailMessage()
    msg.set_content('Server Status ' + page.reason)

    msg['Subject'] = 'Server Status'
    msg['From'] = 'marzolfm@aws1.harrishillsoaring.org'
    msg['To'] = 'marzolfm@localhost, jmurtari@localhost'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit
