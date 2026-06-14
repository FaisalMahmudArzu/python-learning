
def topten():
    n = 1

    while n<=10:
        sq = n*n
        yield sq  #yield just works like return, but return stops the code and yield doesn't stops it
        
        n += 1


values = topten()

for i in values:
    print(i)