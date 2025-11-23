menu={
    "pasta":50,
      "salad": 60,
      "sandwich":50,
      "pizza":80,
      "coffe":60,
      }

print("welcome to sharma Restro")
print("pasta: Rs50\nsalad: Rs60\nsandwich: Rs50\npizza: Rs80\ncoffe: Rs60")
order_total=0

item_1=input("enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item{item_1} is added to your order")
else:
    print("ordered item {item_1} is not available yet")
another_order=input("do want to add another item ? (yes/no)")
if another_order=="yes":
    item_2=input("enter another item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(" item {item_2} has been added to order")
    else:
        print("ordered item {item_2} is not available!")
print( f"the total number of items to be pay is {order_total}") 