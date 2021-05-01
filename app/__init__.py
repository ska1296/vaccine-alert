import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

pincode = "250004"
date = "01-05-2021"

PARAMS = {'pincode': pincode, "date": date}

r = requests.get(url=URL, params=PARAMS)
data = r.json()
centers = data['centers']


def sendEmail(session):
    sender = "ska1296@gmail.com"
    password = 'trolled12345!'
    receiver = "ska1296@gmail.com"
    email_message = "HELLO!\nVaccine available at:\n" + session
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'URGENT: Vaccine available!!'  # The subject line
    message.attach(MIMEText(email_message, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender, password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent')


x = ''
for center in centers:
    sessions = center['sessions']
    name = center['name']
    for session in sessions:
        if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
            pretty_session = json.dumps(session, indent=3)
            x = x + name + ' --> ' + pretty_session + '\n'

sendEmail(x)
