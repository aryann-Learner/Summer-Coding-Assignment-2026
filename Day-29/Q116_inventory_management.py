# Q116 - Inventory management system
inventory = {}
while True:
    print("\n1. Add Item\n2. Update Stock\n3. View Inventory\n4. Search Item\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        item = input("Item name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        inventory[item] = {"qty": qty, "price": price}
        print("Item added!")
    elif choice == '2':
        item = input("Item name: ")
        if item in inventory:
            qty = int(input("New quantity: "))
            inventory[item]["qty"] = qty
            print("Updated!")
    elif choice == '3':
        for item, info in inventory.items():
            print(f"{item}: Qty={info['qty']}, Price=Rs.{info['price']}")
    elif choice == '4':
        item = input("Search: ")
        print(inventory.get(item, "Not found"))
    elif choice == '5':
        break