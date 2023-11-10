# http://www.pythonchallenge.com
#!/usr/bin/env python

# Python Challenge - Level 05
# http://www.pythonchallenge.com/pc/def/peak.html

# From source code:
# "pickhell" sounds like ~ "pickle"
# Pickle - https://docs.python.org/3/library/pickle.html
# http://www.pythonchallenge.com/pc/def/banner.p


import pickle


f = open("banner.p", "rb")
data = pickle.load(f)
f.close()

# print(data)
# Looks like a asequence of characters and times it repeats

# print character X times
for line in data:
    print("".join([x[0] * x[1] for x in line]))  # x[0]: character, x[1]: times to repeat
# channel

# Solution:
# http://www.pythonchallenge.com/pc/def/channel.html
