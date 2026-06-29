# Q7 - Find product of digits
def product_of_digits(n):
    result = 1
    for d in str(abs(n)):
        result *= int(d)
    return result

n = int(input("Enter number: "))
print(f"Product of digits = {product_of_digits(n)}")