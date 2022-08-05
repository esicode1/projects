#!/usr/bin/python3

from urllib import request

with open('urls.txt') as f:
   for line in f:
      url = line
      path = 'path to download files'+url.split('/', -1)[-1]
      request.urlretrieve(url, path.rstrip('\n'))
