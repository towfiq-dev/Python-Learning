# def myFun(a, b):
#   sum = (a + b)
#   print(sum)

# myFun(3, 5)

# def myFun(x,y):
#   sum = (x+y)
#   print(sum)
# myFun(5,5)

# def myFun3():
#   print("Hablu")
#   myFun3()

# myFun3()

# def myFunc(a, b):
#   c = (a+b)
#   print(c)
  
# myFunc(2,4)

# def myFunc2():
#   return "Hello"
# result = myFunc2()
# print(result)

# def additions(a,b):
#   result = (a+b)
#   return result

# r = additions(5,5)
# print(r)

# def mulAdd(*Arms):
#   print(Arms)
#   return sum(Arms)
# r = mulAdd(1,2,3,4,5)
# print(r)
# def myFunc4(fName, lName, age):
#     print(f"my name is {fName} {lName} and I am {age} years old.")
  
# myFunc4(age=23, fName="Towfiqul", lName='Islam')
# def myFunc5(**arms):
#   print(arms)
# myFunc5(age=23, fName="Towfiqul", lName='Islam', marks=34)

def myFunc6(**data):
  print(data)
  print(f"my name is {data['fName']} {data['lName']} and I am {data['age']} years old.")
myFunc6(age=23, fName="Towfiqul", lName='Islam', marks=34)
