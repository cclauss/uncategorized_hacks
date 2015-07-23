#!/usr/bin/env python
# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/6389848566923264

# Now I understand why numpy is all the rage with data scientists!!!

# Three lines of numpy do the whole thing!! Import, read, transform,
#  and cleanse.  Much faster execution time too.

import numpy

remove_zero_readings = True  # basic data cleansing

filename = 'SPLnFFT_2015_07_21.bin'
data = numpy.fromfile(filename, dtype=numpy.float32).reshape(-1, 2)
if remove_zero_readings:
    data = data[numpy.any(data > 0, axis=1)]  # cleanse
print(type(data), len(data))  # numpy.ndarray, 2786
#print(data[:20])  # print first 20 fast, slow pairs

t = numpy.arange(0.0, len(data))  # the file has 8 reading per second for a full 24 hour day
# when we cleanse the zero readings out, the timescale makes no sense.  It might be better
# not to cleanse, but then zoom in on nonzero portions, if absolute time is important

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fast = data[:,1]
slow = data[:,0]
ax.plot(t[fast>0], fast[fast>0], marker='.')
ax.plot(t[slow>0], slow[slow>0])
t_bad=t[(fast<=0) | (slow <= 0)]
ax.scatter(t_bad, max(fast.max(), slow.max())+numpy.ones_like(t_bad), marker='o')
plt.legend(('Fast FFT','Slow FFT','Faulty readings'), loc='lower left')
plt.title('Sound Pressure Level data from ' + filename)
#plt.xlabel('Seconds since midnight in a 24 hour day')
plt.xlabel('Number of samples, 8 per second')
plt.ylabel('Sound Pressure Level in dB(A)')
plt.show()
