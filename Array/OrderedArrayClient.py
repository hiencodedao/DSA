from OrderedArray import *

maxSize = 1000
arr = OrderedArray(maxSize)

arr.insert(77) # Insert 11 items
arr.insert(99)
arr.insert(44) # Inserts not in order
arr.insert(55)
arr.insert(0)
arr.insert(12)
arr.insert(44)
arr.insert(99)
arr.insert(77)
arr.insert(0)
arr.insert(3)

print("Array containing: ", len(arr), "items:", arr)
