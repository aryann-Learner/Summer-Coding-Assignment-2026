# Q105 - Student record management system
students = []
while True:
    print("\n1. Add Student\n2. Display All\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Name: ")
        roll = input("Roll No: ")
        marks = float(input("Marks: "))
        students.append({"name": name, "roll": roll, "marks": marks})
        print("Student added!")
    elif choice == '2':
        if not students:
            print("No records found.")
        for s in students:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
    elif choice == '3':
        break