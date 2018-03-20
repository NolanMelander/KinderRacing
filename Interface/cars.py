import pygame

display_width = 800
display_height = 800


# CAR CLASS
class Racecar:
    def __init__(self, picture, lap, x, y):
        self.picture = picture
        self.dist_traveled = 0
        self.lap = lap
        self.x = x
        self.y = y

    def set_lap(self):
        if self.x > display_width:
            self.x = -80
            self.lap += 1




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

topMenu = pygame.image.load('..\Resources\Cars\\rc_orange.png')
topMenu = pygame.transform.scale(topMenu, (200, 600))
topMenu = pygame.transform.rotate(topMenu, 90)


bottomMenu = pygame.image.load('..\Resources\Cars\\rc_red.png')
bottomMenu = pygame.transform.scale(bottomMenu, (200, 600))
bottomMenu = pygame.transform.rotate(bottomMenu, 90)
