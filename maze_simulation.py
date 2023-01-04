import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the constants
SCREEN_SIZE = (640, 480)

# Set up the maze
maze = [
    '#####',
    '#...#',
    '#.#.#',
    '#...#',
    '#####'
]

#Set up the size of the maze
MAZE_WIDTH = 40
MAZE_HEIGHT = 10

maze = [    '##########', 
            '#........#', 
            '#.####...#',
            '#........#',
            '#...######',
            '#........#',
            '######...#',
            '#........#',
            '#.#####..#',
            '#........#']

for y in range(MAZE_HEIGHT):
    if y == 0 or y == MAZE_HEIGHT - 1:
        maze.append('#' * MAZE_WIDTH)
    else:
        maze.append('#' + '.' * (MAZE_WIDTH - 2) + '#')


# Set up the starting position and direction
position = (1, 1)
direction = 'S'

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
        
# Set up the movement rules
def move_forward():
    global position
    x, y = position
    if direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    if maze[y][x] != '#':
        position = (x, y)
    
    else:
        # Check for obstacles in the right and left directions
        if direction == 'N':
            if maze[y][x - 1] != '#' and maze[y][x + 1] != '#':
                turn_left()
        elif direction == 'S':
            if maze[y][x - 1] != '#' and maze[y][x + 1] != '#':
                turn_left()
        elif direction == 'E':
            if maze[y - 1][x] != '#' and maze[y + 1][x] != '#':
                turn_right()
        elif direction == 'W':
            if maze[y - 1][x] != '#' and maze[y + 1][x] != '#':
                turn_right()
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
    if direction == 'N':
        next_pos = (position[0], position[1] - 1)
    elif direction == 'S':
        next_pos = (position[0], position[1] + 1)
    elif direction == 'E':
        next_pos = (position[0] + 1, position[1])
    elif direction == 'W':
        next_pos = (position[0] - 1, position[1])
    if maze[next_pos[1]][next_pos[0]] == '#':
        turn_left()
        turn_left()

    # Move forward
    move_forward()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the maze
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
           if col == '#':
                pygame.draw.rect(screen, (0, 0, 0), (x * 10, y * 10, 10, 10))

    # Draw the robot
    x, y = position
    pygame.draw.circle(screen, (0, 0, 0), (x * 10, y * 10), 5)

    # Update the display
    pygame.display.flip()

    # Add a delay
    pygame.time.delay(1000)


# Quit
