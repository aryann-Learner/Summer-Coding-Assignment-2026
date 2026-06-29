# Q111 - Ticket booking system
seats = {str(i): "Available" for i in range(1, 11)}
while True:
    print("\n1. View Seats\n2. Book Seat\n3. Cancel Booking\n4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        for seat, status in seats.items():
            print(f"Seat {seat}: {status}")
    elif choice == '2':
        seat = input("Enter seat number (1-10): ")
        if seats.get(seat) == "Available":
            name = input("Your name: ")
            seats[seat] = f"Booked by {name}"
            print("Booking confirmed!")
        else:
            print("Seat not available!")
    elif choice == '3':
        seat = input("Enter seat number: ")
        if seat in seats:
            seats[seat] = "Available"
            print("Booking cancelled!")
    elif choice == '4':
        break