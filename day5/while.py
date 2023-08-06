# call functions based on numbers

def visit_turkey():
    print("We are visitng Antalya, Bursa, Tarabzoun")
    print("We offer 5 starts hotel")
    print("The cost is 600 USD per adult")
    print("we are flying every Thursday")


def visit_egypt():
    print("We are visitng Cairo, Alexandria, Oswan")
    print("We offer 4 and 5 start hotel")
    print("The cost is 400 USD per adult, but you can add 200USD to visih Sharm")
    print("we are flying twice aweek, Monday and Friday")


def flight_booking():
    print("We offer flight booking to Dubai, Maldiv, Thailand, USA")
    print("We offer you free cancellation")
    print("You have to book the flight 24 hours before your trip")


def checkout():
    print("Thanks for booking with us")
    bar_cost = mini_bar(3, 10, 5)
    nights = 7
    money = room_cost(nights, bar_cost)
    print("You have to pay", money,"USD")
    print("We wish to see you again soon")


def mini_bar(drink, water, chocho):
    drink_cost = drink*9
    water_cost = water*3
    chocho_Cost = chocho*5
    mini_bar_sum = drink_cost+water_cost+chocho_Cost
    return mini_bar_sum


def room_cost(nights, bar_cost):
    nights_costs = 50*nights
    tax = 5*nights
    discount = 8*nights
    total = nights_costs + tax + bar_cost - discount
    return total
menu = """
        Enter numbers 1 to 4,  or -1 to exit:
        1. Turkey visi Details
        2. Egypt visit Details
        3. Book Flights details
        4. Checkout
        -1 To exit from the program
"""



while True: 
    print(menu)
    choice = int(input())
    if choice==1:
        visit_turkey()
    elif choice==2:
        visit_egypt()
    elif choice ==3:
        flight_booking()
    elif choice ==4:
        checkout()
    elif choice ==-1:
        print("Thanks for using our program")
        break
    else:
        print("Sorry we do not have this service")
        
    