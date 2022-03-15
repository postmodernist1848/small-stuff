#inspired by Numberphile video in William Shanks
n = int(input('Ваше простое число: '))
digits_string = ''
remainder = 1
remainder_list = []
while remainder not in remainder_list:
    remainder_list.append(remainder)
    remainder *= 10 
    digit, remainder = divmod(remainder, n)
    digits_string += str(digit)
    
print(f'1/{n} имеет {len(digits_string)} знаков после запятой')
print(1 / n, '0.(' + digits_string + ')') 

'''from decimal import *
getcontext().prec = 99999
n = int(input('Ваше простое число (менее 100000): '))
print(str(1 / Decimal(n))[:20])'''