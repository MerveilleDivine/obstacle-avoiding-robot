#This is a code for the simulation of an obstacle avoiding robot.

import random

# Set up the constants
OBSTACLE_PROBABILITY = 0.1

# Set up the starting position and direction
position = (0, 0)
direction = 'N'

# Set up the movement rules
def move_forward():
    global position
    x, y = position
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    position = (x, y)

def turn_left():
    global direction
    if direction == 'N':
        direction = 'W'
    elif direction == 'W':
        direction = 'S'
    elif direction == 'S':
        direction = 'E'
    elif direction == 'E':
        direction = 'N'

def turn_right():
    global direction
    if direction == 'N':
        direction = 'E'
    elif direction == 'E':
        direction = 'S'
    elif direction == 'S':
        direction = 'W'
    elif direction == 'W':
        direction = 'N'

# Set up the simulation loop
while True:
    # Check for an obstacle
    if random.random() < OBSTACLE_PROBABILITY:
        # Turn to avoid the obstacle
        turn_left()
        turn_left()
    else:
        # Move forward
        move_forward()
    print(position)
