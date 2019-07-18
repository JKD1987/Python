mySet = set(["Apple", "Guava", "Banana", "Mango"])

for item in mySet:
    print(item, end=", ")
print()

mySet.add("Apple")
mySet.add("Pine Apple")
print(mySet)

newSet = mySet.copy()
print(newSet)
print("On POP:")
newSet.pop()
print(newSet)
newSet.clear()
print("After Clear:")
print(newSet)

mySet.remove("Mango")
print(mySet)
message = "Hello World"
data = set(message.split(" "))
print(data)

lst = [1, 2.5, "Apple", 1]
set1 = set(lst)
for item1 in set1:
    print(item1, end=", ")
print()

lst2 = list(set1)
print(lst2)