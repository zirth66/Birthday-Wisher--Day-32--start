import smtplib

my_email = "daniel.persson.test@gmail.com"
password = "Y1Vv&8n8!&1w"
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="zirth@yahoo.com", 
        msg="Subject:Hello\n\nThis is the body of my email"
    )
