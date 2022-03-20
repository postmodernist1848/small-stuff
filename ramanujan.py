#very simple search for ramanujan numbers, probably very uboptimized
upper_bound = 40
l = set()
for a in range(1, upper_bound):
    for b in range(1, upper_bound):
        for c in range(a + 1, upper_bound):
            for d in range(b + 1, upper_bound):
                if a**3 + c**3 == b**3 + d**3 and d != a != b and b != c != d:
                    l.add(a**3 + c**3)
                    #print(f'{a**3 + c**3} = {a}^3 + {c}^3 = {b}^3 + {d}^3')
print(*sorted(l))