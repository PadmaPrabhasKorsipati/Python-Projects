operator = input("Enter an Operator (+ or - or * or /):")

num1=int(input("Enter the First Number:"))
num2=int(input("Enter the second Number:"))

if operator == "+":
    result=num1+num2

elif operator == "-":
    result=num1-num2

elif operator == "*":
    result=num1*num2

elif operator ==  "/":
    if num2!=0:
        result=num1/num2
    elif num1>num2:
        result=float(num1/num2)
    else:
        result="Undefined"
        

else:
    result="Invalid operator"


print(f"{num1} + {operator} + {num2} = {result}")