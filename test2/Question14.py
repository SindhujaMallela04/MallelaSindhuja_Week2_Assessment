class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def __init__(self, message):
        self.message = message
    def send(self):
        print(f"The message \"{self.message}\" has been sent successfully.")

class SMSNotification(Notification):
    def __init__(self, message):
        self.message = message
    def send(self):
        print(f"The message \"{self.message}\" has been sent successfully.")

def main():
    print("Email Notification: ")
    email_notification = EmailNotification("Hey there!, Hope you are doing well.")
    email_notification.send()
    print("SMS Notification: ")
    sms_notification = SMSNotification("Hii!!, Howdy?")
    sms_notification.send()
main()
