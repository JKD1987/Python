#String Function Handling
message = "hello! how are you all!!"

print("Default Message: ", message)
print("Message length: ", len(message))
print("Capitalized first letter: ", message.capitalize())
print("Message in upper case: ", message.upper())
print("Message in Lower case: ", message.lower())
print("Message aligned to center: ", message.center(len(message)+20, '-'))
#-------------------
print(message.endswith('all!!',3, len(message)))
print(message.endswith('all'))
print(message.find('how', 12, len(message)))
print(message.find('how'))
print(message.replace('helllo', 'hi'))
print(message.startswith('hello'))
print("Right Justiification: ", message.rjust(len(message)+20, '-'))
print("Left  Justiification: ", message.ljust(len(message)+20, '-'))

myList=message.split(' ')
print(myList)
print(len(myList))
for x in myList:
    print(x)
for indx in range(0,len(myList)):
    print(myList[indx])

