def myMessage():
    return "Hello.."

x=myMessage()
print(x)

def add(x,y):
    return x+y

print(add(3,4))
print(add("Jitendra", " Dubey"))

## Keyword Argument Function

def showData(name, age):
    print("Name: ", name)
    print("Age: ", age)

showData("Sanjay", 12)
showData(12, "Sanjay")
showData(age=12, name = "Sanjay") #passing the value in keywords as used in function definition

#Default value Argument

def calculateSI(p,n, r=5):  # the default argumentss must be in order from right to left. e.g calculateSI(p,n=5,r) is not allowed
    return (p*n*r/100)

print(calculateSI(1000,5))
print(calculateSI(1000, 10, 10))

#Variable number of arguments

def showFriends(*friends):
    print(friends[0:-1])
    print(friends)
    print("------")
    for value in friends:
        print(value.capitalize(), end= ", ")

showFriends("raju", "jaya", "mohan", "sonali")