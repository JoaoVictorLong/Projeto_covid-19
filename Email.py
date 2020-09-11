import smtplib

#def email(mail):

smtpserver = smtplib.SMTP('smtp.outlook.com', 587)
smtpserver.ehlo()
smtpserver.starttls()

msg = ''
