#!/usr/bin/env python
# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/6389848566923264
# This code is available at: https://github.com/cclauss/uncategorized_hacks

# SPLnFFT app makes two sound pressure level readings every 1/8th of a second.
# It stores the results into a daily binary data file that this script reads.
#
# Read 1,382,400 float32 values into a numpy.ndarray.
# Reshape that ndarray into two columns of 691,200 floats each.
# 691,200 == 8 readings per sec * 60 secs per min * 60 mins per hour * 24 hours.
# The columns represent Fast Sound Pressure Level and Slow Sound Pressure Level.

# 24 hours of data is too much to view at once so work should be
# done to allow users to zoom into interesting portions of the day.

import datetime, numpy

filename = 'SPLnFFT_2015_07_21.bin'

def elapsed_time(msg='total'):
    return 'Elapsed time ({}): {}'.format(msg, datetime.datetime.now() - start)

start = datetime.datetime.now()
data = numpy.fromfile(filename, dtype=numpy.float32).reshape(-1, 2)
print(elapsed_time('4 Read and reshape'))
print(type(data), len(data))  # numpy.ndarray, 691200
#print(data[:20])  # print first 20 fast, slow pairs
#print(data[-20:])  # print last 20 fast, slow pairs
t = numpy.linspace(0.0, 24.0, len(data))

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fast = data[:,0]
slow = data[:,1]
ax.plot(t[fast>0], fast[fast>0], 'g+-')
ax.plot(t[slow>0], slow[slow>0], 'ms-')
t_bad = t[(fast <= 0) | (slow <= 0)]
print(elapsed_time('3 Starting scatter...'))  # approx. 0.5 seconds
ax.scatter(t_bad, max(fast.max(), slow.max()) + numpy.ones_like(t_bad), marker='o')
print(elapsed_time('2 Scatter'))  # approx. 22 seconds
plt.legend(('Fast Lp','Slow Lp','Negative readings'), loc='lower right')
plt.title('Sound Pressure Level data from ' + filename)
plt.xlabel('Eight samples per second across a 24 hour day')
plt.ylabel('Sound Pressure Level (Lp) in dB(A)')
# x axis currently starts at -5 and ends at 30 with ticks every 5 hours.
# we would like it to starts at 0 and ends at 24 with a tick every hour.
#plt.xticks(fast, xrange(24))  # crashes!
#plt.xticks(fast, numpy.arange(0,24))  # crashes!
print(elapsed_time('1 Adornments'))
plt.show()
print(elapsed_time('0 plt.show() Done.'))  # approx. 2 minutes 20 seconds
