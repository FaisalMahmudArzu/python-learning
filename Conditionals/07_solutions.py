order_size = int(input("Press 1 for small, 2 for medium, 3 for large :"))
extra_shot = int(input("If you want extra shot press 1, 0 if don't want :"))
coffee = ""

if order_size ==1:
    coffee = "Small"
    if extra_shot ==1:
        coffee = "Small with extra shot"
elif order_size == 2:
    coffee = "Medium"
    if extra_shot ==1:
        coffee = "Medium with extra shot"
elif order_size == 3:
    coffee = "Large"
    if extra_shot ==1:
        coffee = "Large with extra shot"

print("Order is :",coffee)