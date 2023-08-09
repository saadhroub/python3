for i in range(0,50):
   rooms_diction = {"new room":
                  {"room_num":i+10, 
               "booking_counter": "0" ,
               "Type" :"singel",
                   "is_booked": False}
}

def num():
    print("Enter a room number from 10 to 59:  ")
    room_num = int(input())
    num_is_wrong = True
    while num_is_wrong == True:
      if room_num<10 or room_num>59:
        print("wrong , try again")
        room_num = int(input())
      else:
        num_is_wrong = False
    return room_num 


def reserve_room():
    room_num =num() 
    rooms_diction(["new room"]["room_num":i-10]["is_booked":True])
    print(rooms_diction["new room"]["room_num"])


    




    
menu = """Choose an option: 
          1.reserve a room
          2.change room type
          3.cancel the booking
          4.show all reserved rooms information
          5.show statistics
 """
 
print(menu)
option =int(input("Enter your option:  "))
for i in range(1,10):
  if option == 1:
    reserve_room()
 


