print("welcome to the tip calculator")
bill = float(input("What was the total bill? \n"))
people = int(input("how many people to split the bill \n"))
tip = int(input("what percentage tip would you like to give? \n"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)

print(f"Each person should pay {final_amount}")