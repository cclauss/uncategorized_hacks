#!/usr/bin/env python
# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/6389848566923264

# Now I understand why numpy is all the rage with data scientists!!!

# Three lines of numpy do the whole thing!! Import, read, transform,
#  and cleanse.  Much faster execution time too.

import numpy
data = numpy.fromfile('SPLnFFT_2015_07_21.bin', dtype=numpy.float32).reshape(-1, 2)
data = data[numpy.any(data > 0, axis=1)]  # cleanse
print(type(data), len(data))  # numpy.ndarray, 2786
#print(data[:20])  # print first 20 fast, slow pairs

N=len(data)
t=numpy.arange(0.0,N)  #i suspect the file has a full 24 hours in it, but we cleansed a portion, so te timescale makes no sense. better would be to not cleanse, but then zoom on nonzero portions, if absolute time is important

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fast = data[:,1]
slow = data[:,0]

ax.plot(t[fast>0], fast[fast>0],marker='.')
ax.plot(t[slow>0],slow[slow>0])
t_bad=t[(fast<=0) | (slow <= 0)]
ax.scatter(t_bad, max(fast.max(),slow.max())+numpy.ones_like(t_bad),marker='o')
plt.legend(('fast','slow','bad'))
plt.title('SPLnFFT Noise data')
plt.show()