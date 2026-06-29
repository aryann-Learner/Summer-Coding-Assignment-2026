# Q21 - Convert decimal to binary
def decimal_to_binary(n):
    return bin(n)[2:]

n = int(input("Enter decimal number: "))
print(f"Binary = {decimal_to_binary(n)}")