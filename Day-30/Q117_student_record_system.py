# Q117 - Student record system using arrays and strings
students = []
while True:
    print("\n1. Add\n2. Display\n3. Search by Name\n4. Find Topper\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Name: ")
        roll = input("Roll: ")
        marks = list(map(float, input("Marks (5 subjects): ").split()))
        students.append({"name": name, "roll": roll, "marks": marks, "total": sum(marks)})
    elif choice == '2':
        for s in students:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Total: {s['total']}")
    elif choice == '3':
        name = input("Search name: ").lower()
        found = [s for s in students if name in s['name'].lower()]
        for s in found:
            print(s)
    elif choice == '4':
        if students:
            topper = max(students, key=lambda x: x['total'])
            print(f"Topper: {topper['name']} with {topper['total']} marks")
    elif choice == '5':
        break