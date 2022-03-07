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

my_list = range(1, 51)
y_list = [binary_search(my_list, i) for i in my_list]


print(sum(y_list)/len(y_list))
# plotting the points
plt.plot(my_list, y_list)
# naming the x axis
plt.xlabel('искомое число')
# naming the y axis
plt.ylabel('кол-во попыток')
 
# giving a title to my graph
plt.title('график')
 
# function to show the plot
plt.show()


def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j], end = ' ')
    print()