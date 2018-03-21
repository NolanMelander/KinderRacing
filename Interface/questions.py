import pygame
import Interface.letters as letters
from random import randint


class QuestionLetter:
    def __init__(self):
        self.letter_one = self.letter_two = self.letter_three = self.letter_four = self.key = self.sound = 0
        self.letter_image_one = self.letter_image_two = self.letter_image_three = self.letter_image_four = 0
        self.ready = False
        self.create_question()
        self.set_answer()

    def create_question(self):

        self.letter_one = randint(0, 26)

        self.letter_two = randint(0, 26)

        while self.letter_two == self.letter_one:
            self.letter_two = randint(0, 26)

        self.letter_three = randint(0, 26)

        while self.letter_three == self.letter_one or self.letter_three == self.letter_two:
            self.letter_three = randint(0, 26)

        self.letter_four = randint(0, 26)

        while self.letter_four == self.letter_one or self.letter_four == self.letter_two \
                or self.letter_four == self.letter_three:
            self.letter_four = randint(0, 26)

    def set_answer(self):
        answer = randint(1, 4)
        self.get_key(answer)

    def get_key(self, answer):
        if answer == 1:
            self.set_question(self.letter_one)
        elif answer == 2:
            self.set_question(self.letter_two)
        elif answer == 3:
            self.set_question(self.letter_three)
        elif answer == 4:
            self.set_question(self.letter_four)

    def set_image(self):
        if 1 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 1:
                    self.letter_one = letters.set_letter_a()
                if self.letter_two == 1:
                    self.letter_two = letters.set_letter_a()
                if self.letter_three == 1:
                    self.letter_three = letters.set_letter_a()
                if self.letter_four == 1:
                    self.letter_four = letters.set_letter_a()

        if 2 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 2:
                    self.letter_one = letters.set_letter_b()
                if self.letter_two == 2:
                    self.letter_two = letters.set_letter_b()
                if self.letter_three == 2:
                    self.letter_three = letters.set_letter_b()
                if self.letter_four == 2:
                    self.letter_four = letters.set_letter_b()

        if 3 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 3:
                    self.letter_one = letters.set_letter_c()
                if self.letter_two == 3:
                    self.letter_two = letters.set_letter_c()
                if self.letter_three == 3:
                    self.letter_three = letters.set_letter_c()
                if self.letter_four == 3:
                    self.letter_four = letters.set_letter_c()

        if 4 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 4:
                    self.letter_one = letters.set_letter_d()
                if self.letter_two == 4:
                    self.letter_two = letters.set_letter_d()
                if self.letter_three == 4:
                    self.letter_three = letters.set_letter_d()
                if self.letter_four == 4:
                    self.letter_four = letters.set_letter_d()

        if 5 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 5:
                    self.letter_one = letters.set_letter_e()
                if self.letter_two == 5:
                    self.letter_two = letters.set_letter_e()
                if self.letter_three == 5:
                    self.letter_three = letters.set_letter_e()
                if self.letter_four == 5:
                    self.letter_four = letters.set_letter_e()

        if 6 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 6:
                    self.letter_one = letters.set_letter_f()
                if self.letter_two == 6:
                    self.letter_two = letters.set_letter_f()
                if self.letter_three == 6:
                    self.letter_three = letters.set_letter_f()
                if self.letter_four == 6:
                    self.letter_four = letters.set_letter_f()

        if 7 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 7:
                    self.letter_one = letters.set_letter_g()
                if self.letter_two == 7:
                    self.letter_two = letters.set_letter_g()
                if self.letter_three == 7:
                    self.letter_three = letters.set_letter_g()
                if self.letter_four == 7:
                    self.letter_four = letters.set_letter_g()

        if 8 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 8:
                    self.letter_one = letters.set_letter_h()
                if self.letter_two == 8:
                    self.letter_two = letters.set_letter_h()
                if self.letter_three == 8:
                    self.letter_three = letters.set_letter_h()
                if self.letter_four == 8:
                    self.letter_four = letters.set_letter_h()

        if 9 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 9:
                    self.letter_one = letters.set_letter_i()
                if self.letter_two == 9:
                    self.letter_two = letters.set_letter_i()
                if self.letter_three == 9:
                    self.letter_three = letters.set_letter_i()
                if self.letter_four == 9:
                    self.letter_four = letters.set_letter_i()

        if 10 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 10:
                    self.letter_one = letters.set_letter_j()
                if self.letter_two == 10:
                    self.letter_two = letters.set_letter_j()
                if self.letter_three == 10:
                    self.letter_three = letters.set_letter_j()
                if self.letter_four == 10:
                    self.letter_four = letters.set_letter_j()

        if 11 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 11:
                    self.letter_one = letters.set_letter_k()
                if self.letter_two == 11:
                    self.letter_two = letters.set_letter_k()
                if self.letter_three == 11:
                    self.letter_three = letters.set_letter_k()
                if self.letter_four == 11:
                    self.letter_four = letters.set_letter_k()

        if 12 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 12:
                    self.letter_one = letters.set_letter_l()
                if self.letter_two == 12:
                    self.letter_two = letters.set_letter_l()
                if self.letter_three == 12:
                    self.letter_three = letters.set_letter_l()
                if self.letter_four == 12:
                    self.letter_four = letters.set_letter_l()

        if 13 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 13:
                    self.letter_one = letters.set_letter_m()
                if self.letter_two == 13:
                    self.letter_two = letters.set_letter_m()
                if self.letter_three == 13:
                    self.letter_three = letters.set_letter_m()
                if self.letter_four == 13:
                    self.letter_four = letters.set_letter_m()

        if 14 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 14:
                    self.letter_one = letters.set_letter_n()
                if self.letter_two == 14:
                    self.letter_two = letters.set_letter_n()
                if self.letter_three == 14:
                    self.letter_three = letters.set_letter_n()
                if self.letter_four == 14:
                    self.letter_four = letters.set_letter_n()

        if 15 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 15:
                    self.letter_one = letters.set_letter_o()
                if self.letter_two == 15:
                    self.letter_two = letters.set_letter_o()
                if self.letter_three == 15:
                    self.letter_three = letters.set_letter_o()
                if self.letter_four == 15:
                    self.letter_four = letters.set_letter_o()

        if 16 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 16:
                    self.letter_one = letters.set_letter_p()
                if self.letter_two == 16:
                    self.letter_two = letters.set_letter_p()
                if self.letter_three == 16:
                    self.letter_three = letters.set_letter_p()
                if self.letter_four == 16:
                    self.letter_four = letters.set_letter_p()

        if 17 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 17:
                    self.letter_one = letters.set_letter_q()
                if self.letter_two == 17:
                    self.letter_two = letters.set_letter_q()
                if self.letter_three == 17:
                    self.letter_three = letters.set_letter_q()
                if self.letter_four == 17:
                    self.letter_four = letters.set_letter_q()

        if 18 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 18:
                    self.letter_one = letters.set_letter_r()
                if self.letter_two == 18:
                    self.letter_two = letters.set_letter_r()
                if self.letter_three == 18:
                    self.letter_three = letters.set_letter_r()
                if self.letter_four == 18:
                    self.letter_four = letters.set_letter_r()

        if 19 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 19:
                    self.letter_one = letters.set_letter_s()
                if self.letter_two == 19:
                    self.letter_two = letters.set_letter_s()
                if self.letter_three == 19:
                    self.letter_three = letters.set_letter_s()
                if self.letter_four == 19:
                    self.letter_four = letters.set_letter_s()

        if 20 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 20:
                    self.letter_one = letters.set_letter_t()
                if self.letter_two == 20:
                    self.letter_two = letters.set_letter_t()
                if self.letter_three == 20:
                    self.letter_three = letters.set_letter_t()
                if self.letter_four == 20:
                    self.letter_four = letters.set_letter_t()

        if 21 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 21:
                    self.letter_one = letters.set_letter_u()
                if self.letter_two == 21:
                    self.letter_two = letters.set_letter_u()
                if self.letter_three == 21:
                    self.letter_three = letters.set_letter_u()
                if self.letter_four == 21:
                    self.letter_four = letters.set_letter_u()

        if 22 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 22:
                    self.letter_one = letters.set_letter_v()
                if self.letter_two == 22:
                    self.letter_two = letters.set_letter_v()
                if self.letter_three == 22:
                    self.letter_three = letters.set_letter_v()
                if self.letter_four == 22:
                    self.letter_four = letters.set_letter_v()

        if 23 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 23:
                    self.letter_one = letters.set_letter_w()
                if self.letter_two == 23:
                    self.letter_two = letters.set_letter_w()
                if self.letter_three == 23:
                    self.letter_three = letters.set_letter_w()
                if self.letter_four == 23:
                    self.letter_four = letters.set_letter_w()

        if 24 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 24:
                    self.letter_one = letters.set_letter_x()
                if self.letter_two == 24:
                    self.letter_two = letters.set_letter_x()
                if self.letter_three == 24:
                    self.letter_three = letters.set_letter_x()
                if self.letter_four == 24:
                    self.letter_four = letters.set_letter_x()

        if 25 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 25:
                    self.letter_one = letters.set_letter_y()
                if self.letter_two == 25:
                    self.letter_two = letters.set_letter_y()
                if self.letter_three == 25:
                    self.letter_three = letters.set_letter_y()
                if self.letter_four == 25:
                    self.letter_four = letters.set_letter_y()

        if 26 in (self.letter_one, self.letter_two, self.letter_three, self.letter_four):
                if self.letter_one == 26:
                    self.letter_one = letters.set_letter_z()
                if self.letter_two == 26:
                    self.letter_two = letters.set_letter_z()
                if self.letter_three == 26:
                    self.letter_three = letters.set_letter_z()
                if self.letter_four == 26:
                    self.letter_four = letters.set_letter_z()

    def set_question(self, letter):
        if letter == 1:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\A.ogg")
            self.key = pygame.K_a
        if letter == 2:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\B.ogg")
            self.key = pygame.K_b
        if letter == 3:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\C.ogg")
            self.key = pygame.K_c
        if letter == 4:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\D.ogg")
            self.key = pygame.K_d
        if letter == 5:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\E.ogg")
            self.key = pygame.K_e
        if letter == 6:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\F.ogg")
            self.key = pygame.K_f
        if letter == 7:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\G.ogg")
            self.key = pygame.K_g
        if letter == 8:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\H.ogg")
            self.key = pygame.K_h
        if letter == 9:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\I.ogg")
            self.key = pygame.K_i
        if letter == 10:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\J.ogg")
            self.key = pygame.K_j
        if letter == 11:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\K.ogg")
            self.key = pygame.K_k
        if letter == 12:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\L.ogg")
            self.key = pygame.K_l
        if letter == 13:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\M.ogg")
            self.key = pygame.K_m
        if letter == 14:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\\N.ogg")
            self.key = pygame.K_n
        if letter == 15:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\O.ogg")
            self.key = pygame.K_o
        if letter == 16:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\P.ogg")
            self.key = pygame.K_p
        if letter == 17:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\Q.ogg")
            self.key = pygame.K_q
        if letter == 18:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\R.ogg")
            self.key = pygame.K_r
        if letter == 19:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\S.ogg")
            self.key = pygame.K_s
        if letter == 20:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\T.ogg")
            self.key = pygame.K_t
        if letter == 21:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\\U.ogg")
            self.key = pygame.K_u
        if letter == 22:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\V.ogg")
            self.key = pygame.K_v
        if letter == 23:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\W.ogg")
            self.key = pygame.K_w
        if letter == 24:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\X.ogg")
            self.key = pygame.K_x
        if letter == 25:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\Y.ogg")
            self.key = pygame.K_y
        if letter == 26:
            self.sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\Z.ogg")
            self.key = pygame.K_z

        self.set_image()
        self.ready = True

