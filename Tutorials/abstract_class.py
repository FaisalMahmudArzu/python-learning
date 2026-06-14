from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("It's Running")
class programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

com1 = Laptop()
# com1.process()

# com = Computer()
# com.process()

prog1 = programmer()
prog1.work(com1)