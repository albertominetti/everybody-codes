import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

file = open("input-01-03.txt").read().split("\n")

names = file[0].split(',')
moves = file[2].split(',')

print(names)
print(moves)

instr = []
for m in moves:
    instr.append(int(m.replace('L', '-').replace('R', '+')))

print(instr)

for i in instr:
    i = i % len(names)
    names[0], names[i] = names[i], names[0]

print(names[0])