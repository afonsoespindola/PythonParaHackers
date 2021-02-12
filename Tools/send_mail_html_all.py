import smtplib
import email.message
server = smtplib.SMTP('smtp.SEUHOST.com.br:587')
 
email_content = """

 
 
"""
 
msg = email.message.Message()
msg['Subject'] = 'TITULO'

msg['From'] = 'SEUEMAIL@mail.com.br'
password = "SENHA"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)


 
s = smtplib.SMTP('smtp.domain.com.br: 587')
s.starttls()
 
# Login Credentials for sending the mail
s.login(msg['From'], password)

arq = open("mail_list.txt", "r")
for i in arq:
    msg = email.message.Message()
    msg['Subject'] = 'TITULO'
     
     
    msg['From'] = 'SEUEMAIL@mail.com.br'
    msg['To'] = i
    password = "SENHA"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
     
    s = smtplib.SMTP('smtp.domain.com.br: 587')
    s.starttls()
     
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
     
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    print (i)





