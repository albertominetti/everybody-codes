import os, sys, re, math, itertools, tqdm

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    def add(self, new_val):
        if self.val < new_val  and self.right is None:
            self.right = new_val
        elif new_val < self.val and self.left is None:
            self.left = new_val
        else:
            if self.next is None:
                self.next = Node(new_val)
            else:
                self.next.add(new_val)
    
    def spine(self):
        if self.next:
            return [self.val] + self.next.spine()
        else:
            return [self.val]

def part1():
    with open("input-05-01.txt") as input_file:
        content = input_file.read()
        
    _, numbers = content.split(":")
    numbers = list(map(int, numbers.split(",")))
    
    # numbers = [5,3,7,8,9,10,4,5,7,8,8]
    print(numbers) 
    
    result = Node(numbers[0])
    for n in numbers[1:]:
        result.add(n)
            
    print(result.spine())
    print("".join(map(str, result.spine())))




def part2():
    with open("input-05-03.txt") as input_file:
        content = input_file.read()
    print(content) 
    
    
    
def part3():
    with open("input-05-03.txt") as input_file:
        content = input_file.read()
    print(content) 


if __name__ == "__main__":
    part1()
    # part2()
    # part3()