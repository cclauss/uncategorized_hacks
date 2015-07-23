#!/usr/bin/env python
# coding: utf-8

# See http://omz-forums.appspot.com/pythonista/post/6389848566923264

import array, os, struct

my_matrix_2d = [(x, x * 10) for x in xrange(10)]

def flatten(in_list):
    return [item for sub_list in in_list for item in sub_list]

def list_of_pairs(in_list):
    return zip(in_list[::2], in_list[1::2])

# === do it with the array module
def write_floats_via_array(floats, filename='matrix_via_array.txt'):
    with open(filename, 'wb') as out_file:
        array.array('f', floats).tofile(out_file)

def read_floats_via_array(filename='matrix_via_array.txt'):
    floats_in_the_file = os.path.getsize(filename) / struct.calcsize('f')
    b = array.array('f')
    with open(filename, 'rb') as in_file:
        b.fromfile(in_file, floats_in_the_file)
    return b.tolist()

def write_2d_matrix_via_array(matrix_2d, filename='matrix_via_array.txt'):
    write_floats_via_array(flatten(matrix_2d), filename)
    
def read_2d_matrix_via_array(filename='matrix_via_array.txt'):
    return list_of_pairs(read_floats_via_array(filename))

print('=' * 24)
write_2d_matrix_via_array(my_matrix_2d)
print(read_2d_matrix_via_array())

# === do it with the struct module
def write_floats_via_struct(floats, filename='matrix_via_struct.txt'):
    with open(filename, 'wb') as out_file:
        out_file.write(struct.pack('f' * len(floats), *floats))

def read_floats_via_struct(filename='matrix_via_struct.txt'):
    with open(filename, 'rb') as in_file:
        data = in_file.read()
    return struct.unpack_from(len(data) / struct.calcsize('f') * 'f', data)

def write_2d_matrix_via_struct(matrix_2d, filename='matrix_via_struct.txt'):
    write_floats_via_struct(flatten(matrix_2d), filename)
    
def read_2d_matrix_via_struct(filename='matrix_via_struct.txt'):
    return list_of_pairs(read_floats_via_struct(filename))

print('=' * 12)
write_2d_matrix_via_struct(my_matrix_2d)
print(read_2d_matrix_via_struct())
