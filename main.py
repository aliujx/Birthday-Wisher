import smtplib
from random import randint
import datetime as dt
import config

now = dt.datetime.now()
today = now.weekday()
day_to_send = 6

if today == day_to_send:
    with open("quotes.txt") as data:
        motivation = data.read().split("\n")
        letter_to_send = motivation[randint(1, 101)]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=config.my_email, password=config.password)
        connection.sendmail(
            from_addr=config.my_email,
            to_addrs="pakatyak@yahoo.com",
            msg=letter_to_send)
