import random
import rock_paper_scissors_module
rock_paper_scissors = ['rock', 'paper','scissors']
choice_0 = "rock"
choice_1 = 'Paper'
choice_2 = "scissors"
# computer_choice = random.choice(rock_paper_scissors)
game_geussing = [rock_paper_scissors_module.rock, rock_paper_scissors_module.paper, rock_paper_scissors_module.scissors]

computer_choice = random.randint(0,2)


user_choice = int(input("What do you choose?Type 0 for rock 1 for paper or 2 for scissors\n"))
if user_choice >= 0 and user_choice <=2:
        print (f"User choice:{game_geussing[user_choice]}")
        
print(f'Computer choice:{game_geussing[computer_choice]}')

if user_choice >= 3 or user_choice < 0:
     print("Invald choice please try again!")
elif computer_choice == 0 and user_choice == 1:
    print("You win!!")
elif computer_choice == 1 and user_choice == 2:
    print ("You win!")
elif computer_choice == 2 and user_choice == 0:
    print ("You win!")
elif computer_choice == 2 and user_choice == 1:
    print ("Computer wins!")
elif computer_choice == 1 and user_choice == 0:
    print ("Computer wins!")
elif computer_choice == 0 and user_choice == 2:
    print("Computer wins")
elif computer_choice == 0 and user_choice == 0:
    print("This is a tie")
elif computer_choice == 1 and user_choice == 1:
    print("This is a tie")
elif computer_choice == 2 and user_choice == 2:
    print("This is a tie")
else: 
    print("Invald choice please try again!")

# if user_choice == 0:
#     print("User choice:")
#     print(choice_0)
#     print(rock_paper_scissors_module.rock)
# elif user_choice == 1:
#     print("User choice:")
#     print(choice_1)
#     print(rock_paper_scissors_module.paper)
# elif user_choice == 2:
#     print("User choice:")
#     print(choice_2)
#     print(rock_paper_scissors_module.scissors)
# else:
#     if user_choice >= 3 or user_choice < 0:
#      print("Invald choice please try again!")

# if user_choice >= 3 or user_choice < 0:
#      print("Invald choice please try again!")
# elif computer_choice == 0:
#     print("Computer choice:")
#     print(choice_0)
#     print(rock_paper_scissors_module.rock)
# elif computer_choice == 1:
#     print("Computer choice:")
#     print(choice_1)
#     print(rock_paper_scissors_module.paper)
# elif computer_choice == 2:
#     print("Computer choice:")
#     print(choice_2)
#     print(rock_paper_scissors_module.scissors)
# else:
#     if user_choice >= 3 or user_choice < 0:
#      print("Invald choice please try again!")


# import rock_paper_scissors_module #imported this file
# #gnerating integer numbers(includes a,b)
# random_nubers = random.randint(1,20)  
#  #generating floating point numbers in the range 0.0 <= X < 1.0, does not take arguments
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)
# scaled_value = random_number_0_to_1 * 10
# print(scaled_value)
# print(random_nubers)
# print(rock_paper_scissors_module.my_favourite_number) #used the file
# #generate floating point numbers in the range a <= N <= b
# random_float = random.uniform(1,20)
# print(random_float)



# choose = ["Head","Tail"]
# random_coin = random.choice(choose)
# print(random_coin)


random_heads_or_tails = random.randint(0,1)
print(random_heads_or_tails)
if random_heads_or_tails == 0:
    print("Head")
else: 
    print("Tail")
