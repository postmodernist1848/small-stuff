from PIL import Image                                                                                
#this is just a meme module

def wings(moth_part):
    if moth_part == 'right':
        return 'o/'
    elif moth_part == 'left':
        img = Image.open('stalin.jpg')
        img.show() 
        return ''

def int(*args, **kwargs):
    print('А хуй тебе!')

def fc(n):
    if n == 1: #base case
        return 1
    else:
        return n * fc(n - 1) #recursive case


def fib(n):
    if n in memo:
        return memo[n]
    else:
        f1, f2 = fib(n - 1), fib(n - 2)
        memo[n-1] = f1
        memo[n-2] = f2
        return f1 + f2
if __name__ == "__main__":        
    memo = {1: 1, 2: 1}
    print(*map(lambda x: fib(x), range(1, 100)))