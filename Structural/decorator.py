# extending the exisiting functionality without making changes to the original one


# Notification already existed
# but now the notification can be some other types like encryption and logging
# so for that a decorator is created that callls the required send method for the type of notify object 
# that was created during object creation

from abc import ABC, abstractmethod

class Notify(ABC):
    @abstractmethod
    def send(self):
        pass
    
class EmailNotify(Notify):
    def send(self):
        print("email is sent")
class SMSNotify(Notify):
    def send(self):
        print("sms is sent")

class NotifyDecorator(Notify):
    def __init__(self, notify: Notify):
        self._notify = notify
    
    def send(self):
        self._notify.send()

class LogNotify(NotifyDecorator):
    def send(self):
        print("logging a message")
        super().send()

class EncryptNotify(NotifyDecorator):
    def send(self):
        print("encrypting the message")
        super().send()
        

email = EmailNotify()
sms = SMSNotify()

# logs will be sent to sms
login = LogNotify(sms)
login.send()
print("-"*20)
# encryption will be sent to  emails
encrypt = EncryptNotify(email)
encrypt.send()
