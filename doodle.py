# from signal import alarm
# from curses import delay_output
from email.mime import message
from email.mime.text import MIMEText
import smtplib
from turtle import delay
from bs4 import BeautifulSoup
import requests
import datetime
import time
# from click import prompt
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'drexindustries06@gmail.com'
TO = 'joeleyo18@gmail.com'
PASS = 'xxxxxxxxxxxx'

current_time = datetime.datetime.now()
set_date_time = datetime.datetime(2022,7,8,23,59  ,55  )
date_time_delta = current_time - set_date_time
seconds_delta = abs(date_time_delta.total_seconds())
def birthday_gift():
    time.sleep(seconds_delta)
    print('Sending email.....')
    print("initializing server")

    messages = MIMEMultipart()
    messages['Subject'] = ' Automated Happy birthday' + str(datetime.datetime.now())
    messages['From'] = FROM
    messages['To'] = TO
    messages.attach(MIMEText('Happy birthday bro!!!!!!!!! THIS MESSAGE IS SENT TO YOU THROUGH AN AUTOMATED CODE USING PYTHON'))
    # print (current_time- date_time)
    # def delay_code():
    #     while datetime.datetime.now

    # Initialize the server
    server = smtplib.SMTP(SERVER,PORT)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(FROM,PASS)
    server.sendmail(FROM,TO, messages.as_string())

    print('email sent!!!!')
    server.quit()
birthday_gift()
