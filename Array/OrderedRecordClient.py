from OrderedRecordArray import *

def second(x):
    return x[1]
maxsize = 10

key_fn = lambda x : x[1] 

firstArr = OrderedRecordArray(10, key = key_fn)

for rec in [('a', 3.1), ('b', 7.5)]:
            firstArr.insert(rec)

secondArr = OrderedRecordArray(10, key = key_fn)

for rec in [('j', 6.0), ('i', 7.5)]:
            secondArr.insert(rec)

# print("Array containing: ", len(arr), " records including:\n", arr)

# for rec in [('c', 6.0), ('g', 0.0), ('g', 0.0), 
#             ('b', 7.5), ('i', 7.5)]:
#     print("Deleting ", rec, " return ", arr.delete(rec))

# print("Array containing: ", len(arr), " records including:\n", arr)

# for key in [4.4, 6.0, 7.5]:
#     print("Find key return ", arr.find(key), "\nAnd Get key", arr.get(arr.find(key)))

orderArr = firstArr.merge(secondArr, key_fn)
print(type(orderArr))
# print("This is the merged array: ")
orderArr.traverse()