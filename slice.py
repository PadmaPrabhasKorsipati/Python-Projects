
email = input("Enter your Email:")

index=email.index("@")

username=email[:index]
domain=email[index:]


print(f"The Username is:{username}")

print(f"The Domain name is {domain}")

