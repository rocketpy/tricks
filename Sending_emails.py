import smtplib


sender_email = "...@gmail.com"
reciever_email = "...@gmail.com"
password = input('Your email password: ')

subject = "Test"
body = "Bla bla bla"
message = f'Subject: {Subject}\n\n{Body}'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, reciever_email, message)
    
# or
import smtplib, ssl


port = 465
password = input("Your password: ")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("...@gmail.com", password)

