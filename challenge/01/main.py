#!/usr/bin/env python

# Python Challenge - Level 01
# http://www.pythonchallenge.com/pc/def/map.html

def trans(m):
    import string
    l = string.ascii_lowercase
    r = ""
    for i in range(len(m)):
        try:
            r += l[l.index(m[i]) -len(l) +2]
        except:
            r += m[i]
    return r

m = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(trans(m))

url = "http://www.pythonchallenge.com/pc/def/map.html"
print(trans(url))
# "map" -> "ocr"

# Solution
# http://www.pythonchallenge.com/pc/def/ocr.html