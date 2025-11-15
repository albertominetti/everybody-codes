import os, sys, re, math, itertools, tqdm, functools

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def part1():
    with open("input-04-01.txt") as input_file:
        content = input_file.read()

    gears = list(map(int, content.split('\n')))
    # gears = [128, 64, 32, 16, 8]
    # gears = [102, 75, 50, 35 , 13]

    print(2025* gears[0] // gears[-1] ) 


def part2():
    with open("input-04-02.txt") as input_file:
        content = input_file.read()

    gears = list(map(int, content.split('\n')))
    # gears = [128, 64, 32, 16, 8]
    # gears = [102, 75, 50, 35 , 13]

    print(math.ceil(10000000000000 * gears[-1] / gears[0]) ) 


def part3():
    with open("input-04-03.txt") as input_file:
        content = input_file.read()
    gears = [tuple(map(int, line.split("|"))) for line in content.splitlines()]

    print(gears)
    
    ratio = 1
    for a, b in gears[1:-1]:
        ratio *= b / a
    
    ratio *= gears[0][0] / gears[-1][0]

    print(int(100 * ratio))
    

if __name__ == "__main__":
    part1()
    part2()
    part3()