from flask_mail import Mail, Message


class SendMail:
    def __init__(self, app, sender_email):
        self.sender_email = sender_email
        self.app = app
        self.mail = Mail(self.app)

    def compile_mail(self, subject, message_body, recipients):
        message = Message(sender=self.sender_email, subject=subject, recipients=recipients)
        message.body = message_body
        return message

    def send_mail(self, river_level_prediction, recipient_list):
        if recipient_list is None or len(recipient_list) is 0:
            print("No Email Subscription...!")
            return
        subject = f'Prediction for {river_level_prediction.river_name} at {river_level_prediction.station_name}'
        message = f'Prediction: {river_level_prediction.prediction}'
        mail = self.compile_mail(subject, message, recipients=recipient_list)
        with self.app.app_context():
            try :
                self.mail.send(mail)
            except:
                print("Please setup email account...!")
                return
        print("Emails Sent...")

