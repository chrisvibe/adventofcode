#!/bin/bash/python3
# https://adventofcode.com/

import re
import numpy as np

def get_data():
    # with open('./data/test/day5.csv', 'r') as f:
    with open('./data/day5.csv', 'r') as f:
        data = f.read().rstrip()
        crates, moves = data.split('\n\n') 
        crates = crates[1::4]
        n_stacks = int(crates[-1])
        crates = crates[:-n_stacks]
        crates = list(np.array(list(crates)).reshape(-1,n_stacks).T)
        crates = [list(filter(lambda c: c != ' ', x))[::-1] for x in crates] 
        moves = re.findall(r'\d+', moves)
        moves = np.reshape(moves, (-1, 3)).astype('int64') 
        moves[:, -2:] -= 1 # convert to/from to zero-indexed
        return crates, moves 

def arrange_crates(crates, moves, many_crates_at_a_time=False):
    new_crates = crates.copy()
    for move in moves:
        n, i, j = list(move)
        max_n = min(len(new_crates[i]), n)
        # TODO how does one make new_crates selection a variable? See the commented lines below:
        # moved_crates = new_crates[i][-max_n:]
        # moved_crates = moved_crates if many_crates_at_a_time else moved_crates[::-1]
        moved_crates = new_crates[i][-max_n:] if many_crates_at_a_time else new_crates[i][-max_n:][::-1]
        new_crates[j].extend(moved_crates)
        del new_crates[i][-max_n:]
    return new_crates


crates, moves = get_data()
print([''.join(stack) for stack in crates])
print('-'*20)
print(moves)

print(''.join([x[-1] if x else ' ' for x in arrange_crates(crates, moves)]))
crates, moves = get_data() # TODO fix this hack. numpy array memory seems to be unintentionally modified
print(''.join([x[-1] if x else ' ' for x in arrange_crates(crates, moves, many_crates_at_a_time=True)]))
