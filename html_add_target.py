#!/usr/bin/env python

'''
See: http://omz-forums.appspot.com/editorial/post/5888470794895360

FluidR3_GM.html - Should be a local copy of the original webpage source with 'target="_blank"' added to all <a href> tags that do not already have a target.
'''

import bs4, requests

url = 'https://github.com/gleitz/midi-js-soundfonts/tree/master/FluidR3_GM'
filename = url.rpartition('/')[2] + '.html'
soup = bs4.BeautifulSoup(requests.get(url).text)
a_hrefs = soup.find_all('a', href=True, target=False)
for a_href in a_hrefs:
    a_href['target'] = '_blank'
print('{} instances changed:'.format(len(a_hrefs)))
with open(filename, 'w') as out_file:
    out_file.write(soup.decode())
