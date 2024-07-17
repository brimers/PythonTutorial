# Python code​​​​​​‌​‌‌​‌​‌​‌‌​‌​‌​‌​‌‌​‌​​‌ below

'''
This challenge was designed to make me use functions, controls, operators to determine the factorial of a given num
Also test the edge cases of using an input that is not an int (String), a negative int and catch the case 0! which is just 1
'''

def factorial(num):
    # Your code goes here.
    if (type(num) != int) or (num < 0):
        return "None"
    else:
        if num == 0:
            return 1
        return num * (factorial(num - 1))
    
# should return none
print(factorial(-1))

# should return none
print(factorial("Spam"))

# should return 1
print(factorial(0))

# should return 120
print(factorial(5))