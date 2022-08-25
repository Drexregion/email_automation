from urllib import response
from click import prompt
import requests
from bs4 import BeautifulSoup

# Extended Simple Mail Transfer Protocol (ESMTP)
import smtplib

# for email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# manipulate the system date and time
import datetime

now = datetime.datetime.now()

# email content place holder  
content = ""

# helps to extract the news in a serial manner
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt+=('<b>HN Top Stories:</b>\n' +'<br>'+'-'*50 +'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('a',attrs={'class':'titlelink','valign':''})):
        cnt += (str(i+1) + '::'+ tag.text + "\n" +"<br>"
        if tag.text!='More'
        else "")
    return(cnt)
   
extract_news('https://news.ycombinator.com/')
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content +=('<br>------------<br>')
content +=('<br><br>End of message')
# content_1 ='hello'

# lets send this email
print('composing email')

# update your email details 
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'drexindustries06@gmail.com'
TO = 'drexregion1@gmail.com'
PASS = '************'
 
msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories HN [Automated Email]'+''+ str(now.day) + '-' + str(now.month) + '-' + str(now.year) 
msg['From'] = FROM
msg['To']  = TO

msg.attach(MIMEText(content,'html'))

print('initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
# We want to see the error messages from the server
server.set_debuglevel(1)

# Ensures connection between the two email servers
server.ehlo()

# helps to create a secure connection 
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO, msg.as_string())

print('Email sent...')

server.quit()
 