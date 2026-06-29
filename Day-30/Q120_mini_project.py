# Q120 - Complete mini project using arrays, strings and functions
def add_student(students):
    name = input("Name: ")
    roll = input("Roll No: ")
    marks = list(map(float, input("Enter marks for 5 subjects: ").split()))
    total = sum(marks)
    percentage = total / 5
    grade = 'A+' if percentage >= 90 else 'A' if percentage >= 80 else 'B' if percentage >= 60 else 'C' if percentage >= 40 else 'F'
    students.append({"roll": roll, "name": name, "marks": marks, "total": total, "percentage": percentage, "grade": grade})
    print(f"Student {name} added with Grade {grade}")

def display_all(students):
    if not students:
        print("No records!")
        return
    print(f"\n{'Roll':<10} {'Name':<20} {'Total':<10} {'%':<10} {'Grade'}")
    for s in students:
        print(f"{s['roll']:<10} {s['name']:<20} {s['total']:<10} {s['percentage']:.1f}%     {s['grade']}")

def find_topper(students):
    if students:
        topper = max(students, key=lambda x: x['total'])
        print(f"Topper: {topper['name']}, Total: {topper['total']}, Grade: {topper['grade']}")

def class_average(students):
    if students:
        avg = sum(s['percentage'] for s in students) / len(students)
        print(f"Class Average: {avg:.2f}%")

students = []
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student\n2. Display All\n3. Find Topper\n4. Class Average\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_all(students)
    elif choice == '3':
        find_topper(students)
    elif choice == '4':
        class_average(students)
    elif choice == '5':
        print("Goodbye!")
        break