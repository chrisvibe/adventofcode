#!/bin/bash/python3
# https://adventofcode.com/

from functools import reduce
from itertools import groupby

with open('./data/day1.csv', 'r') as f:
    data = f.read().strip()
    data = data.split('\n')
    data = list(map(lambda x: int(x) if x else 0, data))
    data = [list(g) for k, g in groupby(data, key=bool) if k]
    data = [reduce(lambda a, b: a+b, x) for x in data]

print(max(data))
print(sum(sorted(data, reverse=True)[:3]))
