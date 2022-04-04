from time import time

ITERATIONS = 1_000 #50_000 in C
TEST_RANGE = 70


print("ULTIMATE POWER ALGOS TESTER (python version)")

#dumb algorithm

start = time()

for i in range(ITERATIONS):
    for a in range(TEST_RANGE):
        for b in range(TEST_RANGE):
            res = 1
            for _ in range(b):
                res *= a
        
print("1)dumb algo time:", (time() - start) * 50_000 / ITERATIONS, "s")

#smart algorithm

start = time()

for i in range(ITERATIONS):
    for a in range(TEST_RANGE):
        for b in range(TEST_RANGE):
            res = 1
            k = b
            n = a
            while k > 1:
                if k % 2 == 0:
                    n *= n
                    k /= 2
                else:
                    res = res * n
                    k -= 1
                
print("2)smart algo time:", (time() - start) * 50_000 / ITERATIONS, "s")

#** operator

start = time()

for i in range(ITERATIONS):
    for a in range(TEST_RANGE):
        for b in range(TEST_RANGE):
            res = a**b
        
print("3)** operator time:", (time() - start) * 50_000 / ITERATIONS, "s")

#pow() function

start = time()

for i in range(ITERATIONS):
    for a in range(TEST_RANGE):
        for b in range(TEST_RANGE):
            res = pow(a, b)
        
print("4)pow() operator time:", (time() - start) * 50_000 / ITERATIONS, "s")
'''
print("My data")
print(f"1)dumb algo time: {1026.8456101417542/ 23.179} times slower than C",
f"2)smart algo time: {528.121292591095/ 4.156} times slower than C",
f"3)** operator time: {102.81320810317993/ 3.744} times slower than C",
f"4)pow() operator time: {108.95001888275146/ 3.744} times slower than C", sep='\n')'''