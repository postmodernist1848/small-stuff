#эта программа позволяет шифровать (и расшифровывать) русский или английский текст шифром Цезаря и шифром Виженера

import string
def caesar_cipher(text:str, k:int) -> str:    
    '''cipher (decipher) a string in caesar cipher'''
    s = ''
    i = 0
    while not text[i].isalpha():
        i += 1
        if i >= len(text):
            return text
    else:
        if 1040 <= ord(text[i]) <= 1104:
            alpha = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
        else:
            alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    len_alpha = len(alpha) // 2    
    for c in text:
        if c.isalpha():
            pos = alpha.find(c) 
            s += alpha[(pos + k) % len_alpha + len_alpha * c.islower()]
        else:
            s += c
    return(s)

def vigenere_cipher(text:str, keyword:str) -> str:
    '''cipher (decipher) a string in vigenere cipher'''
    s = ''
    i = 0
    while not text[i].isalpha():
        if not keyword.isalpha():
            raise ValueError("Keyword is supposed to be a string of characters of English or Russian alphabet.")
        else:
            keyword = keyword.casefold()
        i += 1
        if i >= len(text):
            return text
    else:
        if 1040 <= ord(text[i]) <= 1104:
            alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'  
        else:
            alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    len_alpha = len(alpha) // 2
    letter_count = 0
    for c in text:
        if c.isalpha():
            keyword_pos = alpha[len_alpha:].find(keyword[letter_count % len(keyword)])
            text_pos = alpha.find(c)
            s += alpha[(text_pos + keyword_pos) % len_alpha + len_alpha * c.islower()]
            letter_count += 1
        else:
            s += c
    return s

sdfasdf
if __name__ == "__main__":
    print(vigenere_cipher(input("Шифруемый текст: "), input("Ключевое слово: ")))

