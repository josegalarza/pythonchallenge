#!/usr/bin/env python
# Python Challenge - Level 10
# http://www.pythonchallenge.com/pc/return/bull.html

# hint:
# len(a[30]) = ?


# click the cow,
# a = [1, 11, 21, 1211, 111221,

# `a` it's the Conway's sequence.
# We need to generate 30 numbers,
# and get the length of the 30th.


def conwayfy(n):
    """
    Given an input number n,
    the function returns next number in the Conway sequence.
    """
    result = ''
    x = 0  # starting index
    while x < len(n):
        d = n[x]  # digit to count repetitions
        c = 0  # repetition count
        while True:
            c += 1  # count occurrence
            try:
                if n[x+c] == d:  # if next digit is the same
                    continue
                else:
                    break
            except IndexError:
                break
        # digit n repeated c times
        result += f"{c}{d}"
        # update next index
        x += c
    return result


# calculate the Conway sequence `a`
a = ['1']
for x in range(30):
    last_num = a[-1]
    a.append(conwayfy(last_num))

print(len(a[30]))
# 5808

# Solution
# http://www.pythonchallenge.com/pc/return/5808.html