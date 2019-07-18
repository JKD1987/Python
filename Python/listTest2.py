lst1 = [1,2,3]
lst2=[4,5,6]

print(lst1+lst2)
lst3=lst1+lst2
print(lst3)
print(lst3[::-1])
print(lst3[2::-1])
print(lst3[2:-1])
print(lst3)

txt=list("Hello! How are you?")
print(txt)
txt.extend(lst3)
print(txt)


