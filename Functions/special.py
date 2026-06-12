# username = "Chaiaurcode"

# def func():
#     # username = "chai"
#     print(username)

# print(username)
# func()

def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))