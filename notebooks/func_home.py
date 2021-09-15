#!/usr/bin/env python3

#the libraries your functions need
import numpy as np

def print_name(some_name):
    print (f'the name is {some_name}')
    
def print_len_name(some_name):
    print (f'the length of the name is {len(some_name)}')
    
def print_max_num(some_name):
    hold=np.max(len(some_name))
    return hold
