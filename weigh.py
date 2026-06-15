#python weight calculator 



weight=int(input("Enter your Weight:"))

unit=input("Kilogram or pounds?(K or L):")

if unit =='K':
    weight*=2.205
    unit="Kgs."
    print(f"Your Weight is: {round(weight,1)} {unit}")

elif unit =="L":
    weight/=2.205
    unit="Lbs"
    print(f"Your Weight is: {round(weight,1)} {unit}")

else:
    print(f"{unit} is not valid. ")


    
