'''
Challenge: Write a fxn that converts a param hex value (type string) into a decimal without using the int()
Output: the decimal value of the hex value or 'None' if the value is not a valid hex value
'''

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDecimal(hexnum):
    string = hexnum.upper()
    for s in string:        
        print(s)
        if s not in hexNumbers:
            print('None')
        else:
            print('Yes')

hexToDecimal('blah')
hexToDecimal('b')
hexToDecimal('A1')
hexToDecimal('xxx')

