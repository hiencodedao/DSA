from SimpleStack import *

stack = stack(100)

expr = input("Input string to check: ")

errors = 0

for pos, letter in enumerate(expr): 
    if letter in "{ [ (": 
        if stack.isFull():
            raise Exception('Stack overflow exception')
        else:
            stack.push(letter)

    if letter in "} ] )":
        if stack.isEmpty(): 
            print("Error:", letter, "at position", pos, "has no matching left delimiter")   
            errors += 1
        else:
            left = stack.pop()
            if not (
                left == "{" and letter == "}" or
                left == "[" and letter == "]" or 
                left == "(" and letter == ")"): 
                print("Error", letter, "at position", pos, "does not match left delimiter", left) 
                errors +=  1

if stack.isEmpty() and errors == 0:
    print("Delimeters balance in expression", expr)     

elif not stack.isEmpty():
    print("Expression missing right delimeter for ", stack)           



    