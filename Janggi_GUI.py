# Author: Sebastian Gajardo
# Date: 2/21/21
# Description: User interface to play Janggi chess game using pygame.

import pygame

pygame.init()  # Initialize pygame.

screen = pygame.display.set_mode((495, 550))  # Create the screen (width, height).

pygame.display.set_caption("Jingga")  # Title.
icon = pygame.image.load("Images/Horse.png")  # Icon.
pygame.display.set_icon(icon)

# Janggi board background image.
janggi_board = pygame.image.load("images/janggi_board.jpg")

# Red king image and placement info.
red_king_img = pygame.image.load("images/red_king.png")
red_king_x = 228  # Initial x coordinate.
red_king_y = 64  # Initial y coordinate.

# Blue king image and placement info.
blue_king_img = pygame.image.load("images/blue_king.png")
blue_king_x = 228  # Initial x coordinate.
blue_king_y = 448  # Initial y coordinate.

# Red guard image and placement info.
red_guard_img = pygame.image.load("images/red_guard.png")
red_guard1_x = 180  # Initial x coordinate.
red_guard1_y = 14  # Initial y coordinate.
red_guard2_x = 290  # Initial x coordinate.
red_guard2_y = 14  # Initial y coordinate.


def red_king(x, y):
    """
    Displays the red king Janggi chess piece at passed x, y coordinates.
    """
    screen.blit(red_king_img, (x, y))  # Display red_king piece at x and y screen coordinates.


def blue_king(x, y):
    """
    Displays the blue king Janggi chess piece at passed x, y coordinates.
    """
    screen.blit(blue_king_img, (x, y))  # Display blue_king piece at x and y screen coordinates.


def red_guard(x, y):
    """
    Displays the red king Janggi chess piece at passed x, y coordinates.
    """
    screen.blit(red_guard_img, (x, y))  # Display red_guard piece at x and y screen coordinates.


# Game loop.
unfinished = True
while unfinished:

    screen.fill((0, 0, 0))  # Black background in RBG format.
    screen.blit(janggi_board, (0, 0))  # Background Janggi board image.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            unfinished = False

    red_king(red_king_x, red_king_y)  # Displays red_king at given coordinates.
    blue_king(blue_king_x, blue_king_y)  # Display blue_king at given coordinates.
    red_guard(red_guard1_x, red_guard1_y)  # Display red_guard at given coordinates.
    red_guard(red_guard2_x, red_guard2_y)  # Display red_guard at given coordinates.

    pygame.display.update()  # Update screen.
