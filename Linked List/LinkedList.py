def identity(x): return x

class Link(object): 
    def __init__(self, datum, next = None):
        self.__data = datum
        self.__next = next 

    def getData(self): 
        return self.__data

    def setData(self, datum): 
        self.__data = datum

    def getNext(self):
        return self.__next

    def setNext(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else: 
            raise Exception("Next link must be Link or None")

    def isLast(self): 
        return self.__next is None

    def __str__(self): 
        return str(self.__data)

class LinkedList(object): 
    def __init__(self): 
        self.__first = None

    def getFirst(self):
        return self.__first

    def setFirst(self, link):
        if link is None or isinstance(link, Link): 
            self.__first = link
        else: 
            raise Exception("First link must be Link or None")

    def getNext(self): 
        return self.getFirst()

    def setNext(self, link):
        self.setFirst(link)

    def isEmpty(self):
        return self.getFirst() is None

    def first(self):
        if self.isEmpty():
            raise Exception("List is empty")
        else: 
            return self.getFirst().getData()

    def traverse(self, func=print):
        link = self.getFirst()
        while link is not None: 
            func(link)
            link = link.getNext()

    def __len__(self):
        link = self.getFirst()
        count = 0
        while link is not None:
            count += 1
            link = link.getNext()
        return count

    def __str__(self):
        ans = "["
        link = self.getFirst()
        while link is not None:
            if len(ans) > 1: 
                ans += ", "
            ans += str(link)
            link = link.getNext() 
        ans += "]"
        return ans

    def insert(self, datum):
        link = Link(datum, self.getFirst()) 
        self.setFirst(link)

    def find(self, goal, key=identity): 
        # Find the first link whose key matches the goal
        link = self.getFirst()
        while link is not None: 
            if key(link.getData()) == goal:
                return link
            link = link.getNext()
    
    def search(self, goal, key=identity): 
        # Find the first item whose key matches the goal
        link = self.find(goal, key)
        if link is not None:
            return link.getData()

    def insertAfter(self, goal, newDatum, key=identity): 
        # Insert a new datum after the goal
        # Link with a matching key
        link = self.find(goal, key)
        if link is None:
            return False
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        return True

    def deleteFirst(self): 
        if self.isEmpty(): 
            raise Exception("Cannot delete from empty list")
      
        first = self.getFirst()
        self.setFirst(first.getNext())
        return first.getData() 

    def delete(self, goal, key=identity): 
        # Delete the first link from the list whose key matches the goal
        if self.isEmpty(): 
            raise Exception("Cannot delete from empty list")
        
        previous = self
        while previous is not None:
            link = previous.getNext()
            if key(link.getData()) == goal:
                previous.setNext(link.getNext())
                return link.getData()
            previous = link

        raise Exception("Cannot find the Link that match the goal")

    