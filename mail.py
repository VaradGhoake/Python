from __future__ import print_function
import getpass
from twisted.mail.smtp import sendmail
from twisted.internet.task import react

from email.mime.text import MIMEText
passs = getpass.getpass()

def main(reactor):
    me = "varadghodake@gmail.com"
    to = [raw_input("To: ")]

    message = MIMEText(raw_input("Body: "))
    message["Subject"] = raw_input("Subject: ")
    message["From"] = me
    message["To"] = ", ".join(to)

    d = sendmail("smtp.gmail.com", me, to, message,
                 port=587, username=me, password= passs,
                 requireAuthentication=True,
                 requireTransportSecurity=True)

    d.addBoth(print)
    return d

react(main)
