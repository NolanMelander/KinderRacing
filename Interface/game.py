import pygame
import Interface.cars as cars
from random import randint

pygame.init()

# SETUP THE GAME WINDOW
#display_width, display_height = pygame.display.Info().current_w, pygame.display.Info().current_h
#gameDisplay = pygame.display.set_mode((display_width, display_height))

display_width, display_height = 800, 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kinder Racing')

black = (0, 0, 0)

clock = pygame.time.Clock()
raceFinished = False

background = pygame.image.load("..\Resources\Track\\TrackTest.png")

# CAR FUNCTIONS
def player_car(x, y):
    gameDisplay.blit(cars.player, (x, y))


def computer_one_car(x, y):
    gameDisplay.blit(cars.computer_one, (x, y))


def computer_two_car(x, y):
    gameDisplay.blit(cars.computer_two, (x, y))


def computer_three_car(x, y):
    gameDisplay.blit(cars.computer_three, (x, y))


# CARS SETUP
player_x = comp_1_x = comp_2_x = comp_3_x = 0
player_y = 150
comp_1_y = 250
comp_2_y = 350
comp_3_y = 450
player_x_change = comp_1_change = comp_2_change = comp_3_change = 0


# TRACK LAPS
player_laps = 0
comp_1_laps = 0
comp_2_laps = 0
comp_3_laps = 0

while not raceFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raceFinished = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player_x_change = randint(1, 10)
            comp_1_change = randint(1, 10)
            comp_2_change = randint(1, 10)
            comp_3_change = randint(1, 10)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            player_x_change = comp_1_change = comp_2_change = comp_3_change = 0

    # ADJUST CAR POSITIONS
    player_x += player_x_change
    comp_1_x += comp_1_change
    comp_2_x += comp_2_change
    comp_3_x += comp_3_change

    # PREPARE DISPLAY
    gameDisplay.blit(background, (0, 95, display_width, display_height))
    #gameDisplay.fill(black)
    player_car(player_x, player_y)
    computer_one_car(comp_1_x, comp_1_y)
    computer_two_car(comp_2_x, comp_2_y)
    computer_three_car(comp_3_x, comp_3_y)
    pygame.display.update()
    clock.tick(60)

    # REPOSITION CARS IF NEEDED
    if player_x > display_width:
        player_x = -80
        player_laps += 1
        print("Orange has completed lap " + (str(player_laps)))

    if comp_1_x > display_width:
        comp_1_x = -80
        comp_1_laps += 1
        print("Black has completed lap " + (str(comp_1_laps)))

    if comp_2_x > display_width:
        comp_2_x = -80
        comp_2_laps += 1
        print("Red has completed lap " + (str(comp_2_laps)))

    if comp_3_x > display_width:
        comp_3_x = -80
        comp_3_laps += 1
        print("White has completed lap " + (str(comp_1_laps)))

pygame.quit()
quit