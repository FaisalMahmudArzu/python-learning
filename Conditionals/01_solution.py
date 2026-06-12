age = int(input("Provide me an age : "))

if age<13:
    print("Child")
elif 13<=age and age<=19:
    print("Teenager")
elif 20<=age and age<=59:
    print("Adult")
elif 60<=age:
    print("Senior")