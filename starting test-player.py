import time
import random

# Setting global variables
map_size = 0
health = 5
skill_bs = False
skill_dfs = False
skill_bfs = False
treasure = False
quit_game = False
error = False
monster = 0
moves = 0
player = "P"
users = []
x = 0
y = 0

# Creating map
def initialize_map(size):
    global map_data
    map_data = [[0] * size for _ in range(size)]
    print("Map initialized")

def print_map():
    for level in map_data:
        print("[ ", end='')
        print(" ][ ".join(map(str, level)), end='')
        print(" ]")

# Opening message
def opening_message():
    print("""
    Welcome to the island.
    You are stranded on a desert island, your aim is to find treasure around the island and make your way to a life boat.
    However, you will come across dangerous traps, puzzles, and creatures.
    Will you survive or will the island take you?
    """)
    map_size_q = input("""
    How big would you like the map to be?
    1. Small
    2. Medium
    3. Large
    """)
    if map_size_q == "1":
        print("You have chosen small map size. 5x5")
        initialize_map(5)
    elif map_size_q == "2":
        print("You have chosen medium map size. 9x9")
        initialize_map(9)
    elif map_size_q == "3":
        print("You have chosen large map size. 12x12")
        initialize_map(12)
    else:
        error_message()

class User:
    def __init__(self, id, health, x, y):
        self.id = id
        self.health = health
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < len(map_data) - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < len(map_data[0]) - 1:
            self.x += 1
        else:
            print("Invalid entry")
        grid_refresh()

def user_start():
    user = User(1, health, 0, 0)
    users.append(user)
    map_data[0][0] = "P"
    print("User starting at 0, 0.")

def grid_refresh():
    initialize_map(len(map_data))
    for user in users:
        map_data[user.get_y()][user.get_x()] = "P"
    print_map()

def error_message():
    print("""
    Error...
    Restarting...
    """)
    time.sleep(5)
    opening_message()

# Running functions
opening_message()
user_start()
print_map()
