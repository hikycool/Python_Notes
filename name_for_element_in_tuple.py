from collections import namedtuple

NAME, SEX = xrange(2)

S1 = ('Jim', 'male')
print S1[NAME], S1[SEX]

Student = namedtuple('Student', ['name', 'sex'])
S2  = Student('Jane', 'female')
print S2.name, S2.sex


