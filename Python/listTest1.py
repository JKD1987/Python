lst = ["Apple", "Mango", "Guava", "Apple"]
print("original list: ", lst)
print("Number of elements in my list = %d" %len(lst))
lst.append("Banana")
print("List after append: ", lst)
lst.insert(3,"Watermelon")
print("List after insert: ", lst)
lst.remove("Apple")
print("List after remove: ", lst)

for item in lst:
    print(item, end="..")
print()

print(lst.index("Guava"))
print(lst.index("Apple",3,len(lst)))
lst1 = lst.copy()
print(lst == lst1)
lst1.sort()
print(lst1)
lst1.reverse()
print(lst1)

lst1.append("Apple")
print(lst1)
print(lst1.count("Apple"))
