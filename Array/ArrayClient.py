import Array
max_size = 7

arr = Array.Array(max_size)

arr.insert(2)
arr.insert(1)
arr.insert(4)
arr.insert(5)
arr.insert(5)
arr.insert(5)

arr.insert("Tao la bo chung may")

# print("This is the maximum value: ", arr.deleteMaxNum())

# print(f"This is the index of element 4: {arr.get(4)}")

# arr.set(3, 19)

arr.traverse()

# arr.__len__()

# orderArr = Array.Array(max_size)

# while len(arr) > 0:
#     x = arr.deleteMaxNum()
#     if x is None:
#         break
#     if isinstance(x, (int, float)):
#         orderArr.insert(x)

# print("This is the ordered array: ")
# orderArr.traverse()

orderArr = arr.removeDuplicate(arr)
print("This is result of removeDuplicate method:")
orderArr.traverse()
