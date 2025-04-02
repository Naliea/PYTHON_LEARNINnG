# import random

# print("Welcome to the Pypassword Generator!")
# password_letters = ["a","b","c","d"]
# password_symbols = ["%","#","@","$"]
# password_numbers = ["1","2","3"]
# print(password_letters)
# password_user_letters = []
# user_letters = int(input("How many letters would you like in your password?"))

# for letters in password_letters:
#    while password_user_letters == range(0,user_letters+1):
#       password_u_letters = password_user_letters.append(letters)
#       random_password_u_letters = random.choice(password_u_letters)
# user_letters= int(input("How many letters would you like in your password?\n"))
# random_letters = random.randint(0,user_letters)
# random_user_letters= password_letters[random_letters]
# print(random_user_letters)
# user_symbols = int(input("How many symbols would you like?\n"))
# random_symbols = [random.choice(password_symbols[0,user_symbols])]
# print(random_symbols)
# user_numbers = int(input("How many numbers would you like?\n"))
# random_numbers = random.choice(password_numbers[user_numbers])
# print(random_numbers)
# password_makers = [random_user_letters,random_symbols, random_numbers]
# print(password_makers)
# print(f"Your password is: {random.choice(password_makers)}")


#    #Implementation of a for loop
# fruits = ["Apple", "Pear", "Orange", "Peach", "Cherry"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# #Sum_score 
# student_score = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
# list_add = student_score[0] + student_score[1] + student_score[2] + student_score[3] + student_score[4] + student_score[5] + student_score[6] + student_score[7] + student_score[8] + student_score[9] + student_score[10] + student_score[11] + student_score[12] + student_score[13] + student_score[14]
# print(list_add)
# list_add = sum(student_score)
# print(list_add)
# sum = 0
# #Understanding sum() behind the scenes using for loop
# for score in student_score:
#    sum += score
# print(sum)
# #Understanding max() behind the scenes using for loop
# max_score = max(student_score)
# print(max_score)
# highest_score = 0
# for score in student_score:
#     if score>highest_score:
#      highest_score = score
# print(highest_score)
# #Understanding min() behind the scenes using for loop
# student_score = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
# lowest_score = student_score[0]
# for score in student_score:
#     if not score > lowest_score:
#         lowest_score = score
# print(lowest_score)

# student_score = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

# # Initialize lowest_score to a very high value
# lowest_score = float('inf')

# for score in student_score:
#     if score < lowest_score:
#         lowest_score = score

# print(lowest_score)  # Output: 24
# # Carl Gauss challenge of calc no.s from 1 to 100
# sum = 0
# for number in  range(1,101):
#     sum += number
# print(sum)
# # all_numbers_from_1_to_10 = []
# # for number in range(1,10):
# #    answer = all_numbers_from_1_to_10[number] # Output:number) # Output:
# #    print(answer)

# #FizzBuzz
# for number in range(1,101):
#    if  number % 3 == 0 and number % 5 == 0:
#       print("FizzBuzz")
#    elif number % 3 == 0:
#       print("Fizz")
#    elif number % 5 == 0:
#       print("Buzz")
#    else:
#       print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_u_letters = []
for i in range(0,nr_letters):
    random_letter = random.choice(letters)
    password_u_letters.append(random_letter)
print(password_u_letters)
for i in range(0,nr_symbols):
    random_symbols = random.choice(symbols)
    password_u_letters.append(random_symbols)
print(password_u_letters)
for i in range(0,nr_numbers):
    random_numbers = random.choice(numbers)
    password_u_letters.append(random_numbers)
print(password_u_letters)
if len(password_u_letters) < 12:
    print("Short passwords are not allowed")

random.shuffle(password_u_letters)
# password = "".join(password_u_letters)
#Password functionality
password = ""
for i in password_u_letters:
    password += i
print(f"Your password is:{password}")