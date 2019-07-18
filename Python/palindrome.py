str = input("Enter a word to check for palindrome: ")
print(str[0])
print("".join(reversed(str))) #iterator reversed iterates over the string in reverse direction and join merges the characters
z=[]
y=str[::-1]
print(y)
if(str == "".join(reversed(str))):
    print("Palindrome")
else:
    print("Not a Palindrome")