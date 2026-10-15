list = [1,2,3,4,5,6,7,8,9,0,255]
p = bytes(list)
print(type(p))

list = [1,2,3,4,5,6,7,8,9,0,255]
p1 = bytearray(list)
print(type(p1))


list2 = [1,2,3,4,5]
p3 = bytearray(list2)
p3[1] = 20
print(p3[1])