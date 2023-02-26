import time
import os
from colorama import Fore
from colored import *
from colored import fg

red_bull_color = fg('blue')
ferrari_color = fg('#ff0000')
mercedes_color = fg('#00ffd5')
alpine_color = fg('#0084ff')
mclaren_color = fg('#ff7700')
alfa_romeo_color = fg('#751205')
aston_martin_color = fg('#014014')
hass_color = fg('#ffffff')
alphatauri_color = fg('#696868')
williams_color = fg('#002aff')

def new_game():
    game_title = input("What would you like to call your new game? ")
    os.mkdir(f"/home/matthew/python/formula1game/games/{game_title}")
    game_title_file = open('/home/matthew/python/formula1game/games/game_title.txt', 'w')
    game_title_file.write(f"{game_title}")
    game_title_file.close()
    
    time.sleep(3)
    
    print("Welcome to your new game! You will be able to begin managing your own F1 Team in this game.")
    time.sleep(3)
    
    team = input("What team would you like to lead? ")
    
    if team == "Red Bull":
        driver1 = "Max Verstappen"
        driver2 = "Sergio Perez"
        reserve_driver = "Danial Ricciardo"
        drivers = [f'{driver1}, {driver2}']
    
    if team == "Ferrari":
        driver1 = "Charles Leclerc"
        driver2 = "Carlos Sainz"
        reserve_driver = "Antonio Giovinazzi"
        drivers = [f'{driver1}, {driver2}']

    if team == "Mercedes":
        driver1 = "Lewis Hamilton"
        driver2 = "George Russell"
        reserve_driver = "Mick Schumacher"
        drivers = [f'{driver1}, {driver2}']
    
    if team == "Alpine":
        driver1 = "Esteban Ocon"
        driver2 = "Pierre Gasly"
        reserve_driver = "Jack Doohan"
        drivers = [f'{driver1}, {driver2}']

    if team == "Mclaren":
        driver1 = "Lando Norris"
        driver2 = "Oscar Piastri"
        reserve_driver = "Alex Palou"
        drivers = [f'{driver1}, {driver2}']
    
    if team == "Alfa Romeo":
        driver1 = "Valteri Bottas"
        driver2 = "Zhou Guanyu"
        reserve_driver = "Theo Pourchaire"
        drivers = [f'{driver1}, {driver2}']
    
    if team == "Aston Martin":
        driver1 = "Lance Stroll"
        driver2 = "Fernando Alonso"
        reserve_driver = "Felipe Drugovich"
        drivers = [f'{driver1}, {driver2}']
    
    if team == "Hass":
        driver1 = "Kevin Magnussen"
        driver2 = "Nico Hulkenburg"
        reserve_driver = "Pietro Fittipaldi"
        drivers = [f'{driver1}, {driver2}']
        
    if team == "Alphatauri":
        driver1 = "Yuki Tsunoda"
        driver2 = "Nyck De Vries"
        reserve_driver = "Liam Lawson"
        drivers = [f'{driver1}, {driver2}']
        
    if team == "Williams":
        driver1 = "Alex Albon"
        driver2 = "Logan Sargeant"
        reserve_driver = "Stoffel Vandoorne"
        drivers = [f'{driver1}, {driver2}']
    
    team_file = open(f'/home/matthew/python/formula1game/games/{game_title}/your_team.txt', 'a')
    team_file.write(f"""{team}
{driver1}
{driver2}
{reserve_driver}""")
    team_file.close()
    
    print("Your new game has been created. We hope you enjoy it!")
    time.sleep(2)
    
    tutorial_choice = input("Would you like to begin a specialized tutorial to learn about the game, or would you like to skip it? ")
    
    if tutorial_choice == "Yes":
        print("Okay, entering tutorial now!")
        time.sleep(2)
