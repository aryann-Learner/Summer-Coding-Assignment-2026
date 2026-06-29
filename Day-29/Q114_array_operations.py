# Q114 - Menu-driven array operations system
arr = []
while True:
    print("\n1. Input Array\n2. Display\n3. Sum & Average\n4. Sort\n5. Reverse\n6. Exit")
    choice = input("Choose: ")
    if choice == '1':
        arr = list(map(int, input("Enter elements: ").split()))
    elif choice == '2':
        print("Array:", arr)
    elif choice == '3':
        print(f"Sum = {sum(arr)}, Average = {sum(arr)/len(arr):.2f}")
    elif choice == '4':
        print("Sorted:", sorted(arr))
    elif choice == '5':
        print("Reversed:", arr[::-1])
    elif choice == '6':
        break