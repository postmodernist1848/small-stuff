def pascal(n):
    if n == 1:
        return [1]
    else:
        prev = pascal(n - 1)
        return [1] + [prev[i] + prev[i+1] for i in range(len(prev) - 1)] + [1] 

for i in range(1, 20):
    print(pascal(i))