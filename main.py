import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('test.html').read_text())
email = EmailMessage()
email['from'] = 'Harish Soni'
email['to'] = 'receiver email'
email['subject'] = 'testing'
email.set_content(html.substitute(name='Harish soni'),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('senderemail','senderpassword')
    smtp.send_message(email)
    print('Message sent successfully')