# # from LinkedList import *

# # myList = LinkedList()

# # for i in range(5): 
# #     myList.insert(i) 

# # it = myList.iterator()
# # print('Created an iterator', it)

# # while it.hasMore(): 
# #     print('The next item is: ', it.next())
# # print('End of iterator')

# def Fibonacci(): 
#     previous = 0
#     current = 1
#     while True:
#         yield current
#         next = previous + current
#         previous = current
#         current = next

# iter = Fibonacci()
# print(iter)
# for i in range(10):
#     print(iter.__next__())

from LinkedList import *

queue = LinkedList() 

for i in range(5):
    queue.insert(i)

print(queue)
    

