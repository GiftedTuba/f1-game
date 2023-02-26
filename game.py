import linecache
import colorama
from colorama import Fore
import re
import os
import getpass
import time
from new_user import *
from new_game import *
from tutorial import *


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it

os.system("clear")

if os.path.isfile("/home/matthew/python/formula1game/username.txt") == False:
    print(Fore.RED +  'Note: No users were found. Attempting to create a new user in 3...2...1' + Fore.WHITE)
    time.sleep(3)
    new_username()

with open(r"/home/matthew/python/formula1game/username.txt", 'r') as username_file:
    username = username_file.readline()
    print(Fore.WHITE + f"Welcome back, {username}!")

print("Welcome to The Formula 1 Manager Game 2023!")

time.sleep(1)

path = "games"

dir = os.listdir(path)

if len(dir) == 0:
    print(Fore.RED + 'Note: No Currently created Games were found. To play, you must create a new game.' + Fore.WHITE)
    

choice_1 = input("Would you like to start a new game, or continue a game? ")

if choice_1 == 'new game' or 'newgame' or 'New Game' or 'New game' or 'NEW GAME' or 'new' or 'New' or 'NEW':
    print("Okay, starting a new game...")
    new_game()
    file_exists = exists("games/game_title.txt")  
    tutorial()
    
else:
    print("That command wasn't understood. Please type it again, or enter 'Help' for more detail.")
    time.sleep(2)
    choice_1()



