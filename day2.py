#!/bin/bash/python3
# https://adventofcode.com/

import numpy as np

def rps_match(c1, c2):  # part 1
    # who wins? matrix is LTW -> 012
    #  (c1) 0 1 2 (c2) aka RPS
    #     0 1 2 0   win if: (c2 - c1 + 4) % 3
    #     1 0 1 2   
    #     2 2 0 1
    return (c2 - c1 + 4) % 3

def decode_rps_symbol(c1, c2):  # part 2
    # what to play? matrix is RPS -> 012
    #  (c1) 0 1 2 (c2) aka LTW
    #     0 2 0 1
    #     1 0 1 2   play: (c1 + c2 + 2) % 3
    #     2 1 2 0
    return (c1 + c2 + 2) % 3


def calc_points(match_results, c2):
    # points:
        # L T W (match points)
        # 0 3 6
        # match points: 3 * result

        # R P S (symbol points)
        # 1 2 3
        # symbol points: c2 + 1
    return sum(match_results * 3 + c2 + 1)


def get_c1_c2():
    with open('./data/day2.csv', 'r') as f:
        data = f.read().strip()
        data = data.replace('\n', '')
        data = data.replace(' ', '')
        data = np.array(data, 'c').view(np.int8).reshape(-1,2)
        data[:,0] -= 65  # (a, b, c) -> (0, 1, 2)
        data[:,1] -= 88 # (x, y, z) -> (0, 1, 2)
    return data[:, 0], data[:, 1]

c1, c2 = get_c1_c2()
match_results = np.array(list(map(rps_match, c1, c2)))
points = calc_points(match_results, c2)
print(points)

c1, c2 = get_c1_c2()
rps_symbols = np.array(list(map(decode_rps_symbol, c1, c2)))
match_results = np.array(list(map(rps_match, c1, rps_symbols)))
points = calc_points(match_results, rps_symbols)
print(points)
