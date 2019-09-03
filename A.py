from time import sleep
from copy import deepcopy
from random import randint
from os import system


N = 30  # размер поля
wait = 1  # время смены фазы в секундах

def clear():  # очистка экрана
    system('cls')


def check(i, j):  # проверка клетки на принадлежность полю
    return 0 <= i < N and 0 <= j < N


def cnt(i, j, x):  # подсчет количества для данной клетки соседей рыб и креветок
    k = 0
    p = 0
    for sh1 in range(-1, 2):
        for sh2 in range(-1, 2):
            if check(i + sh1, j + sh2) and not(sh1 == 0 and sh2 == 0):
                k += ('K' == x[i + sh1][j + sh2])
                p += ('P' == x[i + sh1][j + sh2])
    return [k, p]


def out(x):  # вывод поля
    ous = ''
    for i in range(len(x)):
        for j in range(len(x)):
            ous += str(x[i][j] + ' ')
        ous += '\n'
    print(ous, end='')


def gen(x):  # генерация исходного поля с помощью рандома
    for i in range(len(x)):
        for j in range(len(x)):
            rnd = randint(1, 10)
            if rnd <= 2:
                x[i][j] = 'P'
            elif 2 < rnd <= 4:
                x[i][j] = 'K'
            elif 4 < rnd <= 5:
                x[i][j] = 'C'


a = [['~' for i in range(N)] for j in range(N)]  # объявление поля
gen(a)
anew = deepcopy(a)

while True:  # повторение процесса
    out(a)
    sleep(wait)
    clear()
    for i in range(N):  # заполнение следующей фазы по правилам
        for j in range(N):
            c = cnt(i, j, a)
            if a[i][j] == '~' and c[1] == 3:
                anew[i][j] = 'P'
            elif a[i][j] == '~' and c[0] == 3:
                anew[i][j] = 'K'
            elif a[i][j] == 'P' and (c[1] >= 4 or c[1] < 2):
                anew[i][j] = '~'
            elif a[i][j] == 'K' and (c[0] >= 4 or c[0] < 2):
                anew[i][j] = '~'
    a = deepcopy(anew)