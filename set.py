# sets = {'a', 's', 'e', 'q', 'a', 1,'1'}
# print(sets)
# print(type(sets))

# #for s in sets:
#   #print(s)
# print(1 in sets)
# a= {1,2,3,4,5}
# a.add('w')
# a.remove(1)
# a.pop()
# a.clear()
# print(a)
sets = {'a', 's', 'e', 'q', 'a', 1,'1', '1'}
s1={1,2,3,4,5}
print(set(sets))
c = sets.intersection(s1)
d=sets.union(s1)
print(c)
print(d)