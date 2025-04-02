print("Welcome to Treasure Island")
print("Our mission is to find the treasure")
user_choice1 = input('You are at a crossroad where do you want to go?\n Type "left" or "right" ')
choice_1 = 'red'
choice_2 = 'blue'
choice_3 = 'yellow'
if user_choice1 == "left":
    user_choice2 = input("You've come to a lake.There is an island in the middle of the lake\n Type 'wait' to wait for the boat.Type 'swim' to swim accross")
    if user_choice2 == "wait" :
        user_choice3 = input ("You arrive at the island unharmed. There is a house with 3 doors.\n One red,one yellow and one blue. Which one do you choose?")
        if user_choice3 == choice_1:
            print("There is fire!!Game over")
        elif user_choice3 == choice_2:
            print("There is water!!Game over")
        elif user_choice3 == choice_3:
            print("There is where the treasure is...yaaay you win!!")
        else:
            print("Invalid choice.Try again!")
    else: 
        print("You are bitten by a crocodile.Game over!")
else:
    print("Game over")

print("Welcome to the rollercoaster")
user_height = input("What is your height?")
bill = 0
if user_height > 120:
    print("Yaay congratulations you can ride")
    age = input("What is your age?" )
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif 45  <=age <=55 :
        print("Congrats  you can ride freely!!")
    else:
        bill = 12
        print("Adults tickets are $12")
    
    user_pictures = input("Do you want to take pictures.Type Yes or No")
    if user_pictures == "Yes" :
        print("Add $3")
        bill += 3
    
    print (f"The total bill is $ {bill}")
else:
    print("Sorry! You can't ride")

# Checking if a number is even
number_to_check = input("Enter a number")
if number_to_check % 2 == 0:
    print("That's an even number")
else:
    print("That's an odd number")

#Pizza order practice 
print("Welcome to python deliveries!")
size = input("What Size of pizza do you want ? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese ? Y or N: ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if pepperoni == "Y":
    if size == "S":
        bill += 1
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 2

print(f"Your bill is ${bill}")



