#Strings - Sequence of characters. They are immutable.
a = "this is my book"
print(id(a)) # the variable is pointing to one location
#a[0] = 'x' -- not allowed as strings are immutable in python.
a = a + "also." #This doesnt mean the string a has been modified. Instead variable a has been assigned to a different string in memory.
#interpreter makes a copy of the original string, appends the new value to it andd drops the old string.
print(id(a)) #  The variable is pointing to a different location. 

#Lists - need not be homogeneous. A single list can contain strings, integers as well as objects. Lists are mutable.
l=[1,'apple', 1+1] # notice square brackets
print(l, id(l))
l.append('I am a boy')
print(l, id(l))
l.pop()
print(l, id(l))

#tuples - Like lists, except that they are immutable.
tup = (1,'apple', 1+1)# notice round brackets
print(tup)
print(tup[1])
tup[0] = 2

