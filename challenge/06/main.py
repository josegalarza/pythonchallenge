# http://www.pythonchallenge.com
# Level 6
# http://www.pythonchallenge.com/pc/def/channel.html

# http://www.pythonchallenge.com/pc/def/pants.html

"""
import requests

r = requests.get('http://www.pythonchallenge.com/pc/def/pants.html')
print (r.text)

r = requests.get('http://www.pythonchallenge.com/pc/def/zip.html')
print (r.text)

r = requests.get('http://www.pythonchallenge.com/pc/def/zipper.html')
print (r.text)

# http://www.pythonchallenge.com/pc/def/channel.zip -> get the ZIP file -> extract

import os
with open(os.path.join('channel', 'readme.txt')) as f:
	print(f.read())
	
id = 9002
while True:
	with open('channel/%s.txt' % id) as f:
		data = f.read()
		print(data)
		id = data.split('Next nothing is ')[1]

"""

# clue: Collect the comments
import zipfile
z = zipfile.ZipFile('channel.zip')
file_id = 9002
filename = '%d.txt' % file_id

comments = ""

print('FILE_ID - FILENAME - DATA')

try:
	while filename:
		# get zip/file info
		comment = z.getinfo(filename).comment.decode('utf-8')
		comments += comment
		
		
		with open('channel\%s' % filename) as f:
			data = f.read()
			
			print('%r\t%r\t%r\t%r' % (file_id, filename, comment, data))
			
			file_id = data.split('Next nothing is ')[1]
			filename = '%s.txt' % file_id

except Exception as e:
	print(e)
finally:
	print(comments)

# oxygen
# http://www.pythonchallenge.com/pc/def/oxygen.html