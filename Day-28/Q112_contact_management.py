# Q112 - Contact management system
contacts = {}
while True:
    print("\n1. Add Contact\n2. View All\n3. Search\n4. Delete\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact added!")
    elif choice == '2':
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == '3':
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))
    elif choice == '4':
        name = input("Delete name: ")
        contacts.pop(name, None)
        print("Deleted!")
    elif choice == '5':
        break