import os
import sys
import re
import math
import itertools
import tqdm

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

file = open("test-input-02-02.txt").read()
A = list(map(int, re.findall(r"[-0-9]+", file)))

print((-10) //5)

def add(X, Y):
    X1, Y1 = X
    X2, Y2 = Y
    return [X1 + X2, Y1 + Y2]

def multiply(X, Y):
    X1, Y1 = X
    X2, Y2 = Y
    return [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]

def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def divide(X, Y):
    X1, Y1 = X
    X2, Y2 = Y
    return [sign(X1) * (abs(X1) // X2), sign(Y1) * (abs(Y1) // Y2)]

print(A)
count = 0
Ax, Ay = A
for xd,yd in tqdm.tqdm(list(itertools.product(range(1001),range(1001)))):
    P = [Ax+xd,Ay+yd]
    result = [0,0]
    valid = True
    for _ in range(100):
        result = multiply(result,result)
        result = divide(result,[100000,100000])
        result = add(result,P)
        if any(abs(num)>1000000 for num in result):
            valid = False
            break
    if valid:
        count += 1

print(count)