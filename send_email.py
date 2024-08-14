import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    username = "mesoshooter@gmail.com"
    password = "ctaneqysdsvmvnos"
    receiver = "mesoshooter@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
