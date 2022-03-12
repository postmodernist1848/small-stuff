#русское поле экспериментов

import matplotlib.pyplot as plt

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

import math
def assss(n):
    total = 0
    for i in range(1, n+1):
        total += i**(-1)
    return (round(total - math.log(n), 3))

x_list = range(1, 40000)

y_list = [assss(i) for i in x_list]



# plotting the points
plt.plot(x_list, y_list)
# naming the x axis
plt.xlabel('n')
# naming the y axis
plt.ylabel('"асимптотическое приближение"')
 
# giving a title to my graph
plt.title('график')
 
# function to show the plot
plt.show()


def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j], end = ' ')
    print()