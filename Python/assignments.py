a=10
print("value of a=", a)
b=c=a=5
print(a,b,c)
a,b,c=6, 24.122,"three"
print(a,b,c)
print(a, end=" ") # 'end' helps us how to separate the  next output display. In this case its a space.
print (b, end=' ')
print(c)
print(a, end="\n")
print (b, end=' ')
print(c)