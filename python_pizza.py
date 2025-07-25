print("Welcome to Python Pizza Deliveries!")
size = input("what size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 120
      
elif size == "M":
    bill += 250
    
elif size == "L":
    bill += 400
    
else:
    print("you typed wrong input")

# add on pepperoni    
if pepperoni == "Y":
    if size == "S":
        bill += 20
    else:
        bill += 30

# add on extra cheese    
if extra_cheese == "Y":
    bill += 40
    

print(f"Your final bill is: ${bill}")
    