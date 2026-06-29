# Q115 - Menu-driven string operations system
s = ""
while True:
    print("\n1. Input String\n2. Reverse\n3. Uppercase\n4. Count Words\n5. Check Palindrome\n6. Exit")
    choice = input("Choose: ")
    if choice == '1':
        s = input("Enter string: ")
    elif choice == '2':
        print("Reversed:", s[::-1])
    elif choice == '3':
        print("Uppercase:", s.upper())
    elif choice == '4':
        print("Word count:", len(s.split()))
    elif choice == '5':
        print("Palindrome" if s == s[::-1] else "Not Palindrome")
    elif choice == '6':
        break