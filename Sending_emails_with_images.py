# Vey Important
"""
1. Don’t add your Gmail account password in the script.

2. Never add your customer’s email in the script as it is pretty sensitive data, and you might want to keep it secure.

3. Don’t name your script as email.py to avoid conflict with the built-in Python module.
"""

import smtplib


sender_Email = "...@gmail.com"
reciever_Email = "...@gmail.com"
password = input('Enter your email account password: ')

subject = "Test Email from ..."
body = "Bla bla bla"
message = f'Subject: {Subject}\n\n{Body}'


# or
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

   
from_addr_email = "...@gmail.com"
to_addr_email= "...@gmail.com"

msg = MIMEMultipart()
msg['From'] = from_addr_email
msg['To'] = to_addr_email
msg['Subject'] = "Subject of the email"

body = "Bla bla bla"
msg.attach(MIMEText(body, 'plain'))

file_name = "image.png"
attachment = open("Path of the file", "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "Sender password")
text = msg.as_string()
s.sendmail(from_addr_email, to_addr_email, text)
s.quit()


# or

# Example 
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage


strFrom = '...@gmail.com'
strTo = '...@gmail.com'

# Create the root message 
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot['Cc'] =cc
msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>KPI-DATA!', 'html')
msgAlternative.attach(msgText)

#Attach Image 
fp = open('test.png', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

import smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.gmail.com') #SMTp Server Details
smtp.login('exampleuser', 'examplepass') #Username and Password of Account
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()


# or
import imghdr
import smtplib
from email.message import EmailMessage


sender_email = "...@gmail.com"
reciever_email = "...@gmail.com"
password = input('Your email password: ')

new_message = EmailMessage()                         
new_message['Subject'] = "Bla bla bla" 
new_message['From'] = sender_email                   
new_message['To'] = reciever_email                   
newMessage.set_content('Image attached')

with open('file_name.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name
      
new_message.add_attachment(image_data, maintype='image',
                           subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.loginsSender_email, password)              
    smtp.send_message(new_message)



# To send multiple images as attachments
files_list = ['image.png', 'img.gif']

for file in files_list:
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    new_message.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

