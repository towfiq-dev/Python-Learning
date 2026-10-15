newTuple = ('a', 's', 'd', 'q', 'e')
# result= list(newTuple)
# print(type(result))
# result.append('new')
# print(result)
# newTuple = tuple(result)
# print(newTuple)
(z,*x) = newTuple
print(z)