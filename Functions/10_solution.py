
# def factorial(num):
#     fact = 1
#     for i in range(num,1,-1):
#         fact *= i
#     return fact

# facto = factorial(5)
# print(facto)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))