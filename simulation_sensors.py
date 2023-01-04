import pygame
import serial
import sys

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Obstacle Avoiding Robot')

# Set the background color of the window
bg_color = (255, 255, 255)

# Initialize the robot's position and size
robot_x = window_size[0] / 2
robot_y = window_size[1] / 2
robot_size = 20

# Initialize the serial connection to the robot
ser = serial.Serial('/dev/ttyACM0', 115200)

# Initialize the obstacle's position and size
obstacle_x = 100
obstacle_y = 100
obstacle_size = 50

# Main game loop
while True:
    # Clear the window
    screen.fill(bg_color)

    # Receive sensor data from the robot
    sensor_data = ser.readline()
    print(sensor_data)

    # Parse the sensor data
    data = sensor_data.split(',')
    left_sensor = int(data[0])
    right_sensor = int(data[1])
    front_sensor = int(data[2])

    # Update the robot's position based on the sensor data
    if front_sensor < 30:
        robot_x -= 5
    elif left_sensor < 30:
        robot_y -= 5
    elif right_sensor < 30:
        robot_y += 5
    else:
        robot_x += 5

    # Check for collision with the obstacle
    if abs(robot_x - obstacle_x) < (robot_size + obstacle_size) / 2 and abs(robot_y - obstacle_y) < (robot_size + obstacle_size) / 2:
        print('Collision detected!')

    # Draw the obstacle
    pygame.draw.circle(screen, (0, 0, 255), (obstacle_x, obstacle_y), obstacle_size)

    # Draw the robot
    pygame.draw.circle(screen, (0, 0, 0), (robot_x, robot_y), robot_size)

    # Update the window
    pygame.display.flip()

    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
