# importing
import time
import math
import random


#Setting global variables
global Map
map_size = 0
Health = 5
Skill_BS = False
Skill_DFS = False
Skill_BFS = False
Treasure = False
Quit = False
Error = False
Monster = 0
Moves = 0
Player = "P"
X = 0
Y = 0

#Creating map
def initalise_map(map_size):
    global Map
    Map = [] #creating list for a Map
    #Map.append("P")
    for i in range(map_size):#setting how large the Map will become
        Level = [0] * map_size#making the width the same as height to make a square
        Map.append(Level)#adding nine 0s into the list
    print("Test")
    # return Map
#def print_map():
    for Level in Map:
        print("[ ", end='')#Adds [ to the start of the line
        print(" ][ ".join(map(str, Level)), end='')#print the list of Map seprated by ][  , 'end to make the line continuous
        print(" ]")#Adds ] at the end of the line
    Map[1:0]="P"
        

#Opening message
def opening_message():
    print("""
          Welcome to the island.\n 
          You are stranded on a desert island, your aim is to find treasure around the island and make your way to a life boat.
          However you will come across dangerous traps, puzzles and creatures.\n
          Will you survive or will the island take you?
          """)
    running = True
    map_size_Q = input("""
                       How big would you like the map to be?\n
                       1.Small\n
                       2.Medium\n
                       3.Large\n
                       """)
    if map_size_Q == "1":
        print("You have chosen small map size. 5X5")
        map_size = 5
        initalise_map(map_size)
    elif map_size_Q=="2":
        print("You have chosen medium map size. 9X9")
        map_size = 9
        initalise_map(map_size)
    elif map_size_Q=="3":
        print("You haev chosen large map size. 12X12")
        map_size = 12
        initalise_map(map_size)
    else:
        Error_message()
#print_map()

#insert player
def player_start():
    print("P")




#Menue

#Search BS

#Search DFS

#Search BFS

#Treasure Found

#Health

#Heal

#Movement

#Trap--Pitfall

#Trap--Darts

#Puzzle--Riddle

#Monster--Slime

#Monster--Skeleton

#Esacape

#Quit

#Error message
def Error_message():
    print("""
          Error...\n
          Restarting...\n
          """)
    time.sleep(5)
    opening_message()


#Running functions

opening_message()

