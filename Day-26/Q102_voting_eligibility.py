# Q102 - Voting eligibility system
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"{name} is eligible to vote.")
else:
    print(f"{name} is not eligible to vote. {18 - age} years remaining.")