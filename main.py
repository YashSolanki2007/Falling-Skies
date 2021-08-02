# Imports
import pygame
import random
import math
import time
import sys

# Game Variables
WIDTH = 900
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Skies")

# Set the screen icon
icon = pygame.image.load("old-man.png")
pygame.display.set_icon(icon)

# Making the player
playerImg = pygame.image.load("old-man.png")

playerX = WIDTH / 2 - 64
playerY = HEIGHT - 100
playerX_change = 0

# Making the enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('lion.png'))
    enemyX.append(random.randint(70, WIDTH - 70))
    enemyY.append(random.randint(-150, -50))
    enemyY_change.append(1)

# Making the powerup
powerupImg = pygame.image.load("dollar.png")

powerupX = random.randint(70, WIDTH - 70)
powerupY = random.randint(-1000, -900)
powerupY_change = 1

# Making the font for the player score
player_score = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_font_x = 0
score_font_y = 0

# Making the font for the player lives
player_lives = 3
lives_font = pygame.font.Font('freesansbold.ttf', 32)
lives_font_x = 0
lives_font_y = 75

# Functions


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def powerup(x, y):
    screen.blit(powerupImg, (x, y))


def show_score(x, y):
    score = score_font.render("Score :" + str(player_score), True, (WHITE))
    screen.blit(score, (x, y))


def show_lives(x, y):
    lives = lives_font.render("Lives :" + str(player_lives), True, (WHITE))
    screen.blit(lives, (x, y))


def is_collision_with_enemy(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt((math.pow(playerX - enemyX, 2)) +
                         (math.pow(playerY - enemyY, 2)))

    if distance < 27:
        return True

    else:
        return False


def is_collision_with_powerup(playerX, playerY, powerupX, powerupY):
    distance = math.sqrt((math.pow(playerX - powerupX, 2)) +
                         (math.pow(playerY - powerupY, 2)))

    if distance < 27:
        return True

    else:
        return False


# Main Game Loop
running = True
while running:
    # Fill the screen
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_LEFT:
                playerX_change = -1

        if event.type == pygame.KEYUP:
            playerX_change = 0

    # Boundary Checking for player
    if playerX <= 0:
        playerX = 0

    if playerX >= WIDTH - 67:
        playerX = WIDTH - 67

    # Enemy Logic
    for i in range(num_of_enemies):

        enemyY[i] += enemyY_change[i]
        if enemyY[i] >= HEIGHT + 100:
            enemyX[i] = random.randint(70, WIDTH - 70)
            enemyY[i] = random.randint(-150, -50)
            enemyY[i] += enemyY_change[i]
            player_score += 1
            # print(player_score)

        # Collision
        collision = is_collision_with_enemy(
            enemyX[i], enemyY[i], playerX, playerY)
        if collision and player_lives <= 1:
            time.sleep(0.05)
            sys.exit()
            # enemyX[i] = random.randint(70, WIDTH - 70)
            # enemyY[i] = random.randint(-150, -50)

        if collision and player_lives > 0:
            player_lives -= 1
            player_score -= 2
            enemyX[i] = random.randint(70, WIDTH - 70)
            enemyY[i] = random.randint(-150, -50)
            # print(player_lives)

        enemy(enemyX[i], enemyY[i], i)

    # Boundary checking for the powerup
    if powerupY > HEIGHT + 100:
        powerupX = random.randint(70, WIDTH - 70)
        powerupY = random.randint(-1000, -900)

    # Collisions with powerup
    collision_2 = is_collision_with_powerup(
        playerX, playerY, powerupX, powerupY)
    if collision_2:
        player_score += 5
        player_lives += 1
        powerupX = random.randint(70, WIDTH - 70)
        powerupY = random.randint(-1000, -900)

    # Update the screen
    player(playerX, playerY)
    playerX += playerX_change
    powerup(powerupX, powerupY)
    powerupY += powerupY_change
    show_score(score_font_x, score_font_y)
    show_lives(lives_font_x, lives_font_y)
    pygame.display.update()
