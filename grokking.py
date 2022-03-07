import random

def bogosort(array):
    while True:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
        if sorted:
            return array
        else:
            random.shuffle(array)
    
def quicksort(array:list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        array.remove(pivot)
        less = [i for i in array if i <= pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater) 

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return 'Not sorted!'
    return 'Sorted!'

my_list = [random.randint(1, 10000) for _ in range(100000000)]
sorted_list = quicksort(my_list)

print('original list:', is_sorted(my_list))
print('sorted list:', is_sorted(sorted_list))
