# factory method pattern -> the behaviour of a method can be decided by the subclass

from abc import ABC, abstractmethod


class Notify(ABC):
    
    @abstractmethod
    def notify(self, message: str) -> None:
        pass
    
class SMSNotify(Notify):
    
    def notify(self, message: str) -> None:
        print(f"SMS message sent : {message}")

class EmailNotify(Notify):
    
    def notify(self, message: str) -> None:
        print(f"Email notifiction sent : {message}")


sms = SMSNotify()
sms.notify("Hello world")

print("-"*20)

email = EmailNotify()
email.notify('Hello world')
