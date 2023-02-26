import time
import os
import colorama
import sys
import random
from new_game import *
from os.path import exists
from timeit import default_timer

file_exists = exists("games/game_title.txt")

def tutorial():
    game_title_file = open('games/game_title.txt', 'r')
    game_title = game_title_file.readline()
    game_title_file.close()

    team_file = open(f'games/{game_title}/your_team.txt')
    team = team_file.readline()
    team_file.close()
    
    other_teams_file = open('other_teams.txt')
    other_teams = other_teams_file.readlines()
    
    os.system("clear")
    print("Welcome to the tutorial, that will teach you all about the game!")
    time.sleep(1)
    
    print(f"""
Just before the final race of the 2022 Season, The {team}racing team has made you their intern team principal. You must try to bring the team to a decent result this race. If you do, {team}might make you the team principal for 2023!
""")
    time.sleep(5)
    
    print("It's time for the beginning of the final race weekend of 2022! Since you arrived late, you missed the 3 practices, so now it's time for qualifying, and qualifying determines your position on the track for the race. Let's head down to the track...")
    time.sleep(5)
    
    os.system("clear")
    print("Welcome to The Yas Marina Circuit in Abu Dubai! It's time to prepare for the weekend ahead. There is still an hour until qualifying, so you have decided to give the team a speech ahead of the session.")
    time.sleep(5)
    
    speech = input("What would you like to say in your speech to the entire team? ")
    time.sleep(1)
    
    print("Your speech has inspired and moved the team to keep working hard! Just because you missed almost the entire season doesn't mean that you can't lead the team to victory.")
    time.sleep(3)
    os.system("clear")
    
    print("It's finally time for Qualifying! Qualifying is grouped into 3 stages. The first one is Q1, where only the top 15 qualifiers advance to the next stage.")
    time.sleep(3)
    
    drivers_file = open(f'games/{game_title}/your_team.txt', 'r')
    drivers = drivers_file.readlines()
    driver1 = drivers[1]
    driver2 = drivers[2]
    drivers_file.close()
    
    print(f"Your Drivers, {driver1}and {driver2} are in their cars, ready to head out to set their times on your command.")
    time.sleep(3)
    os.system("clear")
    
    print("This is how Q1 works:")
    print("Your drivers have 20 Minutes (Or 5 minutes in real time) to set their best laps. At the end, the bottom 5 drivers will be out of the session, but the top 15 will advance.")
    time.sleep(5)
    print("At any time, you can tell your drivers to go faster, slower, to pit, and other things like that.")
    # Ask to Begin
    start_q1 = input("Would you like to begin Q1? (y/n): ")
    if start_q1 == "y":
        timeLoop = True

        # Variables to keep track and display
        Sec = 0
        Min = 0
        # Begin Process
        timeLoop = start_q1
        print("Entering Q1...")
        time.sleep(2)
        os.system("clear")
        print(f"Alright! Q1 has offically started. Whenever you're ready, you can send your drivers out with the command, 'Send {driver1} out'. You can listen to their radio, and communicate with them. The dashboard will keep you up to date with everything happening on the track.")
        time.sleep(5)
        print(f"When you want to send them back in the pit lane to rest with the command, 'Send {driver1} in'. Just be sure that they have enough time to get a few laps in so that they can get a good result. The dashboard will also update you with how their fuel and tire situations are.")
        time.sleep(5)
        print("Let's go qualify!")
        time.sleep(1)
        
        # Qualifying
        
        print(f"Already, {other_teams[27]} and {other_teams[28]} are out on the track.")
        
        q1_command = input("What is your command?")
        
        q1_timer = time.time()
        seconds = 0
        minutes = 0
        
    while True:
        try:
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - q1_timer) - minutes * 601
            
            if seconds >= 60:
                minutes += 1
                seconds = 0
                print("4 Minutes Remianing")
            
            if minutes >= 2:
                print("3 Minutes Remaining")
                
            if minutes >= 3:
                print("2 Minutes Remaining")
            
            if minutes >= 4:
                print("1 Minute Remianing")
            
            if minutes >= 5:
                print("Time's Up! Chequered Flag for Q1!")
            
            if q1_command == f"Send {driver1} out" or f"Send {driver2} out":
                print("Alright! Sending him out...")
                time.sleep(1)
                print("Alright, He is now out on the track.")

                qualifying_times = random.choices([1, 2], weights=[0.8, 0.2])[0]
                
                
        except KeyboardInterrupt:
            break
        # Program will cancel when user presses Ctrl + C
    
    
    
    
    
    
    
    