#эта программа позволяет шифровать (и расшифровывать) русский или английский текст шифром Цезаря


import string
def caesar(text, k):    
    s = ''
    
    if 1040 <= ord(text[0]) <= 1104:
        alpha = ''.join([chr(i) for i in range(1040, 1105)])  
    else:
        alpha = string.ascii_letters
    len_alpha = len(alpha) // 2    
    for c in text:
        if c.isalpha():
            pos = alpha.find(c) 
            s += alpha[(pos + k) % len_alpha + len_alpha * (pos // len_alpha)]
        else:
            s += c
    return(s)

print(caesar(input('Шифруемый текст: '), int(input('Сдвиг: '))))    
'''words = input().split()
for e in words:
    print(caesar(e, len([c for c in e if c.isalpha()])), end = ' ')'''
