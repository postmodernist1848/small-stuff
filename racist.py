#русское поле экспериментов
'''
import matplotlib.pyplot as plt
'''
def binary_search(list, item): 
    low = 0
    high = len(list) - 1 
    tries = 0
    while low <= high:
        tries += 1
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return tries            
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def find_divisors(num):
    divisors = 0
    for j in range(1, num // 2 + 1):
        print(j)
        if num % j == 0:
            divisors += 1
    return divisors + 1

def first_number_with_n_divisors(n):
    for i in range(1, 300_000):
        print(i)
        divisors = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                divisors += 1
        if divisors + 1 == n:
            with open('divisors.txt', 'a') as output: 
                print(n, i, sep=': ', file=output)
                return i
    with open('divisors.txt', 'a') as output:
        print(n, 'not found in the first 300000', sep=': ', file=output)
    return 300_000

x_list = list(range(1, 101))

#y_list = [first_number_with_n_divisors(i) for i in x_list]
#print(y_list)

for i in range(32):
    divisors = find_divisors(2**i)
    with open('divisors.txt', 'a') as output:
        print(2**i, divisors, sep=': ', file=output)

'''
# plotting the points
plt.plot(x_list, y_list)
# naming the x axis
plt.xlabel('n')
# naming the y axis
plt.ylabel('Первое число с n делителей')
 
# giving a title to my graph
plt.title('график')
 
# function to show the plot
plt.show()


def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j], end = ' ')
    print()'''