# Q23 - Count set bits in a number
def count_set_bits(n):
    return bin(n).count('1')

n = int(input("Enter number: "))
print(f"Set bits = {count_set_bits(n)}")