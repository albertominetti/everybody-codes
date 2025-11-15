import os, sys, re, math, itertools, tqdm

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


class Node:
    def __init__(self, val, sword = 0):
        self.sword = int(sword)
        self.val = val
        self.left = None
        self.right = None
        self.next = None
        self._number = None
        self._spine = None

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
        if not self._spine:
            if self.next:
                res = int(str(self.val) + str(self.next.spine()))
            else:
                res = self.val
            self._spine = res
        return self._spine
    
    def levels(self):
        res = [self.number()]
        if self.next:
            res += self.next.levels()
        return res

    def number(self):
        if not self._number:  # used like a cache
            res = []
            if self.left:
                res.append(self.left)
            res.append(self.val)     
            if self.right:
                res.append(self.right)
            self._number = int("".join(map(str, res)))
        return self._number
    
    def __lt__(self, other):
        if isinstance(other, Node):
            if self.spine() < other.spine():
                return True
            elif self.spine() > other.spine():
                return False
            else:
                self_levels = self.levels()
                other_levels = other.levels()
                for i in range(min(len(self_levels), len(other_levels))):
                     if self_levels[i] < other_levels[i]:
                         return True
                     elif self_levels[i] > other_levels[i]:
                         return False
                if len(self_levels) < len(other_levels):
                    return True
                elif len(self_levels) > len(other_levels):
                    return False
                else:
                    return self.sword < other.sword
        return NotImplemented
    
    def __str__(self):
        return f"{self.sword} Q:{self.spine()} L: {self.levels()}"
    
    __repr__ = __str__

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

def part2():
    swords = {}
    with open("input-05-02.txt") as input_file:
        line = input_file.readline()
        while line:
            sword, numbers = line.split(":")
            numbers = list(map(int, numbers.split(",")))
            swords[sword] = numbers
            line = input_file.readline()
        
    qualities = {}
    for s in swords:
        numbers = swords[s]
        result = Node(numbers[0])
        for n in numbers[1:]:
            result.add(n)
        qualities[s] = result.spine()
    
    print(max(qualities.values()) - min(qualities.values()))
    
def part3():
    swords = {}
    with open("input-05-03.txt") as input_file:
        line = input_file.readline()
        while line:
            sword, numbers = line.split(":")
            numbers = list(map(int, numbers.split(",")))
            swords[sword] = numbers
            line = input_file.readline()
    
    # swords = {1: [7,1,9,1,6,9,8,3,7,2], 2:[7,1,9,1,6,9,8,3,7,2]}
    # swords = {
    #     1:[7,1,9,1,6,9,8,3,7,2],
    #     2:[6,1,9,2,9,8,8,4,3,1],
    #     3:[7,1,9,1,6,9,8,3,8,3],
    #     4:[6,1,9,2,8,8,8,4,3,1],
    #     5:[7,1,9,1,6,9,8,3,7,3],
    #     6:[6,1,9,2,8,8,8,4,3,5],
    #     7:[3,7,2,2,7,4,4,6,3,1],
    #     8:[3,7,2,2,7,4,4,6,3,7],
    #     9:[3,7,2,2,7,4,1,6,3,7],
    # }
    qualities = []
    for s in swords:
        numbers = swords[s]
        result = Node(numbers[0], s)
        for n in numbers[1:]:
            result.add(n)
        qualities.append(result)
    
    print(qualities)
    best_sorted = sorted(qualities, reverse=True)
    
    checksum = 0
    for i, s in enumerate(best_sorted):
        print(f"{i + 1} * {s.sword}")
        checksum += (i + 1) * s.sword
    print(checksum)
    
    
    


if __name__ == "__main__":
    # part1()
    # part2()
    part3()