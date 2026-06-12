n = int(input("how many even numbers sum needed? :"))
sum = 0

for i in range(1, n+1):
    if i%2==0:
        sum += i
    else:
        pass
print(sum)