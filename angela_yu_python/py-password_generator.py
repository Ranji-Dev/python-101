#password Generator Project
import random
letter =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
         't','u','v','w','x','y','y','z','A','B','C','D','E','F','G','H','I','J','K',
         'L','M','N','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to the password generator !!")
np_letter = int(input("How many letters would you like in your password \n"))
np_number = int(input("How many numbers would you like in your password \n"))
np_symbol = int(input("How many symbols would you like in your password \n"))

#easy level of password generator

# password =""
# for char in range(1, np_letter+1):
#      password += random.choice(letter)
#
# for num in range(1, np_number+1):
#      password += random.choice(number)
#
# for sym in range(1, np_symbol+1):
#      password += random.choice(symbol)
# print(password)

#hard level of password generator
password_list =[]
for char in range(1, np_letter+1):
     password_list.append(random.choice(letter))

for num in range(1, np_number+1):
     password_list.append(random.choice(number))

for sym in range(1, np_symbol+1):
     password_list.append(random.choice(symbol))
#print(password_list)
random.shuffle(password_list)
#print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")