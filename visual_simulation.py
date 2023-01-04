import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the constants
OBSTACLE_PROBABILITY = 0.1
SCREEN_SIZE = (640, 480)

# Set up the starting position and direction
position = (0, 0)
direction = 'North'

# Set up the movement rules
def move_forward():
    global position
    x, y = position
    if direction == 'North':
        y += 1
    elif direction == 'South':
        y -= 1
    elif direction == 'East':
        x += 1
    elif direction == 'West':
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

# Set up the screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set up the simulation loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for an obstacle
    if random.random() < OBSTACLE_PROBABILITY:
        # Turn to avoid the obstacle
        turn_left()
        turn_left()
    else:
        # Move forward
        move_forward()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the robot
    x, y = position
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
