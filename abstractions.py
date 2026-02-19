#Hiding complex implementation detuals and showing only the necessary features of an object.
from abc import ABC, abstractmethod

class Vechical(ABC):
    @abstractmethod
    def start(self):
        pass

class bike(Vechical):
    def start(self):
        print("Bike is starting")


b = bike()
b.start()  # Output: Bike is starting
