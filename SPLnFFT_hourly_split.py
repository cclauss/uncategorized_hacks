#!/usr/bin/env python
# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/6389848566923264
# This code is available at: https://github.com/cclauss/uncategorized_hacks

# SPLnFFT app makes two sound pressure level readings every 1/8th of a second.
# It stores the results into a daily binary data file that this script reads.
#
# Read 1,382,400 float32 values into a numpy.ndarray.
# 24 hours of data is too much to view at once so...
# write out 24 files each containing one hour of SPL data

import datetime, numpy, os

filename = 'SPLnFFT_2015_07_21.bin'
root, ext = os.path.splitext(filename)
fmt = root + '_{:02}' + ext

def elapsed_time(msg='total'):
    return 'Elapsed time ({}): {}'.format(msg, datetime.datetime.now() - start)

start = datetime.datetime.now()
data = numpy.fromfile(filename, dtype=numpy.float32)
print(elapsed_time('Read'))
floats_per_file = len(data) / 24
print('{} floats per file'.format(floats_per_file))
for i in xrange(24):
    data[i*floats_per_file:(i+1)*floats_per_file - 1].tofile(fmt.format(i))
print(elapsed_time('{} files written.  Done.'.format(i+1)))  # approx. 0.333 seconds
