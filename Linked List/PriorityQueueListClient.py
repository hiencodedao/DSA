from PriorityQueueList import *

queue = PriorityQueueList()

for i in range(5):
    queue.insert(i)

print('The queue after insert: ', queue)

print('The priority value is: ', queue.peek())

while not queue.isEmpty():
    print('Removing the priority link: ', queue.removePriority(),
    '\nQueue remains: ', queue)
