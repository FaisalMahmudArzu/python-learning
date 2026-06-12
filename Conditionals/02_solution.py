age = int(input("Enter the age :"))
day = int(input("Press 1 if it is wednesday and 0 if not:"))
ticket_price = 0

if age>=18 and day==1:
    ticket_price = 10
elif age>=18 and day!=1:
    ticket_price = 12
elif age<=18 and day!=1:
    ticket_price = 6
elif age<=18 and day==1:
    ticket_price = 8

print("Your ticket price is $",ticket_price)