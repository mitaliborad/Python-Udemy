print("Welcome to RollerCoaster")
height = int(input("Please Enter Your height in cm : "))

if height >= 120:
    print("You can ride RollerCoaster.")

    age = int(input("Enter your age : "))
    if age <= 18:
        print("You have to pay only $7 for ticket.")
    else:
        print("Your ticket is $12.")
else : 
    print("Sorry! You have to grow taller before you can ride.")