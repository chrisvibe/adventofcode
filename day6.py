#!/bin/bash/python3
# https://adventofcode.com/

import numpy as np

def get_data():
    # with open('./data/test/day6.csv', 'r') as f:
    with open('./data/day6.csv', 'r') as f:
        data = f.read().strip()
        data = data.split('\n')
        return data 

def find_rightmost_index_of_first_unique_char_sequence_in_string(string, sequence_length=4):
    sequence = []
    for i in range(len(string)):
        c = string[i]
        n = "".join(sequence).find(c)
        sequence.append(c)
        if n != -1:
            del sequence[:n+1]
        elif len(sequence) == sequence_length:
            return i, ''.join(sequence)
    return -1, ''

data = get_data()
test_answers = [(7 , 19), (5, 23), (6, 23), (10, 29), (11, 26)]
# looks like 19 was wrong for test string 1, should be 25
i = 0
for msg in data:
    start_msg_rightmost_index, _ = find_rightmost_index_of_first_unique_char_sequence_in_string(msg, sequence_length=4)
    print('part1:', start_msg_rightmost_index+1, '(should be: {})'.format(test_answers[i][0]))
    msg_rightmost_index, _ = find_rightmost_index_of_first_unique_char_sequence_in_string(msg[start_msg_rightmost_index + 1:], sequence_length=14)
    print('part2:', start_msg_rightmost_index + 1 + msg_rightmost_index + 1, '(should be: {})'.format(test_answers[i][1]))
    i += 1

