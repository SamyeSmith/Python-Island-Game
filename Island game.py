import time
import random

# Setting global variables
global bs_search_list
map_size = 0
health = 5
skill_bs = False
skill_dfs = False
skill_bfs = False
treasure = 0
treasure = int(treasure)
quit_game = False
error = False
monster = 0
moves = 0
player = "U"
users = []
treasures = []
traps = []
powers = []
x = 0
y = 0
map_size_q = 0
bs_search_list = []
traces = []
# global bs_list
# global high
# global low
# global mid
# global T
# T = "T"
# high = 0
# low = 0
# mid = 0

# Creating map
def initialize_map(size):
    global map_data
    map_data = [[0] * size for _ in range(size)]
    print("Map initialized")

#displaying the map
def print_map():
    for level in map_data:
        print("[ ", end='')
        print(" ][ ".join(map(str, level)), end='')
        print(" ]")

# Opening message
def opening_message():
    global map_size_q
    global mrange
    print("""
    Welcome to the island.
    You are stranded on a desert island, your aim is to find treasure around the island and make your way to a life boat.
    However, you will come across dangerous traps and puzzles.
    Will you survive or will the island take you?
    """)
    time.sleep(2)
    map_size_q = input("""
    How big would you like the map to be?
    1. Small
    2. Medium
    3. Large
    """)
    if map_size_q == "1":
        print("You have chosen small map size. 5x5")
        mrange = 5
        initialize_map(5)
    elif map_size_q == "2":
        print("You have chosen medium map size. 9x9")
        mrange = 9
        initialize_map(9)
    elif map_size_q == "3":
        print("You have chosen large map size. 12x12")
        mrange = 12
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

class Treasure:
    def __init__(self, id, t_x, t_y):
        self.id = id
        self.t_x = t_x
        self.t_y = t_y
    
    def get_t_x(self):
        return self.t_x

    def get_t_y(self):
        return self.t_y
    
class Trap:
    def __init__(self, id, tr_x, tr_y):
        self.id = id
        self.tr_x = tr_x
        self.tr_y = tr_y
    
    def get_tr_x(self):
        return self.tr_x

    def get_tr_y(self):
        return self.tr_y

class Power:
    def __init__(self, id, p_x, p_y):
        self.id = id
        self.p_x = p_x
        self.p_y = p_y
    
    def get_p_x(self):
        return self.p_x

    def get_p_y(self):
        return self.p_y
    
class Trace:
    def __init__(self, id, tc_x, tc_y):
        self.id = id
        self.tc_x = tc_x
        self.tc_y = tc_y

    def get_tc_x(self):
        return self.tc_x
    
    def get_tc_y(self):
        return self.tc_y
    
    def Tmove(self, direction):
        if direction == "up" and self.tc_y > 0:
            self.tc_y -= 1
        elif direction == "down" and self.tc_y < len(map_data) - 1:
            self.tc_y += 1
        elif direction == "left" and self.tc_x > 0:
            self.tc_x -= 1
        elif direction == "right" and self.tc_x < len(map_data[0]) - 1:
            self.tc_x += 1
        else:
            print("Invalid entry")
    

def user_start():
    user = User(1, health, 0, 0)
    trace = Trace(1,0,0)
    users.append(user)
    traces.append(trace)
    map_data[0][0] = "U"
    print("User starting at 0, 0.")

def treasure_place():  
    global treasure
    treasures.clear()  # Clear any existing treasures
    num_treasures = 1  # Number of treasures to place

    for _ in range(num_treasures):
        if map_size_q == "1":
            t_x = random.randrange(1, 5)
            t_y = random.randrange(0, 5)
        elif map_size_q == "2":
            t_x = random.randrange(0, 9)
            t_y = random.randrange(1, 9)
        elif map_size_q == "3":
            t_x = random.randrange(1, 12)
            t_y = random.randrange(0, 12)
        treasure = Treasure(len(treasures) + 1, t_x, t_y)
        treasures.append(treasure)
    for treasure in treasures:
        map_data[treasure.get_t_y()][treasure.get_t_x()] = "0"
    print("Treasure placed")

