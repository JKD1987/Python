def isPalindrome(x):
    y=x[::-1]
    if(x==y):
        return True
    else:
        return False

#Simple lambda function
x=lambda a:a*2
y=lambda a:a*a
num = int(input("Enter a number"))
print(x(num))
print(y(num))

#Lambda with filter
li=[2,3,4,5,6,7,8,9]
newList = list(filter(lambda x:(x%2 ==0), li))
print(newList)

lis=["abc", "abcba", "def", "rar"]
palindrome_list = list(filter(lambda x: (x==x[::-1]), lis))
print(palindrome_list)

#lambda with map
li1= [2,3,4,5,6,7,8,9]
newList1 = list(map(lambda x:x*x, li1))
print(newList1)

