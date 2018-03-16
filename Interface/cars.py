import pygame

# PLAYER CAR
player = pygame.image.load('..\Resources\Cars\\rc_orange.png')
player = pygame.transform.scale(player, (80, 100))
player = pygame.transform.rotate(player, 90)

computer_one = pygame.image.load('..\Resources\Cars\\rc_black.png')
computer_one = pygame.transform.scale(computer_one, (80, 100))
computer_one = pygame.transform.rotate(computer_one, 90)

computer_two = pygame.image.load('..\Resources\Cars\\rc_red.png')
computer_two = pygame.transform.scale(computer_two, (80, 100))
computer_two = pygame.transform.rotate(computer_two, 90)

computer_three = pygame.image.load('..\Resources\Cars\\rc_white.png')
computer_three = pygame.transform.scale(computer_three, (80, 100))
computer_three = pygame.transform.rotate(computer_three, 90)