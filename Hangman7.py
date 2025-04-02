import random

# words = ["mouse","table","clothe"]
# generated_word = random.choice(words)
# print(generated_word)
# word_list = []
# correct_letters = []
# for i in range(len(generated_word)) :
#     i = "_"
#     word_list.append(i)
# generated_blanks = "".join(word_list)
# print(generated_blanks)
#     placeholder = ""
# number_of_attempts = 0
# while not number_of_attempts == 7:
#     geussed_letter = input("Geuss a letter :")
    # for letter in generated_word :
    #     if letter == geussed_letter.lower():
    #         placeholder += letter
    #         correct_letters.append(letter)
    #     elif letter in correct_letters:
    #         placeholder += letter
    #     else:
    #         letter = "_"
    #         placeholder += letter
#     print(placeholder)
#     number_of_attempts += 1
# if placeholder == generated_word:
#     print("Yaay you won")
# else:
#     print("You lost!!")
           

from hangman_art import logo, stages      
from hangmanwords import words


print(logo)
 

# 3️⃣ Hangman (Full Version) ⚔️
choice_word = random.choice(words)
word_list = []

number_of_attempts = 6

for i in range(len(choice_word)) :
    i = "_"
    word_list.append(i)
generated_blanks = "".join(word_list)
print(generated_blanks)

geussed_letters = []
display = ""
while not choice_word == display :
    geussed_letter = input("Geuss a letter :") 

    if geussed_letter.lower() in geussed_letters:
        print("You have already geussed the letter!Geuss a new one")
        continue
    geussed_letters.append(geussed_letter)

    if geussed_letter.lower() in choice_word:
        for i in range(len(choice_word))  :
            if choice_word[i] == geussed_letter.lower():
                word_list[i] = choice_word[i]
        print(stages[number_of_attempts])
    else:
        number_of_attempts -= 1
        if number_of_attempts != 0:
            print(f"Wrong geuss,you have {number_of_attempts} lives left")
            print(stages[number_of_attempts])
        else:
            print(f"Sorry! You have lost,the word was {choice_word}")
            print(stages[number_of_attempts])
            break
    updated_word_list =  "".join(word_list)
    display = updated_word_list 
    print(display)

if choice_word == display:
    print("congrats you won")


#1️⃣ Number Guessing Game 🎲

# number_geussed = random.randint(0,100)
# user_number = -1
# while user_number != number_geussed:
#     user_number = int(input("I'm thinking of a number between 1-100.Geuss the number:"))
#     if user_number == number_geussed:
#         print("Yaay you win")
#     elif user_number >= number_geussed:
#         print ("Too high")
#     else:
#         print ("Too low")

#2️⃣ Word Scramble Game 🔠
# word_list = ["apple", "cherry", "tomato", "peas", "peach", "pear"]
# random_word = random.choice(word_list)  # Pick a random word
# attempts = 3
# shuffled_word = list(random_word)  # Convert string to list
# random.shuffle(shuffled_word)  # Shuffle the list
# shuffled_word = "".join(shuffled_word)  # Convert back to string
# while attempts > 0:
#     user_geuss = input("What could the shuffled word be?")
#     if user_geuss.lower() == random_word:
#         print("Congratulations you won!")
#         break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Try again {attempts} attempts left")
#         else:
#             print("Sorry you lost!")




