from LinkQueue import * 

queue = Queue() 

print("Initializing queue type ", type(queue), 
"is empty ", queue.isEmpty())

for i in range(5):
    queue.enqueue(i**2)

print('After inserting ', len(queue), ' squares onto the queue',
' it contains ', queue)
print('The front of the queue is ', queue.peek())

while not queue.isEmpty():
    print('Removing ', queue.dequeue(), ' from the queue',
    'leaves ', len(queue), 'items: ', queue)