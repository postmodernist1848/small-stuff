# эта программа позволяет переводить числа в десятичную систему счисления и наоборот

def decimal_to_base(num, base):
    digits = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWZXYZ')
    num = int(num)
    s = ''
    while num > 0:
        s += digits[num % base]
        num = num // base
    return s[::-1]


flag = True
while flag:
    ans = input('1 - перевести в десятичную | 2 - перевести из десятичной: ')
    if ans == '1':
        flag = False
        while True:
            print(int(input('Введите число: '), int(input('Введите основание: '))))
            if input('Еще? (Да/нет) ').lower() != 'да':
                break

    elif ans == '2':
        flag = False
        while True:
            print(decimal_to_base(input('Введите число: '), int(input('Введите основание: '))))
            if input('Еще? (Да/нет) ').lower() != 'да':
                    break
    
    else:
        print('Ошибка #1: неверный ввод при выборе действия')
        