def new_question():
    question = randint(1, 26)
    if question == 1:
        return question_1()
    elif question == 2:
        return question_2()
    elif question == 3:
        return question_3()
    elif question == 4:
        return question_4()
    elif question == 5:
        return question_5()
    elif question == 6:
        return question_6()
    elif question == 7:
        return question_7()
    elif question == 8:
        return question_8()
    elif question == 9:
        return question_9()
    elif question == 10:
        return question_10()
    elif question == 11:
        return question_11()
    elif question == 12:
        return question_12()
    elif question == 13:
        return question_13()
    elif question == 14:
        return question_14()
    elif question == 15:
        return question_15()
    elif question == 16:
        return question_16()
    elif question == 17:
        return question_17()
    elif question == 18:
        return question_18()
    elif question == 19:
        return question_19()
    elif question == 20:
        return question_20()
    elif question == 21:
        return question_21()
    elif question == 22:
        return question_22()
    elif question == 23:
        return question_23()
    elif question == 24:
        return question_24()
    elif question == 25:
        return question_25()
    elif question == 26:
        return question_26()


def question_1():
    option_1 = letters.set_letter_w()
    option_2 = letters.set_letter_a()
    option_3 = letters.set_letter_t()
    option_4 = letters.set_letter_p()
    answer = pygame.K_a
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\A.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_2():
    option_1 = letters.set_letter_b()
    option_2 = letters.set_letter_r()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_g()
    answer = pygame.K_b
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\B.ogg")
    return option_1, option_2, option_3, option_4, answer, sound

