
menu={
    "Pizza":200,
    "Nachos":160,
    "Popcorn":100,
    "Fries":70,
    "Chips":60,
    "Pretzel":150,
    "Soda":50,
    "Lemonade":70
}

cart=[]
total=0


print("---------MENU ---------")
for key,value in menu.items():
    print(f"{key:10}:₹{value:.2f}")

print("------------------------")


while True:
    food=input("Select an item (q to quit):").capitalize()
    
    if food=='q':
        break

    elif menu.get(food) is not None:
        cart.append(food)


print("---------YOUR CART------")  
      
for food in cart:

    total+=menu.get(food)

    print(food,end=" ")

    
print()

print(f"The total Price of the items in the cart is:₹{total}")

