def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    counter = 0

    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, counter))
            counter = 0
        prevChar = char
        counter += 1

    encodedList.append((prevChar, counter))
    return encodedList



#def decodeString(encodedList):



print(encodeString('AAAAABBBBAAA'))

print(encodeString('AAAAABBBBABA'))


#decodeString(Bookkeeping)