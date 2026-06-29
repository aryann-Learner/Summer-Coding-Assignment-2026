# Q118 - Mini library system
library = []
while True:
    print("\n1. Add Book\n2. Issue Book\n3. Return Book\n4. Display\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        title = input("Title: ")
        library.append({"title": title, "status": "Available"})
    elif choice == '2':
        title = input("Book title to issue: ")
        for book in library:
            if book["title"].lower() == title.lower() and book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued!")
                break
        else:
            print("Not available!")
    elif choice == '3':
        title = input("Book title to return: ")
        for book in library:
            if book["title"].lower() == title.lower():
                book["status"] = "Available"
                print("Book returned!")
                break
    elif choice == '4':
        for book in library:
            print(f"Title: {book['title']}, Status: {book['status']}")
    elif choice == '5':
        break