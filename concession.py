
menu={
    "Pizza":200,
    "nachos":160,
    "Popcorn":100,
    "Fries":70,
    "Chips":60,
    "pretzel":150,
    "soda":50,
    "Lemonade":70
}

cart=[]
total=0


print("---------MENU ---------")
for key,value in menu.items():
    print(f"{key:10}:₹{value:.2f}")

print("------------------------")