# a class that works as a bridge between 2 incompatible classes

# instead of calling the different methods of the different class,
# just pass in the instance of the adapter that implement the class
# now this class will handle the payment

from abc import ABC, abstractmethod

# class acting as the bridge
class ProcessPayment(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass
    

class GPay:
    def makeGPayPayment(self, amount: int) -> None:
        print(f"Gpay payment made : {amount}")

class Paypal:
    def makePaypalPayment(self, amount: int) -> None:
        print(f"Paypal payment made : {amount}")
        
        
class GPayAdapter(ProcessPayment):
    def __init__(self, gpay: GPay) -> None:
        self.gpay = gpay
    
    def pay(self, amount:int) -> None:
        self.gpay.makeGPayPayment(amount)

class PaypalAdapter(ProcessPayment):
    def __init__(self, paypal: Paypal) -> None:
        self.paypal = paypal
    
    def pay(self, amount: int) -> None:
        self.paypal.makePaypalPayment(amount)


def checkout(paymentMethod: ProcessPayment, amount: int) -> None:
    paymentMethod.pay(amount)



gpay = GPay()
paypal = Paypal()

# ---
print("Gpay payment")
gdapter = GPayAdapter(gpay)
checkout(gdapter, 1000)


print("-"*20)
print("Paypal payment")
paypaladapter = PaypalAdapter(paypal)
checkout(paypaladapter, 2000)