from re import L
import LinkedList

def identity(x): return x

class Link(LinkedList.Link):
    def __init__(self, datum, next=None, previous=None): 
        self.__data = datum 
        self.__next = next 
        self.__previous = previous

    def getData(self): return self.__data
    def getNext(self): return self.__next
    def getPrevious(self): return self.__previous
    def setData(self, d): self.__data = d
    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception('Next link must be None or Link')
    def setPrevious(self, link):
        if link is None or isinstance(link, Link):
            self.__previous = link
        else:
            raise Exception('Previous link must be None or Link') 

class DoublyLinkedList(LinkedList.LinkedList):
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

    def traverseBackwards(self, func=print):
        link = self.getLast()
        while link is not None: 
            func(link)
            link = link.getPrevious()

    def insertFirst(self, datum):
        newLink = Link(datum, next=self.getFirst())
        if self.isEmpty(): 
            self.setLast(newLink)
        else:
            self.getFirst().setPrevious(newLink)
            self.setFirst(newLink)

    def insertLast(self, datum):
        newLink = Link(datum, previous=self.getLast())
        if self.isEmpty():
            self.setFirst(newLink)
        else: 
            self.getLast().setNext(newLink)
            self.setLast(newLink)

    insert = insertFirst
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception('Cannot delete from an empty list')
        first = self.getFirst()
        self.setFirst(first.getNext())
        if first.getNext():
            first.getNext().setPrevious(None)
        return first.getData()

    def deleteLast(self):
        if self.isEmpty(): 
            raise Exception('Cannot delete from an empty list')
        last = self.getLast()
        self.setLast(last.getPrevious())
        if self.getLast():
            self.getLast().setNext(None)
        return last.getData()

    def insertAfter(self, goal, datum, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        if link.isLast():
            self.insertLast(datum)
        else:
            newLink = Link(datum, previous=link, next=link.getNext())
            link.setNext(newLink)
            link.getNext().setPrevious(newLink)
            return True

    def delete(self, goal, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        if link is self.__last:
            self.deleteLast()
        elif link is self.__first:
            self.deleteFirst()
        else: 
            link.getPrevious().setNext(link.getNext())
            link.getNext().setPrevious(link.getPrevious())
        return link.getData()
            
        





























            
        