# import random
# from hangmanwords import words

# def greet():
#     print("Hello")
#     print("My name is Peace")
#     print("Welcome")

# greet()

# def greet_with_name(first_name,second_name):
#     print(f"Hello my name is {first_name} {second_name}")
    

# greet_with_name(second_name="Peace",first_name="Sunguti")

# def calculate_love_score(name1,name2):
#     count_1 = 0
#     count_2 = 0
#     concatenate_word = name1 + name2
#     concatenate_word = concatenate_word.replace(" ", "")
#     check_word1 = "true"
#     check_word2 = "love"
#     for i in concatenate_word.lower():
#         if i in check_word1:
#             count_1 += 1
#         if i in check_word2:
#             count_2 += 1
#     print(f"{count_1}{count_2}")

# calculate_love_score("Kanye West","Kim Kardashian")
        
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
    
# calculate_love_score("Kanye West", "Kim Kardashian")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def ceaser(direction_given, plain_text, shift_amount):
#     no_whitespace_text = plain_text.replace(" ", "")
#     if direction_given.lower() == 'encode':
#         def encrypt(plain_text, shift_amount):
#             shift_alphabet = ""
#             for letter in (plain_text):
#                 new_index = alphabet.index(letter) + shift_amount
#                 if new_index >= alphabet.index("z"):
#                     new_index %= len(alphabet)
#                 newletter = alphabet[new_index]
#                 shift_alphabet += newletter
#             print(f"This is your decoded message : {shift_alphabet}")
#         encrypt(no_whitespace_text,shift)
#     else:
#         def decrypt(plain_text,shift_amount):
#             original_alphabet = ""
#             for letter in plain_text:
#                 original_index = alphabet.index(letter) - shift_amount
#                 original_alphabet += alphabet[original_index]
#             print(f"This is the original message: {original_alphabet}")

#         decrypt(no_whitespace_text, shift)
# ceaser(direction,text,shift)

def ceaser(direction_given,plain_text,shift_amount):
    new_text = ""
    if direction_given == "decode":
                shift_amount *=- 1
    for letter in plain_text:
        if letter in alphabet:    
            new_index = alphabet.index(letter) + shift_amount
            new_index %= len(alphabet)
            new_letter = alphabet[new_index]
            new_text += new_letter
        else:
            new_text += letter
    print(f"This is the {direction_given}d message: {new_text}")


ceaser(direction,text,shift)

# def caesar(direction_given, plain_text, shift_amount):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     new_text = ""

#     for letter in plain_text:
#         if letter in alphabet:
#             if direction_given == "decode":
#                 new_index = (alphabet.index(letter) - shift_amount) % len(alphabet)
#             else:  # Encoding case
#                 new_index = (alphabet.index(letter) + shift_amount) % len(alphabet)

#             new_letter = alphabet[new_index]
#             new_text += new_letter
#         else:
#             # Keep spaces and punctuation unchanged
#             new_text += letter

#     print(f"This is the {direction_given}d message: {new_text}")
    
# caesar(direction,text,shift)
    