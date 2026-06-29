# Q119 - Mini employee management system
employees = []
while True:
    print("\n1. Add Employee\n2. Display All\n3. Search by ID\n4. Total Salary\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        emp_id = input("ID: ")
        name = input("Name: ")
        salary = float(input("Salary: "))
        employees.append({"id": emp_id, "name": name, "salary": salary})
    elif choice == '2':
        for e in employees:
            print(f"ID: {e['id']}, Name: {e['name']}, Salary: Rs.{e['salary']}")
    elif choice == '3':
        emp_id = input("Search ID: ")
        found = [e for e in employees if e['id'] == emp_id]
        print(found if found else "Not found")
    elif choice == '4':
        print(f"Total Salary = Rs.{sum(e['salary'] for e in employees)}")
    elif choice == '5':
        break