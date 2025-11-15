import os
import sys
import re
import math
import itertools
import tqdm

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

file = list(map(int, open("test-input-03-01.txt").read().split(",")))
print(file)

crates = sorted(list(set(file)), reverse=True)
print(crates)

print(sum(crates))
