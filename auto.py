import smtplib

mail_sender = input("Enter the mail: ")
password = input("Enter the password: ")

mail_rec = input("Enter the recipients mail")

message = """ Subject : Hello there
    Hey, welcome home. """

mail = smtplib.SMTP_SSL('smtp.gmail.com',465)

mail.login(mail,password)

mail.sendmail(mail_sender,mail_rec,message)

mail.quit()