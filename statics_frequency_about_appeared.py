from random import randint
from collections import Counter

data = [1, 2, 3, 4, 3, 1, 3]

c = dict.fromkeys(data, 0)
print c

count = Counter(data)

print count
print count.most_common(2)


import re

txt = open('/Users/syu/Desktop/test.log', 'r').read()
cj = Counter(re.split('\w+', txt))

print cj.most_common(3)

