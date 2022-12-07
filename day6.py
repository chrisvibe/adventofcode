#!/bin/bash/python3
# https://adventofcode.com/

import numpy as np

def get_data():
    # with open('./data/day6.csv', 'r') as f:
    with open('./data/test/day6.csv', 'r') as f:
        data = f.read().strip()
        return data 

data = get_data()

def find_first_possible_starting_signal(string):
    starting_string = []
    for c in string:
        starting_string.append(c)
        if c in starting_string: # start from the right of the last match (scan backward)
            starting_string = []
        elif len(starting_string) == 4:
            break
        else:
            pass
