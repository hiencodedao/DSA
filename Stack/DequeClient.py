from Deque import * 

queue = Deque(10)

for i in range(5):
        queue.insertLeft(i)

queue.insertRight(5)
# queue.insertLeft(1)
# queue.insertRight(2)
# queue.insertLeft(3)
# queue.insertRight(4)
# queue.insertLeft(5)
# queue.insertRight(6)

print("Queue after insert: ", queue)

