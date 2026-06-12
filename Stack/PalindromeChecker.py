from SimpleStack import *

pal = input("Enter your string here to check if it's palindrome or not: ")
pal = pal.lower()

stack = stack(max=len(pal))
compare = ""

for index, letter in enumerate(pal): 
    if isinstance(letter, str): 
        stack.push(letter)
        compare += letter

flag = True
for i in range(len(pal)):
    if compare[i] != stack.pop(): 
        flag= False
        print("The string is NOT palindrome")
        break
if flag:
    print("The string IS palindrome")
    

