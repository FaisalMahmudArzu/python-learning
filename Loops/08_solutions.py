num = int(input("Enter number to check prime or not :"))
is_prime = True

if num>1:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
if is_prime == True:
    print("It is a prime number")
else:
    print("not a prime number")