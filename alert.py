from smtplib import SMTP
from email.message import EmailMessage


class Alert:
    def email_alert(subject, body, to):
        '''
        This function sends an email alert to the specified email address, and is triggered when an accomodation was found.
        :param subject: subject of email
        :param body: body of email
        :param to: email receiver address
        :output: send email with specified parameters
        :return: print message
        '''
        user = "email"
        password = "password"

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
