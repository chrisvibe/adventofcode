#!/bin/bash/python3
# https://adventofcode.com/

import re
import numpy as np
from functools import reduce

def get_data():
    # with open('./data/test/day4.csv', 'r') as f:
    with open('./data/day4.csv', 'r') as f:
        data = f.read().strip()
        data = re.split('\n-,', data)
        data = np.reshape(data, (-1, 4)).astype('int64') 
        return data 

def detect_subset_instances_in_pairs(data):
    # approach 1: take c0 - c2 and c1 - c3 
    # 1 3 → 0 0 → 0
    # 1 3 

    # 1 3 → 0 1 → 0
    # 1 2 

    # 2 3 → 1 0 → 0
    # 1 3 

    # 2 3 → 1 -1 → -
    # 1 4 

    #-------------

    # 2 3 → 1 1 → +
    # 1 2 

    # sign(c0-c2)*sign(c1-c3) == 1 ⇒  A⊆ B || B⊆ A
    diff = data[:,:2] - data[:,-2:]
    diff_sign = np.sign(diff) 
    return (diff_sign[:,0] * diff_sign[:,1]) != 1

    # approach 2:
    # a_min, a_max, b_min, b_max = data[:,0], data[:,1], data[:,2], data[:,3]
    # assume A- <= B-
    # subset if B- <= A+ and B+ <= A+
    # repeat logic with assumption as false
    # return (a_min <= b_min) & ((b_min <= a_max) & (b_max <= a_max)) | (b_min <= a_min) & ((a_min <= b_max) & (a_max <= b_max))  # simplified below
    # return ~(~((a_min <= b_min) & (b_min <= a_max) & (b_max <= a_max)) & ~((b_min <= a_min) & (a_min <= b_max) & (a_max <= b_max)))  # de morgans law (fast eval, only &)


def detect_overlap_instances_in_pairs(data):
    # approach 1: take max-min c1 - c2 and c3 - c0
    # 1 2 →  1 1 → +
    #   1 2 

    # 1 2 →  0 2 → 0 
    #   2 3 
    # 2 3 →  2 0 → 0 
    #   1 2 

    #-------------

    # 1 2 → -1 3 → -
    #   3 4 
    # 3 4 →  3 -1 → -
    #   1 2 

    diff = data[:,[1, 3]] - data[:, [2, 0]]
    diff_sign = np.sign(diff) 
    return (diff_sign[:,0] * diff_sign[:,1]) != -1
 
    # approach 2:
    # assume A- <= B-
    # overlap if A+ <= B-
    # repeat logic with assumption as false
    # a_min, a_max, b_min, b_max = data[:,0], data[:,1], data[:,2], data[:,3]
    # return (a_min <= b_min) & (a_max >= b_min) | (b_min <= a_min) & (b_max >= a_min)  # simplified below
    # return ~(~((a_min <= b_min) & (a_max >= b_min)) & ~((b_min <= a_min) & (b_max >= a_min)))  # de morgans law (fast eval, only &)

data = get_data()
print(data)

subset = detect_subset_instances_in_pairs(data)
print(sum(subset))

overlap = detect_overlap_instances_in_pairs(data)
print(sum(overlap))

