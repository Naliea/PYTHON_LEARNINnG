# Define the clear function to clear the console
import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")