import random
from operator import itemgetter,attrgetter
dic = {}
for x in range(10):
    dic[chr(random.randint(97, 122))] = x * random.randint(0, 10)



print dic

print zip(dic.values(), dic.keys())

print sorted(zip(dic.itervalues(), dic.iterkeys()))

print sorted(dic.iteritems(), key=lambda x: x[1])

print sorted(dic.iteritems(), key=itemgetter(1, 0))
print sorted(dic.iteritems(), key=itemgetter(1, 0), reverse=True)





