year = int(input("Enter the year to check leap year or not:"))

if (year>0):
    if ((year%4)==0 and (year%100)!=0) or (year%400)==0 :
        print("A leap year!") 
    else:
        print("not a leap year")