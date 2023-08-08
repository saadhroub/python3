# Menu Code:
# نطلب من المستخدم أن يدخل رقم بين 1 و 5 وحسب الرقم نكمل معه
# إذا رغب المستخدم في إغلاق القائمة يدخل رقم -1
# ! تعني لأ


hotel = (
            "hotl_name": "Saad Hroub",
            "total_rooms": 50,
            "stars": 5,
            "have_swimming_pool": True
)

rooms = []

for i in range (0,50):
    new_room ={
    "room_no": i+10,
    "booking_counter": 0,
    "is_booked": False,
    "type":"Single"
    }
    rooms.append(new_room)

def get_num():
    print("insert room number from 10 to 59")
    room_num = int(input())
    num_is_wrong = True
    while num_is_wrong==True:
        if room_num<10 or room_num>59:
            print("Wrong Room number, try again")
            room_num = int(input())
        else:
            num_is_wrong = False
    return room_num

def reserve_room():
    room_num = get_num()
    rooms[room_num-10]["is_booked"] = True
    rooms[room_num-10]["booking_counter"] +=1
    print(rooms[room_num-10])
  
        
def cancel_booking():
    room_num = get_num()
    rooms[room_num-10]["is_booked"] = False
    rooms[room_num-10]["booking_counter"] -=1
    print(rooms[room_num-10])


def change_room_type():
    room_num = get_num()
    rooms[room_num-10]["type"] = "Double"
    print(rooms[room_num-10])


def show_all_reservation():
    print("Details")

    
def show_statistics():
    total_booking  = 0
    singles = 0
    doubles = 0
    available = 0    
    for room in rooms:
        total_booking += room["booking_counter"]
        if room["type"] == "Single":
            singles += 1
        else: 
            doubles += 1
        
        if room["is_booked"] == False:
            available += 1
    print("Total Booking:", total_booking)
    print("Total Single:", singles)
    print("Total Double:", doubles)
    print("Total Available:", available)



def menu():
    print("Insert number from 1 to 5 or -1 to exit")
    print("1. To reserve room")
    print("2. To change room type")
    print("3. To cancel reservation")
    print("4. print all reserved rooms details")
    print("5. Show statistics about the hotel")



menu()    
num = int(input())
while (num != -1):
    if num == 1:
        reserve_room()   # حجز غرفة
    elif num == 2:
        change_room_type()  # تغيير نوع الغرفة
    elif num == 3:
        cancel_booking() # إلغاء الحجز للغرفة
    elif num == 4:
        show_all_reservation() # عرض الغرف المحجوزة
    elif num == 5:
        show_statistics() # عرض احصائيات
    else:
        print("Wrong number, try again")
    menu() # عرض القائمة مرة أخرى
    num = int(input())

        

 

