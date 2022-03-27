#stupid one-liners for stepik tasks
# делители-1 #
print(*reversed(max([(sum(j for j in range(1, i + 1) if i % j == 0), i) for i in range(int(input()), int(input()) + 1)]))) 
# ревью кода-4 #
(lambda x: print(max(x) if x else 'NO'))(list((int(i) for i in input() if int(i) % 3 == 0)))
# делители-2
[((print(i, end = ""), [print("+", end = "") for j in range(1, i + 1) if i % j == 0], print())) for i in range(1, int(input()) + 1)]
# микшер цветов 
(lambda c: print('оранжевый' if c == ['желтый', 'красный'] else 'фиолетовый' if c == ['красный', 'синий'] else 'зеленый' if c == ['желтый', 'синий'] else c[0] if c[0] in ['красный', 'желтый', 'синий'] and c[0] == c[1] else 'ошибка цвета'))(sorted([input(), input()])) 
#k-ая буква слова
[[print(x[k], end='') for x in lst if len(x) >= k + 1] for lst, k in [([input() for _ in range(int(input()))], int(input()) - 1)]]
#Google-search-2
(lambda data, querries: print(*[s for s in data if all([q.lower() in s.lower() for q in querries])], sep='\n'))([input() for _ in range(int(input()))], [input() for _ in range(int(input()))])
