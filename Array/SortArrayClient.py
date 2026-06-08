from SortArray import *
import timeit
import random

def initArray(size=14, maxValue=100, seed=3.14159): 
    arr = Array(size)
    random.seed(seed)

    # for i in range(size): 
    #     arr.insert(random.randrange(maxValue))

    for i in [1,2,2,6,2,3,4,5,6,8,7,6,9,10]:
        arr.insert(i)
    
    return arr

arr = initArray()
# print("Array containing: ", len(arr), "items: \n", arr)

# for test in [
#     'initArray().bubbleSort()',
#     'initArray().selectionSort()',
#     'initArray().insertionSort()',
#     'initArray().twoWayBubbleSort()'
# ]:
#     elapsed = timeit.timeit(test, number=100, globals=globals())
#     print(test, "took", elapsed, "seconds", flush=True) 

# arr.twoWayBubbleSort()
# print('Sorted array contain:\n', arr)

# arr.deduplicate()
# print('Deduplicate array after sort: \n', arr)

arr.insertionSortDedup()
print('Sorted array contain:\n', arr)

