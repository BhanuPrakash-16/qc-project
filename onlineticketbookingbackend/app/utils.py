import smtplib, random
from email.mime.text import MIMEText

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email(to_email: str, subject: str, body: str):
    sender = "bhanualluri2006@gmail.com"
    password = "bdrjcpycikwpvybk"  # Gmail App Password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("Email error:", e)
        return False
