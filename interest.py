
priniciple=int(input("Enter th principle amount:"))

time=int(input("Enter the duration of loan:"))

rate=int(input("Enter the rate of interest:"))


while priniciple<=0:
    print("Principle amount could not be zero.")

    priniciple=int(input("Enter th principle amount:"))