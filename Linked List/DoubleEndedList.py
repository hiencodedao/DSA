from LinkedList import * 

class DoubleEndedList(LinkedList):
    def __init__(self):
        self.__first = None
        self.__last = None

    def getFirst(self): 
        return self.__first

    def setFirst(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
            if (link is None or self.getLast() is None):
                self.__last = link
        else: 
            raise Exception("First link must be None or Link")

    def getLast(self): 
        return self.__last

    def last(self): 
        # Take out the item of the last link rather than the link it self
        if self.isEmpty():
            raise Exception("The link is empty")
        return self.__last.getData()

    def insertLast(self, datum):
        if self.isEmpty():
            return self.insert(datum)
        link = Link(datum, None)
        self.__last.setNext(link)
        self.__last = link

    def insertAfter(self, goal, newDatum, key=identity):
        # Insert a new datum after the goal
        # Link with a matching key
        link = self.find(goal, key)
        if link is None: 
            return False
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        if link is self.__last:
            # To check if Link is the last Link, update the last pointer to newLink
            self.__last = newLink
        return True
        
    def delete(self, goal, key=identity):
        # Delete the first link on the list with the matching key
        if self.isEmpty(): 
            raise Exception("Cannot delete from empty list")
    
        previous = self
        while previous is not None:
            link = previous.getNext()
            if key(link.getData()) == goal:
                if previous is self.__last:
                    self.__last = previous
                previous.setNext(link.getNext())
                return link.getData()
            previous = link

        raise Exception("Cannot find the item with matching key")

    
        
