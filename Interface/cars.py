import pygame

display_width = 800
display_height = 800


# CAR CLASS
class Racecar:
    def __init__(self, picture, lap, x, y, pos, lap_pos):
        self.picture = picture
        self.dist_traveled = 0
        self.lap = lap
        self.x = x
        self.y = y
        self.pos = pos
        self.lap_pos = lap_pos

    def set_lap(self):
        if self.x > display_width:
            self.x = -80
            self.lap += 1

    def set_pos(self, car_one, car_two, car_three):
        ahead = 0
        if self.dist_traveled > car_one:
            ahead += 1

        if self.dist_traveled > car_two:
            ahead += 1

        if self.dist_traveled > car_three:
            ahead += 1

        if ahead == 3:
            self.pos = 575
            self.lap_pos = 700
        elif ahead == 2:
            self.pos = 375
            self.lap_pos = 500
        elif ahead == 1:
            self.pos = 175
            self.lap_pos = 300
        else:
            self.pos = 0
            self.lap_pos = 115


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
