#!/usr/bin/env python
# coding: utf-8

# See: https://www.facebook.com/SPLnFFT  Paid app plus in-app purchase to upload .bin to Dropbox
# and: https://omz-forums.appspot.com/pythonista/post/6389848566923264

# 5529600 bytes in the file / 4 bytes per float = 1382400 floats in the file

import datetime, itertools, struct

filename = 'SPLnFFT_2015_07_21.bin'

def list_of_pairs(in_list):
    return itertools.izip(in_list[::2], in_list[1::2])
    # return zip(in_list[::2], in_list[1::2])  # also works but slower

def read_floats(filename=filename):
    with open(filename, 'rb') as in_file:
        data = in_file.read()
    return struct.unpack_from(len(data) / struct.calcsize('f') * 'f', data)

print('=' * 28)
start = datetime.datetime.now()
list_of_floats = read_floats(filename)  # reads floats into a list
print('Elapsed time (read_floats()): {}'.format(datetime.datetime.now() - start)) 
print('{:>7} floats in the list'.format(len(list_of_floats)))
fast_slow_list = list_of_pairs(list_of_floats)  # 1D list --> 2D list
# remove the invalid elements
fast_slow_list = my_list = [(x[0], x[1]) for x in fast_slow_list if x[0] > 0 and x[1] > 0]
print('{:>7} pairs after cleaning'.format(len(fast_slow_list)))
print('Elapsed time (total): {}'.format(datetime.datetime.now() - start)) 
print(fast_slow_list[:50])  # print just the first 50 fast_slow pairs
print('Done.')
