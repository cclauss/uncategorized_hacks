#!/usr/bin/env python

import platform, sys

if platform.system() == 'Darwin':
    if platform.machine().startswith('iP'):
        print('You are running on iOS!')
    else:
        print('You are running on Mac OS X!')
else:
    print('Please upgrade to a real computer and then press any key to continue...')

fmt = '{:<32} = {}'
print(fmt.format('-' * 32, '...'))
print(fmt.format('platform.architecture()',          platform.architecture()))
print(fmt.format('platform.machine()',               platform.machine()))
print(fmt.format('platform.node()',                  platform.node()))
print(fmt.format('platform.platform()',              platform.platform()))
print(fmt.format('platform.processor()',             platform.processor()))
print(fmt.format('platform.python_build()',          platform.python_build()))
print(fmt.format('platform.python_compiler()',       platform.python_compiler()))
print(fmt.format('platform.python_branch()',         platform.python_branch()))
print(fmt.format('platform.python_implementation()', platform.python_implementation()))
print(fmt.format('platform.python_revision()',       platform.python_revision()))
print(fmt.format('platform.python_version()',        platform.python_version()))
print(fmt.format('platform.python_version_tuple()',  platform.python_version_tuple()))
print(fmt.format('platform.release()',               platform.release()))
print(fmt.format('platform.system()',                platform.system()))
print(fmt.format('platform.version()',               platform.version()))
print(fmt.format('platform.uname()',                 platform.uname()))

print('-' * 32)
s, r, v = platform.system(), platform.release(), platform.version()
print(platform.system_alias(s, r, v)) # system, release, version))
print(s)
print(r)
print(v)
print('-' * 32)
print('')
