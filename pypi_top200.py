cat ./top200.py
#!/usr/bin/env python

import xmlrpclib

fmt = '{:30}{:13}{}'
py3_classifier = 'Programming Language :: Python :: 3'

client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')

def header():
    return '\n'.join((fmt.format('Module name', 'Latest', 'Python 3?'),
                      fmt.format('=' * 11, '=' * 6, '=' * 9)))
print(header())
losers = []
for pkg_name, downloads in client.top_packages(200):
    release = client.package_releases(pkg_name)[0]
    release_data = client.release_data(pkg_name, release)
    py3 = bool([x for x in release_data['classifiers']
                if x.startswith(py3_classifier)])
    s = fmt.format(pkg_name, release, py3)
    print(s)
    if not py3:
        losers.append(s)
print('\n{} Python 2 ONLY packages:'.format(len(losers)))
if losers:
    print(header())
    print('\n'.join(losers))
