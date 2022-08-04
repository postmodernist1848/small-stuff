#эта программа представляет собой реализацию незамысловатой игры 'угадай число'

import random
from os import system
print("Добро пожаловать в числовую угадайку")
while True:
    r_bound = input("Из сколько чисел угадываем?\nВведите число: ")
    if r_bound.isdigit():
        r_bound = int(r_bound)
        break
        
def is_valid(num):
    return num.isdigit() and r_bound >= int(num) >= 1


number = random.randint(1, r_bound)
flag = True
guesses = 0
print('Угадай число от 1 до', r_bound)
while flag:
    g = input("Введите число: ")
    if not is_valid(g):
        continue
    guesses += 1
    if int(g) < number:
        print("Искомое число больше")
    elif int(g) > number:
        print("Искомое число меньше")
    else:
        print("Вы угадали число, затратив", guesses, "попыток")
        guesses = 0
        if input("Начать новую игру? (Да/Нет) ").lower() != 'да':
            flag = False
            

