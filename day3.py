#!/bin/bash/python3
# https://adventofcode.com/

import numpy as np
from functools import reduce

def get_data():
    with open('./data/day3.csv', 'r') as f:
        data = f.read().strip()
        char_to_int_array = lambda string: np.array(string, 'c').view(np.int8)
        data = [list(map(calculate_item_scores, char_to_int_array(line))) for line in data.split('\n')]
        return data 

def find_duplicates_per_rucksack_compartment(data):
    return [set(line[:len(line)//2]).intersection(set(line[-len(line)//2:])) for line in data]

def find_badge_per_group(data):
    data = [set(x) for x in data]
    data = np.reshape(data, (-1, 3))
    f = lambda line: reduce(lambda x, y: x.intersection(y), line)
    return map(f, data)

def calculate_item_scores(items):
    # a-z [1 ,26]
    # A-Z [27,52]
    # A-Z comes BEFORE a-z, so we shift the scale:
    return 1 + (items - ord('a')) % (ord('z') - ord('A') + 1)

data = get_data()
duplicate_sets = find_duplicates_per_rucksack_compartment(data)
print(duplicate_sets)
print(sum(map(sum, duplicate_sets)))

badge_per_group = find_badge_per_group(data)
print(sum(map(sum, badge_per_group)))
