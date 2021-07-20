import showstatus  # importing the matrix to showseats
import select    # module for seat selection
import payment_mail   # module for payment and email
import builtins  # module to globalize variables across modules

print("Welcome to Egale Airline, Lets get started with booking your seat")
date1 = str(input("Enter date for flight: "))
locationto1 = str(input("Where do you want to fly? "))
locationfrom1 = str(input("Where will you board the plane? "))
global seatsn
seatsn1 = 0
board = [[0.0, 1.0, 2.0],[0.1, 1.1, 2.1],[0.2, 1.2, 2.2],[0.3, 1.3, 2.3]]
while  True:
    showstatus.showstatus(board)
    select.select1(board)
    seatsn1 += 1
    ans2 = input("would you Like to Book Another Seat? " )
    if ans2 == "no" :
        break
    if ans2 == "yes" :
        continue
builtins.seatsn = seatsn1  # making variables accessible across modules
builtins.date = date1
builtins.location = locationfrom1 + "→" + locationto1


showstatus.showstatus(board)
payment_mail.payment(board)
