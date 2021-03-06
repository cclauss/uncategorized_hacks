#!/usr/bin/env python
# coding: utf-8

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3

print('Python "remembers" changes made to complex datatypes when they are used as default parameters to functions.')

# ===== list =====

print('\nProblem with empty list "[]" as a default parameter...')
def func_with_list(value, l=[]):
    l.append(value)
    return l

def func_with_list_fixed(value, l=None):
    l = l or []
    l.append(value)
    return l

for i in xrange(5):
    print('{} vs. {}'.format(func_with_list_fixed(i), func_with_list(i)))

# ===== set =====

print('\nProblem with empty set "set()" as a default parameter...')
def func_with_set(value, s=set()):
    s.add(value)
    return s

def func_with_set_fixed(value, s=None):
    s = s or set()
    s.add(value)
    return s

for i in xrange(5):
    print('{} vs. {}'.format(func_with_set_fixed(i), func_with_set(i)))

# ===== dict =====

print('\nProblem with empty dict "{}" as a default parameter...')
def func_with_dict(value, d={}):
    for key in d:
        d[key] += 1
    d[value] = 0
    return d

def func_with_dict_fixed(value, d=None):
    d = d or {}
    for key in d:
        d[key] += 1
    d[value] = 0
    return d

for c in 'abcde':
    print('{} vs. {}'.format(func_with_dict_fixed(c), func_with_dict(c)))
