import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to the PyPassword Generator!")

num_of_letters = int(input("How many Letters would you like in your password?"))
num_of_symbols = int(input("how many symbols would you like?"))
num_of_numbers = int(input("how many numbers would you like?"))

# Easy level
password_list = []

for char in range(0,num_of_letters):
    password_list.append(random.choice(letters))
    
for char in range(0,num_of_symbols):
    password_list.append(random.choice(symbols))

for char in range(0,num_of_numbers):
    password_list.append(random.choice(numbers))
    
    
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
    
print(f"your password is : {password}")
