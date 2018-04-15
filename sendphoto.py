#!/usr/bin/env python
"""
Home Automation: sends an e-mail with a photograph attachment
For the Raspberry Pi
"""
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
def emailphoto(msgtext, afilename):
 #enter the e-mail account username between the quotes
 smtp_user = "sendfromhere@gmail.com"
 #enter the e-mail account password between the quotes
 smtp_pass = "password"
 msg = MIMEMultipart()
 #enter the target e-mail address between the quotes
 msg['To'] = "private@gmail.com"
 #enter the e-mail account username between the quotes
 msg['From'] = "webcam"
 #enter the message subject between the quotes
 msg['Subject'] = "Motion was detected"
 #That is what you see if don't have an e-mail reader:
 msg.preamble = 'Multipart message.\n'
 #sys.argv[1] is the 1st parameter that is passed to this
 #and it contains the text for the body of the e-mail
 part = MIMEText(msgtext)
 msg.attach(part)
 #The next 3 lines attach the photo using the filename
 #passed in as the second parameter to this program
 part = MIMEApplication(open(afilename,"rb").read())
 part.add_header('Content-Disposition', 'attachment', filename=afilename)
 msg.attach(part)
 #enter the SMTP server URL or IP Address between the quotes
 s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
 s.login(smtp_user,smtp_pass)
 s.sendmail(msg['From'], msg['To'], msg.as_string())
 s.quit()
def main():
 emailphoto(sys.argv[1], sys.argv[2])
if __name__ == "__main__":
 main()s