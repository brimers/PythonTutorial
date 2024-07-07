'''
Challenge: Write a fxn that converts a param hex value (type string, max 3 characters) into a decimal without using the int()
Output: the decimal value of the hex value or 'None' if the value is not a valid hex value or greater than 3 characters

Lingering questions:
I need to check two conditions 
1. is the param of 3 or less characters?
    if yes then check for acceptable hex values
    if no then break
2. are all the characters in the param an acceptable hex value?
    similar but repectively opposite outcomes to above

which one would i need to check first to short function?

Future Considerations:

making the function more dynamic:

-revising the function to accept vairable length input
-

'''

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

'''
INITIAL ATTEMPT:

This failed bc I forgot the nature of the for loop will iterate through the loop as many times as there 
are characters in the value which explains why when i passed A1 it would print out 161 twice



    print("hex num given is " + hexnum)
    string = hexnum.upper()
    strlen = len(string)

    if not len(string) in range(4):
        return print("Too many characters in string")
    else:
        for s in string:
            print("enter loop: " + hexnum)
            if s in hexNumbers:
                if strlen == 3:
                    print((hexNumbers[string[0]] * 256)  + (hexNumbers[string[1]] * 16) + (hexNumbers[string[2]] * 1))
            
                elif strlen == 2:
                    print((hexNumbers[string[0]] * 16) + (hexNumbers[string[1]] * 1))
            
                else: 
                    print((hexNumbers[string[0]] * 1))
            else:
                print("Value given is not a hex value")
                break
            

hexToDecimal('blah')
hexToDecimal('b')
hexToDecimal('bc')
hexToDecimal('A1')
hexToDecimal('xxx')


hex num given is blah
Too many characters in string
hex num given is b
enter loop: b
11
hex num given is bc
enter loop: bc
188
enter loop: bc
188
hex num given is A1
enter loop: A1
161
enter loop: A1
161
hex num given is xxx
enter loop: xxx
Value given is not a hex value


'''