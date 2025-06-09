import pygame
import math

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
RED = (255, 255, 0)
CIRCLE_RADIUS = 100
BALL_RADIUS = 8

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the center of the circle
center_x, center_y = WIDTH // 2, HEIGHT // 2

# Define the angle of the ball
angle = 91
png=19.4

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the position of the ball
    ball_x = center_x + CIRCLE_RADIUS * math.cos(angle)
    ball_y = center_y + CIRCLE_RADIUS * math.sin(angle)

    arc_x= center_x + (CIRCLE_RADIUS-31) * math.cos(png)
    arc_y= center_y + (CIRCLE_RADIUS-31)* math.sin(png)

    # Draw everything
    #screen.fill(WHITE)
  #  pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), CIRCLE_RADIUS, 1)
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), BALL_RADIUS)
    pygame.draw.circle(screen, RED, (center_x-39, center_y-17), BALL_RADIUS+3,6)
    pygame.draw.circle(screen, RED, (center_x+39, center_y-17), BALL_RADIUS+3,6)
    if png <21.2:
     pygame.draw.circle(screen, RED, (int(arc_x), int(arc_y)), BALL_RADIUS-3)
    
   

    # Update the angle
    angle += 0.015
    png+=0.01
    

    

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(65)

# Quit Pygame
pygame.quit()

