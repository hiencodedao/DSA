from OrderedList import *

def identity(x): return x

class PriorityQueueList(OrderedList):
    def __init__(self, key=identity):
        self.__first = None
        self.__key = key

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else: 
            raise Exception('First link must be Link or None')

    def getFirst(self):
        return self.__first

    def getKey(self, datum):
        return self.__key(datum)

    def peek(self): 
        if self.isEmpty(): 
            raise Exception('List is empty')
        else:
            return self.getFirst().getData()

    def removePriority(self):
        if self.isEmpty():
            raise Exception('List is empty')
        firstLink = self.getFirst() 
        self.setFirst(firstLink.getNext())
        return firstLink