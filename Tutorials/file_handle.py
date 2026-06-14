# f = open('mydata', 'r')

# f1 = open('abc', 'a')

# for data in f:
#     f1.write(data)

# print(f.readline(), end='')
# print(f.readline())


f = open('IMG_0122.HEIC','rb')
f1 = open('MyPic.jpg', 'wb')

for i in f:
    f1.write(i)