#Memory Handling
x="ABC"
y="def"
print(x,y)
del(x)
print(x)
x=55 # this assignment will fail as print in above line ran into exception. If we comment above line, this assignment will work
print(x)