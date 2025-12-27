# creating a superclass of a superclasses so the common functionality is put into 1 class
# that gets derived to all other classes 
# andt then that gets derived to all other classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def drive(self) -> None:
        pass
    
    @abstractmethod
    def stop(self) -> None:
        pass


class TwoWheeler(Vehicle):
    @abstractmethod
    def typeOf2Wheeler(self, type: str) -> None:
        pass

class FourWheeler(Vehicle):
    @abstractmethod
    def soundSystem(self, type: str) -> None:
        pass


class TW1(TwoWheeler):
    def drive(self):
        print("Driving a two wheeler")
    
    def stop(self):
        print("Stopping a two wheeler")
    
    def typeOf2Wheeler(self, type):
        print(f"Type of tehe 2 Wheeler :{type}")

class FW1(FourWheeler):
    def drive(self):
        print("Driving a four wheeler")
    
    def stop(self):
        print("Stopping a four wheeler")
    
    def soundSystem(self, type):
        print(f"type of the sound system is : {type}")


jupiter = TW1()
activa = TW1()

honda = FW1()
ertiga = FW1()
# --------

jupiter.drive()
jupiter.typeOf2Wheeler('scooty')
jupiter.stop()

print("-"*20)

activa.drive()
activa.typeOf2Wheeler('bike')
activa.stop()

print("-"*20)

honda.drive()
honda.soundSystem('dolby')
honda.stop()

print("-"*20)


ertiga.drive()
ertiga.soundSystem('dolby2')
ertiga.stop()

print("-"*20)