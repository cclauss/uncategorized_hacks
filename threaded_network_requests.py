# coding: utf-8

# See: http://omz-forums.appspot.com/pythonista/post/4970494348492800

import datetime, requests, threading, time
print('=' * 20)
fmt = '{} bytes downloaded from {}.'
urls = ['http://' + x for x in 'google.com bing.com yahoo.com facebook.com'.split()]

print('Starting serial data acquisition...')
start = datetime.datetime.now()
for url in urls:
    data = requests.get(url).text
    print(fmt.format(len(data), url))
print('Elapsed time (serial): {}'.format(datetime.datetime.now() - start)) 

class Worker(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.start()

    def run(self):
        data = requests.get(self.url).text
        print(fmt.format(len(data), self.url))

print('\nStarting parallel data acquisition...')
start = datetime.datetime.now()
workers = [Worker(url) for url in urls]
while any(worker.is_alive() for worker in workers):
    time.sleep(1)
print('Elapsed time (parallel): {}'.format(datetime.datetime.now() - start)) 
