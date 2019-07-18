str1 = input("Enter first String: ")
str2 = input("Enter Second String: ")

if(len(str1) != len(str2)):
    print("Not Anagrams.")
else:
    n1=len(str1)
    n2=len(str2)

    #method1 - using Sorting
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)
    if(sortedStr1 == sortedStr2):
        print("Anagrams.")
    else:
        print("Not Anagrams.")

    #method2 - counting number of characters
    list = [0]*256
    for indx in range(0,n1):
        list[ord(str1[indx])] = list[ord(str1[indx])]+1 # On occurrance of a character in string 1, increase the list count
        list[ord(str2[indx])] = list[ord(str2[indx])]-1 # On occurrence of same character in String2, decrease the list count
    for id in range(0,255):
        if(list[id] != 0):
            print("Not Anagrams..")
            break
    else:
        print("Anagrams..")

    #method 3 - XOR XOR 0f even number of occrances must be zero
    value =0
    for indx in range(0,n1):
        value = value ^ ord(str1[indx])
        value = value ^ ord(str2[indx])
    if(value == 0):
        print("Anagrams...")
    else:
        print("Not Anagrams...")
