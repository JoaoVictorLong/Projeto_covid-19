import smtplib

#def email(mail):
my_email = "email"
recevi_email = "email"

server = smtplib.SMTP('localhost','1025')

mensage = """Subject: Covid-19 \
From: voce


testando %s
"""%(joao)



server.sendmail(my_email, recevi_email, mensage)
