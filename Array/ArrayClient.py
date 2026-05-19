import Array
max_size = 5

arr = Array.Array(max_size)

for i in range(5):
    arr.insert(i)

print(f"This is the index of element 4: {arr.get(4)}")

arr.set(3, 19)

arr.traverse()

arr.__len__()

