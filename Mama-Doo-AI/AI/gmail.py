print("gmail service not working rn.......")


def sendMail(content, subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = "@gmail.com"
    receiver_email = "@gmail.com"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # convert both parts to MIMEText objects and add them to the MIMEMultipart message
    part1 = MIMEText(content, "plain")
    message.attach(part1)

    # send your email
    with smtplib.SMTP("smtp.gmail.com", "587") as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login("@gmail.com","")
        smtpserver.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print('Email got sent')
