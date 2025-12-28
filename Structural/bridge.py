# split classes into closely related hierarchies

from abc import ABC, abstractmethod

class Notify(ABC):
    @abstractmethod
    def msg(self, msg: str):
        pass

class Alert(Notify):
    def msg(self,  msg: str) -> None:
        print("ALERT MSG SENT ", msg)

class Broadcast(Notify):
    def msg(self,  msg: str) -> None:
        print("BROADCAST MSG SENT ", msg)

class NotifyType(ABC):
    def __init__(self, notify:Notify):
        self.notify = notify
    
    def send(self, message: str):
        # self.notify.msg(message)
        pass

class Email(NotifyType):
    def send(self, message:str):
        self.notify.msg(message)

class SMS(NotifyType):
    def send(self, message: str):
        self.notify.msg(message)
        

alert = Alert()
broadcast = Broadcast()

email = Email(alert)
email.send("from email")

sms = SMS(broadcast)
sms.send("from sms")
