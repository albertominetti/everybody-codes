import os
import sys
import re
import math

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

file = open("test-input-02-01.txt").read()
print(file)

A = list(map(int, re.findall(r"[0-9]+", file)))

print(A)

def add(X, Y):
    X1, Y1 = X
    X2, Y2 = Y
    return [X1 + X2, Y1 + Y2]

def multiply(X, Y):
    X1, Y1 = X
    X2, Y2 = Y
    return [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]

def divide(X, Y):
    X1, Y1 = X
    X2, Y2 = Y
    return [math.floor(X1 / X2), math.floor(Y1 / Y2)]


print(add([1,1],[2,2]))

R = [0,0]
for _ in range(3):
    R = multiply(R, R)
    R = divide(R, [10,10])
    R = add(R, A)

print(R)