# Q110 - Bank account system
accounts = {}
while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        acc = input("Account number: ")
        accounts[acc] = 0
        print("Account created!")
    elif choice == '2':
        acc = input("Account number: ")
        if acc in accounts:
            amt = float(input("Amount: "))
            accounts[acc] += amt
            print(f"Deposited. Balance: Rs.{accounts[acc]}")
    elif choice == '3':
        acc = input("Account number: ")
        if acc in accounts:
            amt = float(input("Amount: "))
            if amt <= accounts[acc]:
                accounts[acc] -= amt
                print(f"Withdrawn. Balance: Rs.{accounts[acc]}")
            else:
                print("Insufficient balance!")
    elif choice == '4':
        acc = input("Account number: ")
        print(f"Balance: Rs.{accounts.get(acc, 'Account not found')}")
    elif choice == '5':
        break