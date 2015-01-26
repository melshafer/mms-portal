# File: send_email.py
# Melanie Shafer, 2015

import smtplib
import config
import format_output

def send_email(from_addr, to_addr_list, subject, message, login, password, smtpserver='smtp.gmail.com:587'):

    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()


send_email(from_addr    =  config.from_addr,
           to_addr_list =  config.to_addr_list,
           subject      = 'Email from MMS Portal - {}'.format(config.student_name),
           message      =  format_output.message,
           login        =  config.email_login,
           password     =  config.email_password)
