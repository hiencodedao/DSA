# Stack and Queue that implement based on Singly Linked Circular List

from SinglyLinkedCircular import *

class Queue(SinglyLinkedList):
    def __init__(self):
        self.__last = None

    push = SinglyLinkedList.insertLast
    pop = SinglyLinkedList.deleteFirst
    peek = SinglyLinkedList.getFirst

    def isEmpty(self):
        return self.__last is None

queue = Queue() 

for i in [(1, 'Hien'), (2, 'Phuong'), (3, 'Quy'), (4, 'Binh')]:
    queue.push(i)

queue.pop()
    
print('Queue contains: ', queue)
