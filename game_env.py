import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Game - Draw Track and Generate Car")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game variables
drawing = False
clock = pygame.time.Clock()

# Car
car_img = pygame.Surface((30, 15))
car_img.fill(white)
car_rect = car_img.get_rect(center=(width // 2, height // 2))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                pygame.draw.circle(screen, white, event.pos, 5)

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car_rect.y -= 5
    if keys[pygame.K_DOWN]:
        car_rect.y += 5
    if keys[pygame.K_LEFT]:
        car_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        car_rect.x += 5

    # Update display
    screen.fill(black)
    screen.blit(car_img, car_rect)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
