import os, sys, re, math, itertools, tqdm
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def part1():
    with open("input-06-01.txt") as input_file:
        content = input_file.read()
    # content = "ABabACacBCbca"
    mentors = 0
    pairs = 0
    for c in content:
        if c == "A":
            mentors += 1
        elif c == "a":
            pairs += mentors
    print(pairs)




def part2():
    with open("input-06-02.txt") as input_file:
        content = input_file.read()
    # content = "ABabACacBCbca"
    mentors = defaultdict(int)
    pairs = 0
    for c in content:
        if c.isupper():
            mentors[c] += 1
        elif c.islower():
            pairs += mentors[c.capitalize()]
    print(pairs)
    
    
def part3():
    with open("input-06-03.txt") as input_file:
        content = input_file.read()
    print(content) 


if __name__ == "__main__":
    # part1()
    part2()
    # part3()