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


myTuple = [('W', 5),('1', 2),('G', 3)]
def decodeString(encodedList):
    decodedString = ''
    for elem in encodedList:
        decodedString = decodedString + elem[0] * elem[1] 
    return decodedString




print(encodeString('AAAAABBBBAAA'))

print(encodeString('BookKeeping'))


print(decodeString(myTuple))