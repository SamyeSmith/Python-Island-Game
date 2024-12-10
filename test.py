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

    def move(self, direction, map_data):
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

def user_start(users, map_data, health):
    user = User(1, health, 0, 0)
    users.append(user)
    map_data[0][0] = "P"
    print("User starting at 0, 0.")

def grid_refresh(map_data, users):
    initialize_map(len(map_data))
    for user in users:
        map_data[user.get_y()][user.get_x()] = "P"
    print_map()

def user_move(user, map_data):
    direction = input("""
                      Enter user movement.
                      UP
                      DOWN
                      LEFT
                      RIGHT
                      """).lower()
    user.move(direction, map_data)
    grid_refresh(map_data, users)

# Example usage
map_data = [['.' for _ in range(5)] for _ in range(5)]
users = []
health = 100

def initialize_map(size):
    global map_data
    map_data = [['.' for _ in range(size)] for _ in range(size)]

def print_map():
    for row in map_data:
        print(' '.join(row))

user_start(users, map_data, health)
user_move(users[0], map_data)
