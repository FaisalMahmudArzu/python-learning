# from array import *
# # vals = array('i', [5,9,8,4,12])
# # newArr = array(vals.typecode, (a*a for a in vals))

# # for e in newArr:
# #     print(e)


# arr = array('i',[])
# n = int(input("Enter the length of the array :"))

# for i in range(n):
#     x = int(input("Enter the next value :"))
#     arr.append(x)
# print(arr)

# val = int(input("Enter the value you want to find index :"))

# for j in range(n):
#     if(arr[j]==val):
#         print("The index is :", j)
#         break
# else: 
#     print("Not found")
    

from numpy import *

# arr = array([1,2,3,4,5],float)
# print(arr.dtype)
# print(arr)

# arr = linspace(0,15) #last number here indicated how many parts will be divided the range in array. in default it will do 50 parts

# arr = arange(1,15,2) #last number is the gaps between numbers

# arr = logspace(1,40,5)
# print('%.2f' %arr[4])

# arr1 = array([1,2,4,5,6,7])
# arr2 = array([8,9,10,11,12,13,14])

# # print(max(arr1))
# print(concatenate([arr1,arr2]))


# arr1 = array([
#         [1,2,3,4],
#         [5,6,7,8]
#              ])
# print(arr1.ndim) #tells the dimension
# print(arr1.shape) #shows rows and columns
# arr2 = arr1.flatten() #we get 1 dimensional array from multi dimensional array 
# arr3 = arr2.reshape(2,2,3)

m1 = matrix('1 2 3 ;6 4 5 ;1 6 7') #makes a matrix
m2 = matrix('1 2 3 ;6 8 5 ;2 6 7') #makes a matrix
# print(diagonal(m)) #diagonal numbers only

m3 = m1 * m2
print(m3)
