#problem 1
'''total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)'''
#problem 2
'''total = 0
f1, f2 = 1, 1
while f1 <= 4_000_000:
    if f1 % 2 == 0:
        total += f1
    f1, f2 = f2, f1 + f2
print(total)'''
#problem 3
'''def is_prime(num):
    for i in range(2, int(num**(1/2)) + 2):
        if num % i == 0:
            return False
    return True

def factorize(num):
    if is_prime(num):
        return [num]
    else:
        for i in range(2, num):
            if num % i == 0:
                return [i, *factorize(num // i)]

print(max(factorize(600851475143)))'''
#problem 4
'''for i in range(100, 1000):
    for j in range(i, 1000):
        prod = str(i * j)
        if prod[::-1] == prod:
            print(prod)
'''
#problem 5
'''i = 2520 
while True:
    found = True
    for j in range(1, 21):
        if i % j != 0:
            found = False
            break
    if found:
        print(i)
    i += 1'''
#problem 6
print(sum(range(101))**2 - sum([i**2 for i in range(1, 101)]))
