#!/usr/bin/env python

# Python Challenge - Level 04
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests

id = 12345
id = 16044 /2

while True:
	r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % id)
	print(r.text)
	id = r.text.split('and the next nothing is ')[1]

# Solution:
# http://www.pythonchallenge.com/pc/def/peak.html
