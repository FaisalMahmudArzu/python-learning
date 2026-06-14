a = 5
b = 3

try: 
    print("resource opened")
    print(a/b)
    k = int(input("Enter a number :"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, You cannot divide a number by Zero.", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went wrong")

finally:
    print("resource closed")