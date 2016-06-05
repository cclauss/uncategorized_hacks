#!/usr/bin/env python3

MAX_PACKAGES = 200
USE_ASYNCIO = True

import asyncio
import collections
import time
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

pkg_info = collections.namedtuple('pkg_info', 'pkg_name downloads version py3')
fmt = '{:30}{:13}{}'
py3_classifier = 'Programming Language :: Python :: 3'

client = ServerProxy('https://pypi.python.org/pypi')


def header():
    return '\n'.join((fmt.format('Module name', 'Latest', 'Python 3?'),
                      fmt.format('=' * 11, '=' * 6, '=' * 9)))


def get_pkg_info(pkg_name, downloads=0):
    # multiple asyncio jobs can not share a client
    local_client = ServerProxy('https://pypi.python.org/pypi') if USE_ASYNCIO else client
    try:
        release = local_client.package_releases(pkg_name)[0]
    except IndexError:  # marionette-transport and similar
        print(pkg_name)
        return None
    release_data = local_client.release_data(pkg_name, release)
    py3 = py3_classifier in '\n'.join(release_data['classifiers'])
    return pkg_info(pkg_name, downloads, release, py3)


@asyncio.coroutine
def async_main():  # ~ 32 seconds for 200 packages on my MacBook Pro
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(None, get_pkg_info, pkg_name, downloads)
               for pkg_name, downloads in client.top_packages(MAX_PACKAGES)]
    return [(yield from fut) for fut in futures]


def sync_main():
    # as list for apples-to-apples benchmark - ~ 112 seconds
#   return [get_pkg_info(pkg_name, downloads) for pkg_name, downloads
#           in client.top_packages(MAX_PACKAGES)]

    # or as a generator for continuous output - ~ 105 seconds
    return (get_pkg_info(pkg_name, downloads) for pkg_name, downloads
            in client.top_packages(MAX_PACKAGES))


print('Gathering Python 3 support info on the top {} PyPI packages...'.format(MAX_PACKAGES))
start = time.time()
if USE_ASYNCIO:
    loop = asyncio.get_event_loop()
    packages_info = loop.run_until_complete(async_main())
else:
    packages_info = sync_main()
print(time.time() - start)  # ~ 32 seconds if USE_ASYNCIO else ~ 112 seconds

print(header())
for package_info in packages_info:
    print(fmt.format(package_info.pkg_name, package_info.version, package_info.py3))

losers = [pkg for pkg in packages_info if not pkg.py3]
print('\n{} Python 2 ONLY packages:'.format(len(losers)))
if losers:
    print(header())
    print('\n'.join(fmt.format(pkg.pkg_name, pkg.version, pkg.py3) for pkg in losers))

print(time.time() - start)
