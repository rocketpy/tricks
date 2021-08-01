import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


MY_EMAIL = "..."
MY_PASSWORD = "..."
RECIPIENT_ADDRESS = "..."
HOST_ADDRESS = 'smtp.host_address.com'
HOST_PORT = 587


server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_EMAIL, MY_PASSWORD)

message = MIMEMultipart()

message['From'] = MY_EMAIL
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Automated Email"

textPart = MIMEText("Here is a some text", 'Topic')

message.attach(textPart)

# to send
server.send_message(message)
server.quit()
 
