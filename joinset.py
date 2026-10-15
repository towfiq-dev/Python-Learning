joinset = {1,2,3,'g',4,5}
joinset2 = {6,7,8,'r9',0}
set3 = joinset.union(joinset2)
print(set3)
joinset2.update(joinset)
print(joinset2)