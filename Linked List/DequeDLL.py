from DoublyLinkedList import *

class Deque(DoublyLinkedList): 
    def __init__(self): 
        self.__first = None
        self.__last = None

    def getFirst(self): return self.__first
    def getLast(self): return self.__last

    def setFirst(self, link): 
        if link is None or isinstance(link, Link):
            self.__first = link
            if (self.__last is None):
                self.__last = link
        else:
            raise Exception('First link must be None or Link')
    
    def setLast(self, link):
        if link is None or isinstance(link, Link):
            self.__last = link
            if self.__first is None:
                self.__first = link
        else:
            raise Exception('Last link must be None or Link')

    insertLeft = DoublyLinkedList.insertFirst
    insertRight = DoublyLinkedList.insertAfter
    removeLeft = DoublyLinkedList.deleteFirst
    removeRight = DoublyLinkedList.deleteLast
    peekLeft = getFirst
    peekRight = getLast
    isEmpty = DoublyLinkedList.isEmpty

queue = Deque()

for i in range(5):
    if i%2 ==0:
        queue.insertFirst(i)
    else:
        queue.insertLast(i)

print('The queue after insert: ', queue)

print('Deleting element: ', queue.deleteFirst(), 
    '\nQueue remains: ', queue)

print('Deleting element: ', queue.deleteLast(), 
    '\nQueue remains: ', queue)


        