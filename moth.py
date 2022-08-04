







from PIL import Image                                                                                
#this is just a meme module

def wings(moth_part):
    if moth_part == 'right':
        return 'o/'
    elif moth_part == 'left':
        try:
            img = Image.open('stalin.jpg')
        except FileNotFoundError:
            raise FileNotFoundError("'stalin.jpg' not found in moth.py location. Please put stalin.jpg in the directory.")
        img.show() 
        return ''

def int(*args, **kwargs):
    print('А хуй тебе!')

def factorial(n):
    if n <= 1: 
        #base case
        return 1
    else:
        #recursive case
        return n * factorial(n - 1) 

print(factorial(10))


memo_fib = {1: 1, 2: 1}
def fib(n):
    try:
        if n in memo_fib:
            return memo_fib[n]
    except NameError:
        raise NameError("'memo_fib' not found. To use moth fib function tou need to import memo_fib from moth")

    else:
        f1, f2 = fib(n - 1), fib(n - 2)
        memo_fib[n-1] = f1
        memo_fib[n-2] = f2
        return f1 + f2
