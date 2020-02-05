import csv

#  we can use this for sending emails
with open("file.csv") as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for name, email, grade in reader:
        print(f"Sending email to {name}")
        # send email here
