# coding: utf-8

# See http://omz-forums.appspot.com/pythonista/post/6389848566923264

import array, os, struct

my_matrix_2d = [(x, x * 10) for x in xrange(10)]

def list_of_pairs(in_list):
    out_list = []
    while in_list:
        x, y = in_list[:2]
        in_list = in_list[2:]
        out_list.append([x, y])
    return out_list

# === do it with the array module
def write_2d_matrix_via_array(matrix_2d, filename='matrix_via_array.txt'):
    def flatten(in_list):
        return [item for sublist in in_list for item in sublist]
    a = array.array('f', flatten(matrix_2d))
    with open(filename, 'wb') as out_file:
        a.tofile(out_file)
    
def read_2d_matrix_via_array(filename='matrix_via_array.txt'):
    floats_in_the_file = os.path.getsize(filename) / struct.calcsize('f')
    b = array.array('f')
    with open(filename, 'rb') as in_file:
        b.fromfile(in_file, floats_in_the_file)
    return list_of_pairs(b.tolist())
    
print('=' * 20)
write_2d_matrix_via_array(my_matrix_2d)
print(read_2d_matrix_via_array())

# === do it with the struct module
def read_2d_matrix_via_struct(filename='matrix_via_struct.txt'):
    with open(filename, 'rb') as in_file:
        data = in_file.read()
    fmt = len(data) / struct.calcsize('f') * 'f'
    return list_of_pairs(struct.unpack_from(fmt, data))

def write_2d_matrix_via_struct(matrix_2d, filename='matrix_via_struct.txt'):
    with open(filename, 'wb') as out_file:
        for x, y in matrix_2d:
            out_file.write(struct.pack('ff', x, y))

print('=' * 10)
write_2d_matrix_via_struct(my_matrix_2d)
print(read_2d_matrix_via_struct())
