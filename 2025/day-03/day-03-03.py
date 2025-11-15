import os
import sys
import re
import math
import itertools
import tqdm
from collections import Counter

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

file = list(map(int, open("test-input-03-03.txt").read().split(",")))
print(file)
# file = [4,51,13,64,57,51,82,57,16,88,89,48,32,49,49,2,84,65,49,43,9,13,2,3,75,72,63,48,61,14,40,77]

crates = Counter(file)


print(crates)
print(max(crates.values()))
