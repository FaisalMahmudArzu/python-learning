
# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram

#     def config(self):
#         print("Config is :", self.cpu, self.ram)

# com1 = Computer('i5', 16)
# com2 = Computer('Ryzen 7', 8)

# com1.config()
# com2.config()
        


class Computer:
    def __init__(self):
        self.name = "Faisal"
        self.age = 28

    def compare(self,other):
        if self.age == other.age:
            return True
        else: 
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)

print(c2.name)