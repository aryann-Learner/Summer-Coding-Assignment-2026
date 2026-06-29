# Q113 - Menu-driven calculator
while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Choose: ")
    if choice == '5':
        break
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    if choice == '1':
        print(f"Result = {a + b}")
    elif choice == '2':
        print(f"Result = {a - b}")
    elif choice == '3':
        print(f"Result = {a * b}")
    elif choice == '4':
        print(f"Result = {a / b}" if b != 0 else "Cannot divide by zero!")