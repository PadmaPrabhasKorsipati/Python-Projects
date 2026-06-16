
principle=0

time=0

rate=0

"""time=int(input("Enter the duration of loan:"))

rate=int(input("Enter the rate of interest:"))"""


while principle<=0:

    priniciple=int(input("Enter th principle amount:"))
    if principle <=0:
      print("Principle amount could not be zero.")

   
while rate<=0:
   
   rate=int(input("Entyer the rate of interest:"))
   if rate<=0:
      print("Rate could not be zero.")


while time<=0:
   time=int(input("Enter the duration of loan:"))

   if time<=0:
      print("Time could not be zero.")
   


Total=principle*pow(1+(rate/12),12*time)

print(f"The Total Compound interest is:{Total}")