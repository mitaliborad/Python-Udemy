print("Welcome to RollerCoaster")
height = int(input("Please Enter Your height in cm : "))

if height >= 120:
    print("You can ride RollerCoaster.")
    bill = 0 

    age = int(input("Enter your age : "))
    if age <=12 :
        bill = 5
        print("child tickets are $5.")
    elif age<=18:
        bill = 7
        print("youth tickets are $7.")
    elif age>= 45 and age <= 55:
        print("Everything will be okay. Have a free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")
     
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")   
    if wants_photo == "y" :
        bill += 3
    
    print(f"your final bill is ${bill}")
   
        
else : 
    print("Sorry! You have to grow taller before you can ride.")