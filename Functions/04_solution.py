import math
def area(r):
    return (math.pi*r*r)
def circumference(r):
    return (2*math.pi*r)
r = float(input("What is the radius? :"))

print(f"The area : {area(r):.2f}")
print(f"The circumference : {circumference(r):.2f}")