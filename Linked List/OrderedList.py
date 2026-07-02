from DoubleEndedList import *

class OrderedList(DoubleEndedList):
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

    def find(self, goal):
        link = self.getFirst()
        while (link is not None and 
                self.getKey(link.getData()) < goal):
            link = link.getNext()
        return link

    def search(self, goal):
        link = self.find(goal)
        if (link is not None
            and self.getKey(link.getData()) == goal):
            return link.getData()

    def insert(self, datum):
        goal = self.getKey(datum)
        previous = self
        while (previous.getNext() is not None
                and self.getKey(previous.getNext().getData()) < goal):
                previous = previous.getNext() 

        newLink = Link(datum, previous.getNext())
        previous.setNext(newLink)

    def delete(self, goal): 
        if self.isEmpty():
            raise Exception("Cannot delete from empty list")
        
        previous = self
        while (previous.getNext() is not None
                and self.getKey(previous.getNext().getData()) < goal):
                previous = previous.getNext()

        if (goal != self.getKey(previous.getNext().getData())
            or previous.getNext() is None):
            raise Exception('No datum with matching key found '
            'in the list')
        
        toDelete = previous.getNext()
        previous.setNext(toDelete.getNext())

        return toDelete.getData()

    



