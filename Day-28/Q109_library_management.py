# Q109 - Library management system
books = []
while True:
    print("\n1. Add Book\n2. Display Books\n3. Search Book\n4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        title = input("Book title: ")
        author = input("Author: ")
        books.append({"title": title, "author": author})
        print("Book added!")
    elif choice == '2':
        for b in books:
            print(f"Title: {b['title']}, Author: {b['author']}")
    elif choice == '3':
        key = input("Search by title: ").lower()
        found = [b for b in books if key in b['title'].lower()]
        print(found if found else "Not found")
    elif choice == '4':
        break