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
engine = pygame.mixer.Sound("..\Resources\Sounds\misc\engine.ogg")
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


def display_lap(pc, comp_1, comp_2, comp_3, car_one, car_two, car_three, car_four):
    gameDisplay.blit(pc, (car_one.lap_pos, 0))
    gameDisplay.blit(comp_1, (car_two.lap_pos, 0))
    gameDisplay.blit(comp_2, (car_three.lap_pos, 0))
    gameDisplay.blit(comp_3, (car_four.lap_pos, 0))

    car_one.set_pos(car_two.dist_traveled, car_three.dist_traveled, car_four.dist_traveled)
    car_two.set_pos(car_one.dist_traveled, car_three.dist_traveled, car_four.dist_traveled)
    car_three.set_pos(car_one.dist_traveled, car_two.dist_traveled, car_four.dist_traveled)
    car_four.set_pos(car_one.dist_traveled, car_two.dist_traveled, car_three.dist_traveled)

    # REPOSITION PLAYERS
    player_car(car_one.pos, 0)
    computer_one_car(car_two.pos, 0)
    computer_two_car(car_three.pos, 0)
    computer_three_car(car_four.pos, 0)
    pass


def question_display(choice_1, choice_2, choice_3, choice_4):
    gameDisplay.blit(choice_1, (245, 625))
    gameDisplay.blit(choice_2, (380, 625))
    gameDisplay.blit(choice_3, (515, 625))
    gameDisplay.blit(choice_4, (650, 625))


def game_start():

    #CAR OBJECTS
    car_one = cars.Racecar(cars.player, 1, 0, 150, 575, 700)
    car_two = cars.Racecar(cars.computer_one, 1, 0, 250, 375, 500)
    car_three = cars.Racecar(cars.computer_two, 1, 0, 350, 175, 300)
    car_four = cars.Racecar(cars.computer_three, 1, 0, 450, 0, 115)

    # CARS SETUP
    player_x_change = comp_1_change = comp_2_change = comp_3_change = 0

    # QUESTION SETUP
    #option_1, option_2, option_3, option_4, answer, sound = questions.new_question()
    currentQuestion = questions.QuestionLetter()
    currentQuestion.sound.play()
    correct = False
    raceFinished = False

    while not raceFinished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raceFinished = True

            if event.type == pygame.KEYDOWN:
                if event.key == currentQuestion.key:
                    player_x_change = randint(1, 20)
                    comp_1_change = randint(1, 20)
                    comp_2_change = randint(1, 20)
                    comp_3_change = randint(1, 20)

                if event.key == pygame.K_LSHIFT:
                    currentQuestion.sound.play()

            if event.type == pygame.KEYUP:
                if event.key == currentQuestion.key:
                    player_x_change = comp_1_change = comp_2_change = comp_3_change = 0
                    correct = True

        car_one.x += player_x_change
        car_two.x += comp_1_change
        car_three.x += comp_2_change
        car_four.x += comp_3_change

        car_one.dist_traveled += player_x_change
        car_two.dist_traveled += comp_1_change
        car_three.dist_traveled += comp_2_change
        car_four.dist_traveled += comp_3_change

        # PREPARE DISPLAY
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(background, (0, 95, display_width, display_height))
        player_lapImg = lap_tracker(car_one.lap)
        comp_1_lapImg = lap_tracker(car_two.lap)
        comp_2_lapImg = lap_tracker(car_three.lap)
        comp_3_lapImg = lap_tracker(car_four.lap)
        display_lap(player_lapImg, comp_1_lapImg, comp_2_lapImg, comp_3_lapImg, car_one, car_two, car_three, car_four)
        displayQuestion = False
        while not displayQuestion:
            if currentQuestion.ready:
                question_display(currentQuestion.letter_one, currentQuestion.letter_two, currentQuestion.letter_three,
                                 currentQuestion.letter_four)
                displayQuestion = True

        player_car(car_one.x, car_one.y)
        computer_one_car(car_two.x, car_two.y)
        computer_two_car(car_three.x, car_three.y)
        computer_three_car(car_four.x, car_four.y)
        play = pygame.image.load("..\Resources\Misc\play.png")
        gameDisplay.blit(play, (100, 675))
        pygame.display.update()
        clock.tick(60)

        if correct:
            #option_1, option_2, option_3, option_4, answer, sound = questions.new_question()
            currentQuestion = questions.QuestionLetter()
            engine.play(maxtime=3000)
            currentQuestion.sound.play()
            correct = False

        car_one.set_lap()
        car_two.set_lap()
        car_three.set_lap()
        car_four.set_lap()


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def game_menu():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill((0, 0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Kinder Racing", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(cars.topMenu, (display_width/6, 150))
        gameDisplay.blit(cars.bottomMenu, (display_width/6, 500))

        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        start = pygame.image.load("..\Resources\Misc\play.png")
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            gameDisplay.blit(start, (150, 450))
            pygame.draw.rect(gameDisplay, (200, 0, 0), (550, 450, 100, 50))
            if clicked[0] == 1:
                gameDisplay.fill((0, 0, 0))
                game_start()
        elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, (250, 0, 0), (550, 450, 100, 50))
            gameDisplay.blit(start, (150, 450))
            if clicked[0] == 1:
                pygame.quit()
                quit()
        else:
            gameDisplay.blit(start, (150, 450))
            pygame.draw.rect(gameDisplay, (200, 0, 0), (550, 450, 100, 50))

        quitText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects("Quit", quitText)
        textRect.center = ((550 + (100/2)), (450+(50/2)))
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


game_menu()

