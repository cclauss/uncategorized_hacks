#!/usr/bin/env python
# coding: utf-8

import platform

if platform.system() == 'Darwin':
    if platform.machine().startswith('iP'):
        print('You are running on iOS!')
    else:
        print('You are running on Mac OS X!')
else:
    print('Please upgrade to a real computer and then press any key to continue...')

print('-' * 32 + ' = ...')
fmt = '{}.{:<23} = {}'
for func in (platform.architecture,    platform.machine,        platform.node,
             platform.platform,        platform.processor,      platform.python_build,
             platform.python_compiler, platform.python_branch,  platform.python_implementation,
             platform.python_revision, platform.python_version, platform.python_version_tuple,
             platform.release,         platform.system,         platform.version,
             platform.uname):
    print(fmt.format(func.__module__, func.__name__ + '()', func()))

print('-' * 32)
s, r, v = platform.system(), platform.release(), platform.version()
print(platform.system_alias(s, r, v))  # system, release, version))
print(s)
print(r)
print(v)
print('-' * 32)
print('')
