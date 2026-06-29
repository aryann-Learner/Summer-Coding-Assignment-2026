# Q107 - Salary management system
name = input("Employee name: ")
basic = float(input("Basic salary: "))
hra = 0.2 * basic
da = 0.1 * basic
tax = 0.1 * basic
net = basic + hra + da - tax
print(f"\nSalary Slip for {name}")
print(f"Basic: Rs.{basic}, HRA: Rs.{hra}, DA: Rs.{da}, Tax: Rs.{tax}")
print(f"Net Salary: Rs.{net}")