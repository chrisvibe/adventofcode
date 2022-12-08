#!/bin/bash/python3
# https://adventofcode.com/

import numpy as np
from functools import reduce

def get_data():
    # with open('./data/test/day7.csv', 'r') as f:
    with open('./data/day7.csv', 'r') as f:
        data = f.read().strip()
        data = data.split('\n')
        return data 

def std_out_to_file_tree(std_out):
    file_tree = dict()
    file_tree['..'] = file_tree
    file_tree['__size__'] = 0
    file_tree['__type__'] = 'folder' 
    root_folder = '/'
    file_tree[root_folder] = dict() 
    file_tree[root_folder]['..'] = file_tree
    file_tree[root_folder]['__size__'] = 0
    file_tree[root_folder]['__type__'] = 'folder' 
    current_tree = file_tree[root_folder]
    current_folder = root_folder
    for o in std_out:
        parced = o.split(' ')
        a, b = parced[:2]
        c = parced[2] if len(parced) == 3 else ''
        if a == '$': # execute command 
            if b == 'cd':
                # navigate to folder
                for folder in c.split('/'):
                    if folder:
                        current_tree = current_tree[folder]
            elif b == 'ls':
                # init recording of files/folders
                pass
        else:
            # recording of files/folders
            current_tree[b] = dict()
            current_tree[b]['..'] = current_tree
            if a == 'dir':
                current_tree[b]['__size__'] = 0
                current_tree[b]['__type__'] = 'folder' 
            else:
                current_tree[b]['__size__'] = int(a)
                current_tree[b]['__type__'] = 'file' 
    return file_tree

def print_nested_dict(nested_dict, i=0):
    for k in nested_dict:
        if k not in ['..', '__size__', '__type__']:
            print('\t'*i, k, nested_dict[k]['__type__'], nested_dict[k]['__size__'])
            if isinstance(nested_dict[k], dict):
                print_nested_dict(nested_dict[k], i+1)

def calc_folder_sizes(tree):
    for branch in tree:
        if isinstance(tree[branch], dict) and branch != '..':
            sub_tree = calc_folder_sizes(tree[branch]) 
            tree['__size__'] += sub_tree['__size__']
    return tree

def flatten_file_tree(nested_dict, i=0, file_tree=None):
    if not file_tree:
        file_tree = []
    for k in nested_dict:
        if k not in ['..', '__size__', '__type__']:
            file_tree.append({
                'level': i,
                'name': k,
                'type': nested_dict[k]['__type__'],
                'size': nested_dict[k]['__size__'],
                })
            if isinstance(nested_dict[k], dict):
                flatten_file_tree(nested_dict[k], i+1, file_tree=file_tree)
    return file_tree

data = get_data()
file_tree = std_out_to_file_tree(data)
print('-'*20)
file_tree = calc_folder_sizes(file_tree)
print_nested_dict(file_tree)

flat_file_tree = flatten_file_tree(file_tree)
l = list(filter(lambda f: f['size'] <= 100000 and f['type'] == 'folder', flat_file_tree))
print(sum(map(lambda x: x['size'], l)))
l = list(filter(lambda f: f['size'] >= 8381165 and f['type'] == 'folder', flat_file_tree))
print(min(map(lambda x: x['size'], l)))
