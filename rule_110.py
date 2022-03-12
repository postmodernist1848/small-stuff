#попытка реализации правила 110 - одномерного клеточного автоматона, не особо понял, как это должно работать

import time

states = {'***':' ', 
          '** ':'*',
          '* *':'*', 
          '*  ':' ', 
          ' **':' ', 
          ' * ':'*',
          '  *':'*',
          '   ':' '}
def compute_next_gen(gen):
    next_gen = ''
    for i in range(0, len(gen)):
        next_gen += states[gen[i - 1] + gen[i] + gen[(i + 1) % len(gen)]]
    return next_gen

gen = '                                                                  *'
print(gen)
while True:
    time.sleep(0.5)
    gen = compute_next_gen(gen)
    print(gen)
    
    

    