def trap_place():  
    global trap
    traps.clear()  # Clear any existing treasures
    num_traps = 5  # Number of treasures to place
    for _ in range(num_traps):
        if map_size_q == "1":
            tr_x = random.randrange(1, 5)
            tr_y = random.randrange(0, 5)
        elif map_size_q == "2":
            tr_x = random.randrange(0, 9)
            tr_y = random.randrange(1, 9)
        elif map_size_q == "3":
            tr_x = random.randrange(1, 12)
            tr_y = random.randrange(0, 12)
        trap = Trap(len(traps) + 1, tr_x, tr_y)
        traps.append(trap)
    for trap in traps:
        map_data[trap.get_tr_y()][trap.get_tr_x()] = "0"
    print("Trap placed")

def power_place():  
    global power
    powers.clear()  # Clear any existing treasures
    num_power = 5  # Number of treasures to place
    for _ in range(num_power):
        if map_size_q == "1":
            p_x = random.randrange(1, 5)
            p_y = random.randrange(0, 5)
        elif map_size_q == "2":
            p_x = random.randrange(0, 9)
            p_y = random.randrange(1, 9)
        elif map_size_q == "3":
            p_x = random.randrange(1, 12)
            p_y = random.randrange(0, 12)
        power = Power(len(powers) + 1, p_x, p_y)
        powers.append(power)
    for power in powers:
        map_data[power.get_p_y()][power.get_p_x()] = "P"
    print("Powers placed")

def grid_refresh():
    initialize_map(len(map_data))
    for treasure in treasures:
        map_data[treasure.get_t_y()][treasure.get_t_x()] = "0"#T
    for trap in traps:
        map_data[trap.get_tr_y()][trap.get_tr_x()] = "0"#C
    for user in users:
        map_data[user.get_y()][user.get_x()] = "U"
    for power in powers:
        map_data[power.get_p_y()][power.get_p_x()] = "P"
    print_map()

def check_tresure(x, y):
    for treasure in treasures:
        if x == treasure.get_t_x() and y == treasure.get_t_y():
            print("You have found treasure! \n You win.")
            # treasure = treasure +1
            treasure =+ 1
            win_game()
        # treasures.remove(treasure)

def check_trap(x, y):
    global health
    for trap in traps:
        if x == trap.get_tr_x() and y == trap.get_tr_y():
            print("You have found a trap! \n Answer a riddle or lose health.")
            riddle = random.randrange(0, 3)
            if riddle == 0:
                riddle_answer0 = input("Riddle: What has a face and two hands but no arms or legs?").lower()
                if riddle_answer0 != "clock" and riddle_answer0 != "a clock":
                    print("You have fallen into the trap!")
                    health = health -1
                    print(f"You have {health} health left.")
                    if health == 0:
                        end_game()
                else:
                    print("Congratulations,you passed the trap!")

            elif riddle == 1:
                riddle_answer1 = input("Im the rare case when today comes before yesterday. What am I?").lower()
                if riddle_answer1 != "a dictionary" and riddle_answer1 != "dictionary":
                    print("You have fallen into the trap!")
                    health = health -1
                    print(f"You have {health} health left.")
                    if health == 0:
                        end_game()
                else:
                    print("Congratulations,you passed the trap!")

            elif riddle == 2:
                riddle_answer2 = input("What goes all the way around the world but stays in a corner?").lower()
                if riddle_answer2 != "a stamp" and riddle_answer2 != "stamp":
                    print("You have fallen into the trap!")
                    health = health -1
                    print(f"You have {health} health left.")
                    if health == 0:
                        end_game()
                else:
                    print("Congratulations,you passed the trap!")


# def binary_seach(bs_list, low, high, T):
#     global mid
#     bs_list = map_data
#     if map_size_q == "1":
#         high = str(high)
#         high = 5
#         low = str(low)
#         low = 0
#         mid = str(mid)
#         if high >= low:
#             mid = (high + low) // 2

#             if bs_list[mid] == T:
#                 return mid
            
