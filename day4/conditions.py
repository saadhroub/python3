sunny = True
passport = True
money = int(input("Enter the money: "))

if sunny and passport:
    if money>=5000:
        print("We will go Maldiv")
    elif money>=2000:
        print("We will go Antalya")
    else:
        print("We will go Aqaba")
else:
    print("Home Sweet Home")

        