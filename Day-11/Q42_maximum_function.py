# Q42 - Function to find maximum
def maximum(a, b):
    return a if a > b else b

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"Maximum = {maximum(a, b)}")