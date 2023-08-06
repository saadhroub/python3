# insert the number of day
# 0 --> Mon, 1->Tue, 2->Wed, 3->Thu, 4-> Fri,
# 5->Sat, "We will go to the beach", 6->Sun

d = input("Enter the day number")
if d=='0':
    print("Mon")
elif d=='1':
    print("Tue")
elif d=='2':
    print("Wed")
elif d=='3':
    print("Thu")
elif d=='4':
    print("Fri")
elif d=='5':
    print("Sat")
elif d=='6':
    print("Sun")
else:
    print("Wrong Number")
    