def question_3():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_m()
    option_3 = letters.set_letter_c()
    option_4 = letters.set_letter_x()
    answer = pygame.K_c
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\C.ogg")
    return option_1, option_2, option_3, option_4, answer, sound

def question_4():
    option_1 = letters.set_letter_t()
    option_2 = letters.set_letter_k()
    option_3 = letters.set_letter_d()
    option_4 = letters.set_letter_c()
    answer = pygame.K_d
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\D.ogg")
    return option_1, option_2, option_3, option_4, answer, sound

def question_5():
    option_1 = letters.set_letter_e()
    option_2 = letters.set_letter_d()
    option_3 = letters.set_letter_f()
    option_4 = letters.set_letter_b()
    answer = pygame.K_e
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\E.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_6():
    option_1 = letters.set_letter_n()
    option_2 = letters.set_letter_i()
    option_3 = letters.set_letter_a()
    option_4 = letters.set_letter_f()
    answer = pygame.K_f
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\F.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_7():
    option_1 = letters.set_letter_r()
    option_2 = letters.set_letter_g()
    option_3 = letters.set_letter_n()
    option_4 = letters.set_letter_o()
    answer = pygame.K_g
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\G.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_8():
    option_1 = letters.set_letter_b()
    option_2 = letters.set_letter_x()
    option_3 = letters.set_letter_h()
    option_4 = letters.set_letter_a()
    answer = pygame.K_h
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\H.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_9():
    option_1 = letters.set_letter_i()
    option_2 = letters.set_letter_f()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_t()
    answer = pygame.K_i
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\I.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_10():
    option_1 = letters.set_letter_j()
    option_2 = letters.set_letter_y()
    option_3 = letters.set_letter_g()
    option_4 = letters.set_letter_q()
    answer = pygame.K_j
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\J.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_11():
    option_1 = letters.set_letter_t()
    option_2 = letters.set_letter_k()
    option_3 = letters.set_letter_j()
    option_4 = letters.set_letter_c()
    answer = pygame.K_k
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\K.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_12():
    option_1 = letters.set_letter_l()
    option_2 = letters.set_letter_v()
    option_3 = letters.set_letter_p()
    option_4 = letters.set_letter_i()
    answer = pygame.K_l
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\L.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_13():
    option_1 = letters.set_letter_g()
    option_2 = letters.set_letter_b()
    option_3 = letters.set_letter_c()
    option_4 = letters.set_letter_m()
    answer = pygame.K_m
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\M.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_14():
    option_1 = letters.set_letter_j()
    option_2 = letters.set_letter_g()
    option_3 = letters.set_letter_n()
    option_4 = letters.set_letter_x()
    answer = pygame.K_n
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\\N.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_15():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_u()
    option_3 = letters.set_letter_n()
    option_4 = letters.set_letter_y()
    answer = pygame.K_o
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\O.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_16():
    option_1 = letters.set_letter_p()
    option_2 = letters.set_letter_j()
    option_3 = letters.set_letter_t()
    option_4 = letters.set_letter_s()
    answer = pygame.K_p
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\P.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_17():
    option_1 = letters.set_letter_k()
    option_2 = letters.set_letter_q()
    option_3 = letters.set_letter_m()
    option_4 = letters.set_letter_b()
    answer = pygame.K_q
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\Q.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_18():
    option_1 = letters.set_letter_v()
    option_2 = letters.set_letter_a()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_r()
    answer = pygame.K_r
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\R.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_19():
    option_1 = letters.set_letter_y()
    option_2 = letters.set_letter_g()
    option_3 = letters.set_letter_s()
    option_4 = letters.set_letter_k()
    answer = pygame.K_s
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\S.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_20():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_r()
    option_3 = letters.set_letter_m()
    option_4 = letters.set_letter_t()
    answer = pygame.K_t
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\T.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_21():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_c()
    option_3 = letters.set_letter_u()
    option_4 = letters.set_letter_y()
    answer = pygame.K_u
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\\U.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_22():
    option_1 = letters.set_letter_b()
    option_2 = letters.set_letter_w()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_v()
    answer = pygame.K_v
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\V.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_23():
    option_1 = letters.set_letter_w()
    option_2 = letters.set_letter_v()
    option_3 = letters.set_letter_d()
    option_4 = letters.set_letter_c()
    answer = pygame.K_w
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\W.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_24():
    option_1 = letters.set_letter_x()
    option_2 = letters.set_letter_t()
    option_3 = letters.set_letter_h()
    option_4 = letters.set_letter_i()
    answer = pygame.K_x
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\X.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_25():
    option_1 = letters.set_letter_y()
    option_2 = letters.set_letter_w()
    option_3 = letters.set_letter_a()
    option_4 = letters.set_letter_t()
    answer = pygame.K_y
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\Y.ogg")
    return option_1, option_2, option_3, option_4, answer, sound


def question_26():
    option_1 = letters.set_letter_e()
    option_2 = letters.set_letter_z()
    option_3 = letters.set_letter_v()
    option_4 = letters.set_letter_k()
    answer = pygame.K_z
    sound = pygame.mixer.Sound("..\Resources\Sounds\Letters\Z.ogg")
    return option_1, option_2, option_3, option_4, answer, sound

