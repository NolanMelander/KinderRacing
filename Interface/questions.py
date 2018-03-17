import pygame
import Interface.letters as letters
from random import randint

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
    return option_1, option_2, option_3, option_4, answer


def question_2():
    option_1 = letters.set_letter_b()
    option_2 = letters.set_letter_r()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_g()
    answer = pygame.K_b
    return option_1, option_2, option_3, option_4, answer


def question_3():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_m()
    option_3 = letters.set_letter_c()
    option_4 = letters.set_letter_x()
    answer = pygame.K_c
    return option_1, option_2, option_3, option_4, answer


def question_4():
    option_1 = letters.set_letter_t()
    option_2 = letters.set_letter_k()
    option_3 = letters.set_letter_d()
    option_4 = letters.set_letter_c()
    answer = pygame.K_d
    return option_1, option_2, option_3, option_4, answer


def question_5():
    option_1 = letters.set_letter_e()
    option_2 = letters.set_letter_d()
    option_3 = letters.set_letter_f()
    option_4 = letters.set_letter_b()
    answer = pygame.K_e
    return option_1, option_2, option_3, option_4, answer


def question_6():
    option_1 = letters.set_letter_n()
    option_2 = letters.set_letter_i()
    option_3 = letters.set_letter_a()
    option_4 = letters.set_letter_f()
    answer = pygame.K_f
    return option_1, option_2, option_3, option_4, answer


def question_7():
    option_1 = letters.set_letter_r()
    option_2 = letters.set_letter_g()
    option_3 = letters.set_letter_n()
    option_4 = letters.set_letter_o()
    answer = pygame.K_g
    return option_1, option_2, option_3, option_4, answer


def question_8():
    option_1 = letters.set_letter_b()
    option_2 = letters.set_letter_x()
    option_3 = letters.set_letter_h()
    option_4 = letters.set_letter_a()
    answer = pygame.K_h
    return option_1, option_2, option_3, option_4, answer


def question_9():
    option_1 = letters.set_letter_i()
    option_2 = letters.set_letter_f()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_t()
    answer = pygame.K_i
    return option_1, option_2, option_3, option_4, answer


def question_10():
    option_1 = letters.set_letter_j()
    option_2 = letters.set_letter_y()
    option_3 = letters.set_letter_g()
    option_4 = letters.set_letter_q()
    answer = pygame.K_j
    return option_1, option_2, option_3, option_4, answer


def question_11():
    option_1 = letters.set_letter_t()
    option_2 = letters.set_letter_k()
    option_3 = letters.set_letter_j()
    option_4 = letters.set_letter_c()
    answer = pygame.K_k
    return option_1, option_2, option_3, option_4, answer


def question_12():
    option_1 = letters.set_letter_l()
    option_2 = letters.set_letter_v()
    option_3 = letters.set_letter_p()
    option_4 = letters.set_letter_i()
    answer = pygame.K_l
    return option_1, option_2, option_3, option_4, answer


def question_13():
    option_1 = letters.set_letter_g()
    option_2 = letters.set_letter_b()
    option_3 = letters.set_letter_c()
    option_4 = letters.set_letter_m()
    answer = pygame.K_m
    return option_1, option_2, option_3, option_4, answer


def question_14():
    option_1 = letters.set_letter_j()
    option_2 = letters.set_letter_g()
    option_3 = letters.set_letter_n()
    option_4 = letters.set_letter_x()
    answer = pygame.K_n
    return option_1, option_2, option_3, option_4, answer


def question_15():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_u()
    option_3 = letters.set_letter_n()
    option_4 = letters.set_letter_y()
    answer = pygame.K_o
    return option_1, option_2, option_3, option_4, answer


def question_16():
    option_1 = letters.set_letter_p()
    option_2 = letters.set_letter_j()
    option_3 = letters.set_letter_t()
    option_4 = letters.set_letter_s()
    answer = pygame.K_p
    return option_1, option_2, option_3, option_4, answer


def question_17():
    option_1 = letters.set_letter_k()
    option_2 = letters.set_letter_q()
    option_3 = letters.set_letter_m()
    option_4 = letters.set_letter_b()
    answer = pygame.K_q
    return option_1, option_2, option_3, option_4, answer


def question_18():
    option_1 = letters.set_letter_v()
    option_2 = letters.set_letter_a()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_r()
    answer = pygame.K_r
    return option_1, option_2, option_3, option_4, answer


def question_19():
    option_1 = letters.set_letter_y()
    option_2 = letters.set_letter_g()
    option_3 = letters.set_letter_s()
    option_4 = letters.set_letter_k()
    answer = pygame.K_s
    return option_1, option_2, option_3, option_4, answer


def question_20():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_r()
    option_3 = letters.set_letter_m()
    option_4 = letters.set_letter_t()
    answer = pygame.K_t
    return option_1, option_2, option_3, option_4, answer


def question_21():
    option_1 = letters.set_letter_o()
    option_2 = letters.set_letter_c()
    option_3 = letters.set_letter_u()
    option_4 = letters.set_letter_y()
    answer = pygame.K_u
    return option_1, option_2, option_3, option_4, answer


def question_22():
    option_1 = letters.set_letter_b()
    option_2 = letters.set_letter_w()
    option_3 = letters.set_letter_q()
    option_4 = letters.set_letter_v()
    answer = pygame.K_v
    return option_1, option_2, option_3, option_4, answer


def question_23():
    option_1 = letters.set_letter_w()
    option_2 = letters.set_letter_v()
    option_3 = letters.set_letter_d()
    option_4 = letters.set_letter_c()
    answer = pygame.K_w
    return option_1, option_2, option_3, option_4, answer


def question_24():
    option_1 = letters.set_letter_x()
    option_2 = letters.set_letter_t()
    option_3 = letters.set_letter_h()
    option_4 = letters.set_letter_i()
    answer = pygame.K_x
    return option_1, option_2, option_3, option_4, answer


def question_25():
    option_1 = letters.set_letter_y()
    option_2 = letters.set_letter_w()
    option_3 = letters.set_letter_a()
    option_4 = letters.set_letter_t()
    answer = pygame.K_y
    return option_1, option_2, option_3, option_4, answer


def question_26():
    option_1 = letters.set_letter_e()
    option_2 = letters.set_letter_z()
    option_3 = letters.set_letter_v()
    option_4 = letters.set_letter_k()
    answer = pygame.K_z
    return option_1, option_2, option_3, option_4, answer


