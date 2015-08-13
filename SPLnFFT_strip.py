#!/usr/bin/env python
# coding: utf-8

'''
Much like '  1 2 3  '.strip() returns '1 2 3', this script removes any hours which
only contain (0, 0) values from the start and end of a SPLnFFT.bin file.  A new
file is written with a filename format that adds '_<start_hour>h_to_<end_hour>h'.

ex. if SPLnFFT_2015_08_13.bin contains 8 hours of SPL data from 09h00 to 16h59
then an new SPLnFFT_2015_08_13_09h_to_17h.bin file will be written and its size
will be 8/24ths (i.e. 1/3rd) of the size of SPLnFFT_2015_08_13.bin
'''

import numpy, os

filename = 'SPLnFFT_2015_07_21.bin'
root, ext = os.path.splitext(filename)

data = numpy.fromfile(filename, dtype=numpy.float32).reshape(-1, 2)
pairs_per_hour = len(data) / 24 # 28800
assert pairs_per_hour == 28800, '{} has an invalid length: {}'.format(filename, len(data))

start_index = end_index = 0 # find the index of the first and last non-zero pairs
for i, fast_and_slow in enumerate(data):
    if any(fast_and_slow):
        start_index = start_index or i
        end_index = i
assert start_index, filename + ' contains no SPL data!'

start_hour = int(start_index / pairs_per_hour)
end_hour = int(end_index / pairs_per_hour + 1)
out_filename = '{}_{:02}h_to_{:02}h{}'.format(root, start_hour, end_hour, ext)
data[start_hour * pairs_per_hour : end_hour * pairs_per_hour].tofile(out_filename)
fmt = '{} has been written with {} hours of SPL data starting at {:02}h and ending at {:02}h.'
print(fmt.format(out_filename, end_hour - start_hour, start_hour, end_hour))
