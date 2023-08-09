rooms = [
    {
        "number": 1,
        "type": "Single",
        "is_booked": False,
        "booking_counter": 0,
    },
    {
        "number": 2,
        "type": "Double",
        "is_booked": False,
        "booking_counter": 0,
    },
    {
        "number": 50,
        "type": "King",
        "is_booked": False,
        "booking_counter": 0,
    },
]


def menu():
    print("Please select an option (1-5):")
    print("1. Reserve an available room.")
    print("2. Change room type.")
    print("3. Cancel the booking.")
    print("4. Show all reserved rooms information.")
    print("5. Show statistics.")
    print("-1. Exit.")
    option = int(input("Option: "))
    return option

   
def room_no():
    room_number = int(input("Please enter a room number (1-50): "))
    if room_number > 50 or room_number < 1:
        print("Invalid room number.")
        menu()
    if rooms[room_number - 1]["is_booked"]:
        print("Room is already booked.")
        menu()
    else:
        return room_number 
    
    
def reserve():
    room_number = room_no()
    rooms[room_number - 1]["is_booked"] = True
    print("Room number {} has been reserved.".format(room_number))


def change_type():
    room_number = room_no()
    new_type = input("Please enter a new room type (Single, Double, Deluxe, or King): ")
    if new_type not in ["Single", "Double", "Deluxe", "King"]:
        print("Invalid room type.")
        menu()
    rooms[room_number - 1]["type"] = new_type
    print("Room type has been changed.")

    
def cancel():
    room_number = room_no()
    rooms[room_number - 1]["is_booked"] = False
    print("Booking has been cancelled.")


def reservations():
    print("Room number | Type | Booking counter")
    for room in rooms:
        if room["is_booked"]:
            print("{} | {} | {}".format(room["number"], room["type"], room["booking_counter"]))


def statistics():
    print("Number of booked rooms: {}.".format(len([room for room in rooms if room["is_booked"]])))
    print("Number of available rooms: {}.".format(len([room for room in rooms if not room["is_booked"]])))


while True:
    option = menu()
    if option == -1:
        break
    if option == 1:
        reserve()
    elif option == 2:
        change_type()
    elif option == 3:
        cancel()
    elif option == 4:
        reservations()
    elif option == 5:
        statistics()
    else:
        continue