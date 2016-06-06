#!/usr/bin/env python3

import asyncio
import collections
import time
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

MAX_PACKAGES = 200  # or try 1000
PYPI_URL = 'https://pypi.python.org/pypi'
USE_ASYNCIO = True

pkg_info = collections.namedtuple('pkg_info', 'pkg_name downloads version py3')
FMT = '{pkg_name:30}{version:13}{py3}'
py3_classifier = 'Programming Language :: Python :: 3'

client = ServerProxy(PYPI_URL)


def header():
    fmt = '{:30}{:13}{}'
    return '\n'.join((fmt.format('Module name', 'Latest', 'Python 3?'),
                      fmt.format('=' * 11, '=' * 6, '=' * 9)))


def get_pkg_info(pkg_name, downloads=0):
    # multiple asyncio jobs can not share a client
    local_client = ServerProxy(PYPI_URL) if USE_ASYNCIO else client
    try:
        release = local_client.package_releases(pkg_name)[0]
    except IndexError:  # marionette-transport, ll-orasql, and similar
        print(pkg_name, 'has no releases in PyPI!!')
        return pkg_info(pkg_name, downloads, 'PyPI error!!', False)
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
    # return [get_pkg_info(pkg_name, downloads) for pkg_name, downloads
    #         in client.top_packages(MAX_PACKAGES)]

    # or as a generator for continuous output - ~ 105 seconds
    return (get_pkg_info(pkg_name, downloads) for pkg_name, downloads
            in client.top_packages(MAX_PACKAGES))


fmt = 'Gathering Python 3 support info on the top {} PyPI packages...'
print(fmt.format(MAX_PACKAGES))
start = time.time()
if USE_ASYNCIO:
    loop = asyncio.get_event_loop()
    packages_info = loop.run_until_complete(async_main())
else:
    packages_info = sync_main()
print(time.time() - start, 'seconds')  # ~ 32 sec if USE_ASYNCIO else ~ 105 sec

print(header())
for package_info in packages_info:
    print(FMT.format(**package_info._asdict()))

losers = [pkg for pkg in packages_info if not pkg.py3]
print('\n{} Python 2 ONLY packages:'.format(len(losers)))
if losers:
    print(header())
    print('\n'.join(FMT.format(**pkg._asdict()) for pkg in losers))

print(time.time() - start, 'seconds')
