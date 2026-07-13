from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light bulb on")

class Switch:
    def __init__(self, device: Switchable):  # Depends on abstraction
        self.device = device
        
    def operate(self):
        self.device.turn_on()
