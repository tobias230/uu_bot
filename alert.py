from smtplib import SMTP
from email.message import EmailMessage


class Alert:
    def email_alert(subject, body, to):
        # gmx account
        user = "tobias.zenner@gmx.de"
        password = "T0b1aS99"

        # mail message init
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        msg['from'] = user

        server = SMTP("mail.gmx.com", 25)
        server.starttls()
        server.login(user, password)

        try:
            server.sendmail(user, to, msg.as_string())
        finally:
            print("message was send to " + to + " with content: " + body)
            server.quit()
