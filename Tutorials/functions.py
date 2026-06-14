# def add_sub(x,y):
#     c = x + y
#     d = x - y
#     return c,d

# result1, result2 = add_sub(5,3)
# print(result1)
# print(result2)


# def update(x):
#     print(id(x))
#     x = 8
#     print(id(x))
#     print(x)
    
# a = 10
# print(id(a))
# update(a)
# print("a ",a)


# def person(*b):    # *b means all values in a tuple except a
#     c = 0
#     for i in b:
#         c = c+i
#     print(c)
    

# person(5,6,7,3)


# def person(name, **data):    # **b means values with different argument will be passed
#     print(name)
#     for i,j in data.items():
#         print(i,j)
    

# person('Faisal',age=28 ,city='Dhaka' ,mob= 9187434319)



# a = 10
# def something():
#     global a #it says to use the global variable a outside the function
#     a = 15
#     print("something in fun", a)
# something()
# print(a)

# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if (i % 2 == 0):
#             even = even + 1
#         else:
#             odd = odd + 1

#     return even, odd

# lst = [20,25,14,19,16,24,28,47,26]

# even, odd = count(lst)
# print("Even : {} and Odd : {}".format(even, odd))



n = int(input("Enter the number of iteration "))
def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Invalid Entry")

    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
                c = a + b
                b = c
                a = b
                print(c) 
            
fib(n)