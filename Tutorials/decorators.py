# def div(a,b):
#     print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#             return func(a,b)
#     return inner

# div = smart_div(div)


# div(2,4)

# from calc import *

# x = add(2,5)
# print(x)


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper 

@timer
def example_function(n):
    time.sleep(n)

example_function(2)