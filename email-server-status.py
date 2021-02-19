#!/usr/bin/python3.8
import smtplib
import urllib.request
from email.message import EmailMessage

page = urllib.request.urlopen('http://aws1.harrishillsoaring.org/wordpress/')
if page.status != 200:
    msg = EmailMessage()
    msg.set_content('Server Status ' + page.reason)

    msg['Subject'] = 'Server Error'
    msg['From'] = 'marzolfm@aws1.harrishillsoaring.org'
    msg['To'] = 'marzolfm@localhost, jmurtari@localhost'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit