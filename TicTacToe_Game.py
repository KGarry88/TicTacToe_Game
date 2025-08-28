# ---------------------------------------------------------------------------#
# TIC-TAC-TOE GAME
# 
# Author: Kevin Garry
# Date: 8/27/2025
# ---------------------------------------------------------------------------#

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Different colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Define font
font = pygame.font.SysFont("bahnschrift", 25)

# Define title text from center
text_surface = font.render("Tic-Tac-Toe", True, (white))
text_rect = text_surface.get_rect(center=(width / 2, height / 3))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    screen.blit(text_surface, text_rect)
    pygame.display.update()

pygame.quit()