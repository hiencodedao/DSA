import Array
max_size = 7

arr = Array.Array(max_size)

for i in range(5):
    arr.insert(i)

arr.insert("Tao la bo chung may")
arr.insert(-6)

# print(f"This is the index of element 4: {arr.get(4)}")

# arr.set(3, 19)

arr.traverse()

# arr.__len__()

print("This is the max number in the array and delete it:", arr.deleteMaxNum())

arr.traverse()
