hottile_diction_rooms={
    "stars":5,
    "swimming_pool": True,
    "free_wifi": True
}

rooms = []

for i in range (0,30):
    room2 = {
    "room_id": i+10,
    "booking_counter": 0,
    "is_booked": False,
    "type":"Single"
    }
    rooms.append(room2)


def room_num():
    print("PUT room number from 0 to 30")
    room_num = int(input())
    num_is_wrong = True
    while num_is_wrong==True:
        if room_num<1 or room_num>30:
            print("Wrong  number, try again")
            room_num = int(input())
        else:
            num_is_wrong = False
    return room_num


def reserve_room():
    room_num = room_num()
    rooms[room_num-10]["is_booked"] = True
    rooms[room_num-10]["booking_counter"] +=1
    print(rooms[room_num-10])


def cancel_booking():
    room_num = room_num()
    rooms[room_num-10]["is_booked"] = False
    rooms[room_num-10]["booking_counter"] -=1
    print(rooms[room_num-10])


def change_room_type():
    room_num = room_num()
    rooms[room_num-10]["type"] = "Double"
    print(rooms[room_num-10])


def show_all_reservation():
    print("info")
    

def show_status():
    total_booking  = 1
    singles = 2
    doubles = 3
    empty =4    
    for room in rooms:
        total_booking += room["booking_counter"]
        if room["type"] == "Single":
            singles += 1
        else: 
            doubles += 1
        if room["is_booked"] == False:
            empty += 1
    print("all Booking:", total_booking)
    print("all Single:", singles)
    print("all Double:", doubles)
    print("all Available:", empty)


def menu():
    print("Insert number from 1 to 5 or -1 to exit")
    print("1. To reserve room")
    print("2. To change room type")
    print("3. To cancel booking")
    print("4. print all reserved rooms info")
    print("5. Show status about the hotel")


menu()    
num = int(input())
while (num != -1):
    if num == 1:
        reserve_room()   
    elif num == 2:
        change_room_type() 
    elif num == 3:
        cancel_booking()  
    elif num == 4:
        show_all_reservation() 
    elif num == 5:
        show_status()
    else:
        print("Wrong , try again")
    menu()
    num = int(input())