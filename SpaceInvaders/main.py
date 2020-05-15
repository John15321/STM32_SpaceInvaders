#!/usr/bin/python

import random
import math
import pygame

# Initializing PyGame
pygame.init()

# If Intellisense is showing you error you may need to add (case for Visual Studio Code):
# this one will just white list pygame
# "python.linting.pylintArgs": [
#   "--extension-pkg-whitelist=pygame"
# ]
# to your setting.json, because Pylint imports modules to effectively identify valid
# methods and attributes. It was decided that importing c extensions that
# are not part of the python stdlib is a security risk and could introduce malicious code.

# Creating the screen
# screen size (has to be a tuple: width x height)
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
# screen color (in RGB)
screen_color = (27, 27, 47)  # very darker blue/purple

# Adding background
background = pygame.image.load("background.png")

# value if the game is running
RUNNING = True

# Title and Icon
pygame.display.set_caption("Space Invaders with STM32")
pygame.display.set_icon(pygame.image.load("ufo.png"))

# Player
# players icon
playerImg = pygame.image.load("player.png")
# starting player position
player_x_position = 370
player_y_position = 400
player_speed = 0  # in pixels

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

text_x_position = 10
text_y_position = 10

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemy_x_position = []
enemy_y_position = []
enemy_x_speed = []

for each in range(0, 5):
    enemy_x_position.append(random.randint(0, 736))
    enemy_y_position.append(random.randint(0, 200))
    enemy_x_speed.append(0.5)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bullet_x_position = 0
bullet_y_position = 480
bullet_y_speed = 0.5
bullet_ready = True


def player(new_x_position, new_y_position):
    '''
    Player funtion created for player utilities, like drawing the player or handling damage
    '''
    # drawing the players icon
    screen.blit(playerImg, (new_x_position, new_y_position))


def enemy(new_x_position, new_y_position):
    '''
    Enemy funtion created for enemy utilities, like drawing the player or handling damage
    '''
    # drawing the enemy icon
    screen.blit(enemyImg, (new_x_position, new_y_position))


def bullet(new_x_position, new_y_position):
    '''
    Bullet funtion created for bullet utilities, like drawing the player or handling damage
    '''
    screen.blit(bulletImg, (new_x_position+16, new_y_position+10))


def isCollision(obj1_x_position, obj1_y_position, obj2_x_position, obj2_y_position):
    distance = math.sqrt((obj1_x_position-obj2_x_position)
                         ** 2+(obj1_y_position-obj2_y_position)**2)
    return distance < 27


# def show_score(score_x, y):
#     sc = font.render("Score: "+str(score), True, (255, 255, 255))
#     screen.blit(sc, (x, y))


# Main Game Loop
while RUNNING:
    # setting the background color for the whole screen
    screen.fill(screen_color)

    # for loop for catching evvents for PyGame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # if a key is pressed -> move
        if event.type == pygame.KEYDOWN:
            # if left arrow -> go left
            if event.key == pygame.K_LEFT:
                print("Pressed left")
                player_speed = -1
            # if right arrow -> go right
            if event.key == pygame.K_RIGHT:
                print("Pressed right")
                player_speed = 1
            # if space -> shoot bullet
            if event.key == pygame.K_SPACE and bullet_ready:
                print("Pressed space")
                bullet_ready = False
                bullet_x_position = player_x_position
                bullet_y_position = player_y_position

        # if a key that was pressed is lifted
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                player_speed = 0

    # Updating the bullet
    if bullet_ready == False:
        bullet_y_position -= bullet_y_speed
        bullet(bullet_x_position, bullet_y_position)
    # Boundries for the bullet
    if bullet_y_position <= -32:
        bullet_ready = True

    # Updating player positions
    player_x_position += player_speed
    # Adding boundiers for the player so it doesnt go off the screen
    if player_x_position <= 0:
        player_x_position = 0
    if player_x_position >= 736:
        player_x_position = 736

    for i in range(0, 5):
        # Updating enemy position
        enemy_x_position[i] += enemy_x_speed[i]
        # Adding boundiers for the enemy also
        if enemy_x_position[i] <= 0:
            enemy_x_speed[i] *= -1
            enemy_y_position[i] += 40
        if enemy_x_position[i] >= 736:
            enemy_x_speed[i] *= -1
            enemy_y_position[i] += 40

        if enemy_y_position[i] <= 0:
            enemy_y_position[i] = 0
        if enemy_y_position[i] >= 350:
            enemy_x_position[i] = random.randint(0, 736)
            enemy_y_position[i] = random.randint(0, 200)

        # Resolcing collisions
        collision = isCollision(
            enemy_x_position[i], enemy_y_position[i], bullet_x_position, bullet_y_position)
        if collision:
            bullet_y_position = 480
            bullet_ready = True
            score += 1
            enemy_x_position[i] = random.randint(0, 736)
            enemy_y_position[i] = random.randint(0, 200)
            print("Score: " + str(score))
        # Drawing the enemy
        enemy(enemy_x_position[i], enemy_y_position[i])

    # Drawing the player
    player(player_x_position, player_y_position)
    # Show score
    sc = font.render("Score: "+str(score), True, (255, 255, 255))
    screen.blit(sc, (10, 10))
    pygame.display.update()
