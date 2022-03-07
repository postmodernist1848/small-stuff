from random import *
import string

pwd_number = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль (пароли)? '))

if input('Включать ли в пароль цифры от 0 до 9? ').lower() == 'да':
    weight_dig = 0.15
else: 
    weight_dig = 0

if input('Включать ли в пароль прописные буквы? ').lower() == 'да':
    weight_uppercase = 0.3
else: 
    weight_uppercase = 0

if input('Включать ли в пароль строчные буквы? ').lower() == 'да':
    weight_lowercase = 0.5
else: 
    weight_lowercase = 0

if input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ').lower() == 'да':
    weight_punctuation = 0.15
else: 
    weight_punctuation = 0
    
def get_password():
    char = [''.join(choices([choice(string.digits), choice(string.ascii_lowercase), choice(string.ascii_uppercase), choice(string.punctuation)], \
    weights = (weight_dig, weight_lowercase, weight_uppercase, weight_punctuation), k = 1)) for _ in range(randint (9, 17))]
    return ''.join(char)

for _ in range(pwd_number):
    print(get_password())