#             elif map_data[mid] > T:
#                 return binary_seach(bs_list, low, mid -1, T)
            
#             else:
#                 return binary_seach(bs_list, mid + 1, high, T)
#         else:
#             return -1
#     BS_result = binary_seach(bs_list, 0, len(bs_list)-1, T)

# def binary_search(bs_x, y):
#     for user in users:
#         bs_x = user.get_x()
#         for i in range(mrange):
#             if bs_x == power.get_p_x() and i == power.get_p_y():
#                 print (f"Power found at {bs_x}, {i}.")
                
#             elif bs_x == trap.get_tr_x() and y == trap.get_tr_y():
#                 print (f"Trap found at {bs_x}, {i}.")

#             else:
#                 i += 1


# def binary_search(bs_x, y):
#         for i in range(mrange + 1):
#             bs_search_list.append(i) # making the list that will be used for BS search
#             i += 1
#             low = 0
#             high = mrange + 1
#             # bs_y = bs_search_list[x]
#             # print(bs_y)
#             # x += 1

#             # if v == 0:

#         while high >= low:

#                 mid = (high + low) // 2

#                 if bs_search_list[mid] == treasure.get_t_y():
#                     print (f"Treasure is on y: {treasure.get_t_y()}")
#                     break

#                 elif bs_search_list[mid] > treasure.get_t_y:
#                     high =- 1

#                 else:
#                     low =+ 1

                    # if bs_x == power.get_p_x() and target == power.get_p_y():
                    #     print (f"Power found at {bs_x}, {i}.")
                    #     v =+ 1
                    
                    # elif bs_x == trap.get_tr_x() and target == trap.get_tr_y():
                    #     print (f"Trap found at {bs_x}, {i}.")
                    #     v =+ 1
                    

                    # else:
                    #     i += 1


def check_power(x, y):
    for power in powers:
        if x == power.get_p_x() and y == power.get_p_y():
            t_y = treasure.get_t_y
            print("You have found a power up!")
            search = random.randrange(0, 2)
            # search = 3
            if search == 0:
                print("You have activted the default search for treasure.")
                
                for user in users:
                    bs_x = user.get_x()
                    for i in range(mrange):
                        if bs_x == power.get_p_x() and i == power.get_p_y():
                            print (f"Power found at {bs_x}, {i}.")
                            
                        elif bs_x == trap.get_tr_x() and y == trap.get_tr_y():
                            print (f"Trap found at {bs_x}, {i}.")

                        else:
                            i += 1

            # elif search == 3:
            #     print("You have activated the DFS search for treasure.")
            #     print("Not Implemented")
            # elif search == 2:
            #     print("You hve activated the BFS search for treasure.")
            #     print("Not Implemented")
            elif search == 1:
                print("You have activated the BS search")

                for i in range(mrange + 1):
                    bs_search_list.append(i)
                    i += 1
                    low = 0
                    high = mrange + 1

                while high >= low:

                    mid = (high + low) // 2

                    if bs_search_list[mid] == treasure.get_t_y():
                        print (f"Treasure is on y: {treasure.get_t_y()}")
                        break

                    elif bs_search_list[mid] > treasure.get_t_y():
                        high = mid - 1

                    else:
                        low = mid + 1

            

def user_move():
    direction = input("Enter user movement. UP DOWN LEFT RIGHT: ").lower()
    for user in users:
        user.move(direction)
    for user in users:
        check_trap(user.get_x(), user.get_y())
        check_tresure(user.get_x(), user.get_y())
        check_power(user.get_x(), user.get_y(), )
    user_move()

def error_message():
    print("""
    Error...
    Restarting...
    """)
    time.sleep(2)
    opening_message()

def end_game():
    print("Your game is over, you have lost.")
    time.sleep(2)
    quit()

def win_game():
    print(f"You have escaped with treasure! Well done!")
    time.sleep(2)
    quit()

    




# Running functions
opening_message()
time.sleep(1)
treasure_place()
trap_place()
power_place()
user_start()
print_map()
time.sleep(1)
user_move()
