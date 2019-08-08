def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)


print(mydoubler)
print(mytripler)
print(mydoubler(1)) 
print(mytripler(4))
