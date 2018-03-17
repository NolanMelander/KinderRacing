import pygame
import Interface.cars as cars
import Interface.questions as questions
from random import randint

pygame.init()

# SETUP THE GAME WINDOW
display_width, display_height = 800, 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kinder Racing')
pygame.display.set_icon(cars.player)
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


def lap_tracker(lap):
    if lap == 1:
        image = pygame.image.load("..\Resources\Laps\lap_1.png")
    elif lap == 2:
        image = pygame.image.load("..\Resources\Laps\lap_2.png")
    elif lap == 3:
        image = pygame.image.load("..\Resources\Laps\lap_3.png")
    elif lap == 4:
        image = pygame.image.load("..\Resources\Laps\lap_4.png")
    elif lap == 5:
        image = pygame.image.load("..\Resources\Laps\lap_5.png")
    elif lap == 6:
        image = pygame.image.load("..\Resources\Laps\lap_6.png")
    elif lap == 7:
        image = pygame.image.load("..\Resources\Laps\lap_7.png")
    elif lap == 8:
        image = pygame.image.load("..\Resources\Laps\lap_8.png")
    elif lap == 9:
        image = pygame.image.load("..\Resources\Laps\lap_9.png")
    elif lap == 10:
        image = pygame.image.load("..\Resources\Laps\lap_10.png")
    else:
        image = pygame.image.load("..\Resources\Laps\lap_1.png")

    image = pygame.transform.scale(image, (50, 50))
    return image


def sort_pos(p_pos, one_pos, two_pos, three_pos):
    return 575, 375, 175, 0


def display_lap(pc, comp_1, comp_2, comp_3, player_x, comp_one_x, comp_two_x, comp_three_x):
    gameDisplay.blit(pc, (115, 0))
    gameDisplay.blit(comp_1, (300, 0))
    gameDisplay.blit(comp_2, (500, 0))
    gameDisplay.blit(comp_3, (700, 0))

    player_pos = 575
    comp_one_pos = 375
    comp_two_pos = 175
    comp_three_pos = 0

    player_pos, comp_one_pos, comp_two_pos, comp_three_pos = sort_pos(player_x, comp_one_x, comp_two_x, comp_three_x)

    # REPOSITION PLAYERS
    player_car(player_pos, 0)
    computer_one_car(comp_one_pos, 0)
    computer_two_car(comp_two_pos, 0)
    computer_three_car(comp_three_pos, 0)
    pass


def question_display(choice_1, choice_2, choice_3, choice_4):
    gameDisplay.blit(choice_1, (245, 625))
    gameDisplay.blit(choice_2, (380, 625))
    gameDisplay.blit(choice_3, (515, 625))
    gameDisplay.blit(choice_4, (650, 625))


# CARS SETUP
player_x = comp_1_x = comp_2_x = comp_3_x = 0
player_y = 150
comp_1_y = 250
comp_2_y = 350
comp_3_y = 450
player_x_change = comp_1_change = comp_2_change = comp_3_change = 0

# TRACK LAPS
player_laps = 1
comp_1_laps = 1
comp_2_laps = 1
comp_3_laps = 1

# QUESTION SETUP
option_1, option_2, option_3, option_4, answer, sound = questions.new_question()

correct = False

key = pygame.KEYUP
while not raceFinished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raceFinished = True

    if event.type == pygame.KEYDOWN:
        #if event.key == pygame.K_SPACE:
        if event.key == answer:
            player_x_change = randint(1, 20)
            comp_1_change = randint(1, 20)
            comp_2_change = randint(1, 20)
            comp_3_change = randint(1, 20)

        if event.key == pygame.K_LSHIFT:
            sound.play()

    if event.type == pygame.KEYUP:
        #if event.key == pygame.K_SPACE:
        if event.key == answer:
            player_x_change = comp_1_change = comp_2_change = comp_3_change = 0
            correct = True

    # ADJUST CAR POSITIONS
    player_x += player_x_change
    comp_1_x += comp_1_change
    comp_2_x += comp_2_change
    comp_3_x += comp_3_change

    # PREPARE DISPLAY

    gameDisplay.blit(background, (0, 95, display_width, display_height))
    player_lapImg = lap_tracker(player_laps)
    comp_1_lapImg = lap_tracker(comp_1_laps)
    comp_2_lapImg = lap_tracker(comp_2_laps)
    comp_3_lapImg = lap_tracker(comp_3_laps)
    display_lap(player_lapImg, comp_1_lapImg, comp_2_lapImg, comp_3_lapImg, player_x, comp_1_x, comp_2_x, comp_3_x)
    question_display(option_1, option_2, option_3, option_4)
    player_car(player_x, player_y)
    computer_one_car(comp_1_x, comp_1_y)
    computer_two_car(comp_2_x, comp_2_y)
    computer_three_car(comp_3_x, comp_3_y)
    play = pygame.image.load("..\Resources\Misc\play.png")
    gameDisplay.blit(play, (100, 675))
    pygame.display.update()
    clock.tick(60)


    if correct:
        option_1, option_2, option_3, option_4, answer, sound = questions.new_question()
        sound.play()
        correct = False

    # REPOSITION CARS IF NEEDED
    if player_x > display_width:
        player_x = -80
        player_laps += 1

    if comp_1_x > display_width:
        comp_1_x = -80
        comp_1_laps += 1

    if comp_2_x > display_width:
        comp_2_x = -80
        comp_2_laps += 1

    if comp_3_x > display_width:
        comp_3_x = -80
        comp_3_laps += 1


pygame.quit()
quit
