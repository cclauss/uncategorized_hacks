#!/usr/bin/env python
# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/6389848566923264

# Now I understand why numpy is all the rage with data scientists!!!

# Four lines of numpy do the while thing!! Import, read, transform, and cleanse.
# Much faster execution time too.

import numpy
data = numpy.fromfile('SPLnFFT_2015_07_21.bin', dtype=numpy.float32)
data.shape = (len(data) / 2, 2)
data = data[numpy.all(data > 0, axis=1)]
print(type(data), len(data))  # numpy.ndarray, 2786
print(data[:20])
