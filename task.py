from itertools import permutations, combinations, product

def tx():
    count = 0
    for tup in set(permutations('АВРОРА')):
        word = ''.join(tup)
        count += word.count('АА') + word.count('РР') == 0
    return count

def t185():
    count = 0
    for i1 in range(5, 10):
        for i2 in range(4, i1):
            for i3 in range(3, i2):
                for i4 in range(2, i3):
                    for i5 in range(1, i4):
                        for i6 in range(i5):
                            if i1 % 2 == i3 % 2 == i5 % 2 and \
                                    i2 % 2 == i4 % 2 == i6 % 2 and \
                                    i1 % 2 != i2 % 2:
                                        print(i1, i2, i3, i4, i5, i6, sep='')
                                        count += 1
    return count

def t187():
    count = 0
    for word in set(product('БАНКИР', repeat=6)):
        if word.count('И') <= 1 and word.count('A') <= 1:
            count += 1
    return count

def t190():
    count = 0
    for word in set(product('КАЛЬКА', repeat=6)):
        if word.count('A') <= 1:
            count += 1
    return count

def t195():
    def conscount(word):
        return word.count('П') + word.count('С')
    count = 0
    for k in range(3, 8):
        for word in set(product('СЕПИЯ', repeat=k)):
            if word.count('E') <= 2 and word.count('И') <= 2 and word.count('Я') <= 2 and ((word[0] in 'ПС' and conscount(word) == 1) or (conscount(word) == 0)):
                count += 1
    return count

def t230():
    count = 0
    digits = '012345678'
    pairs = [c + c for c in digits]
    for num in map(''.join, product(digits, repeat=7)):
        if num[0] not in '037' and not any([pair in num for pair in pairs]):
            count+=1
    return count

def t233():
    count = 0
    digits = '012345678'
    threes = [c + c + c for c in digits]
    for num in map(''.join, product(digits, repeat=7)):
        if num[0] not in '0246' and num[-3:] not in threes:
            count+=1
    return count

def t236():

    count = 0
    for word in map(''.join, set(permutations('АВТОРОТА'))):
        valid = True
        for i in range(len(word) - 1):
            if (word[i] in 'ОА') == (word[i + 1] in 'ОА'):
                valid = False
        count += valid
    return count

def t241():
    count = 0
    for word in map(''.join, set(permutations('АММИАКАТ'))):
        valid = False
        for i in range(len(word) - 1):
            if (word[i] in 'ИА') == (word[i + 1] in 'ИА'):
                valid = True
                break
        count += valid
    return count

def t245():
    count = 0
    for word in map(''.join, set(permutations('ПРЕПАРАТ'))):
        valid = False
        for i in range(len(word) - 1):
            if (word[i] in 'ИА') == (word[i + 1] in 'ИА'):
                valid = True
                break
        count += valid
    return count

def t263():
    count = 0
    digits = '012345678'
    for num in map(''.join, product(digits, repeat=5)):
        if num[0] in '2468' and num[-1] not in '18' and num.count('3') <= 1:
            count += 1
    return count

def main():
    print(t230())
    print(t233())
    print(t263())

if __name__ == '__main__':
    main()
