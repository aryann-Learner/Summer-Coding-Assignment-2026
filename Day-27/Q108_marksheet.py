# Q108 - Marksheet generation system
name = input("Student name: ")
subjects = ["Maths", "Science", "English", "Hindi", "CS"]
marks = [float(input(f"{sub} marks (out of 100): ")) for sub in subjects]
total = sum(marks)
percentage = total / len(subjects)
grade = 'A' if percentage >= 80 else 'B' if percentage >= 60 else 'C' if percentage >= 40 else 'F'
print(f"\nMarksheet for {name}")
print(f"Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")