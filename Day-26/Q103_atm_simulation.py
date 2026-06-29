# Q103 - ATM simulation
balance = 10000
pin = "1234"
entered_pin = input("Enter PIN: ")
if entered_pin != pin:
    print("Invalid PIN!")
else:
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            print(f"Balance: Rs.{balance}")
        elif choice == '2':
            amt = int(input("Deposit amount: "))
            balance += amt
            print(f"Deposited Rs.{amt}. New balance: Rs.{balance}")
        elif choice == '3':
            amt = int(input("Withdraw amount: "))
            if amt > balance:
                print("Insufficient funds!")
            else:
                balance -= amt
                print(f"Withdrawn Rs.{amt}. New balance: Rs.{balance}")
        elif choice == '4':
            print("Thank you!")
            break