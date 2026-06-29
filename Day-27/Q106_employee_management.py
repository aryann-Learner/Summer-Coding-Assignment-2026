# Q106 - Employee management system
employees = []
while True:
    print("\n1. Add Employee\n2. Display All\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Name: ")
        emp_id = input("Employee ID: ")
        dept = input("Department: ")
        employees.append({"name": name, "id": emp_id, "dept": dept})
        print("Employee added!")
    elif choice == '2':
        for e in employees:
            print(f"ID: {e['id']}, Name: {e['name']}, Dept: {e['dept']}")
    elif choice == '3':
        break