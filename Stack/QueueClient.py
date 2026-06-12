from Queue import * 

queue = Queue(10)

for person in ['Don', 'Ken', 'Ivan', 'Raj', 'Amir', 'Adi']: 
    queue.insert(person)

print ('After inserting: ', len(queue), 'person on the queue:\n', queue) 
print('Is the queue full?', queue.isFull())

print('Removing item from the queue:')
while not queue.isEmpty(): 
    print(queue.remove(), end=' ')
print()