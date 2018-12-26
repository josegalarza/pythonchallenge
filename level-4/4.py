# http://www.pythonchallenge.com
# Level 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests

id = 12345
id = 16044 /2

while True:
	r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % id)
	print(r.text)
	id = r.text.split('and the next nothing is ')[1]