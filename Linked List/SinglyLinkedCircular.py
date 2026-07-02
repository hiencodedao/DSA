import LinkedList

def identity(x): return x[1]

class Link(LinkedList.Link):
    def __init__(self, datum, next=None):
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

class SinglyLinkedList(LinkedList.LinkedList):
    def __init__(self): 
        self.__last = None

    def getLast(self):
        return self.__last

    def setLast(self, link):
        if link is not None or isinstance(link, Link):
            self.__last = link
        else:
            raise Exception('Last link must be None or Link')

    def getNext(self):
        return self.getFirst()

    def getFirst(self):
        if self.isEmpty():
            raise Exception('List is empty')
        elif self.__last.getNext() is None:
            first = self.__last
        else:
            first = self.__last.getNext()
        return first

    def insertFirst(self, datum): 
        new = LinkedList.Link(datum, None)
        if self.isEmpty():
            self.__last = new
        else:
            new.setNext(self.getFirst())
            self.__last.setNext(new)
        return True

    def insertLast(self, datum):
        new = LinkedList.Link(datum, None)
        if self.isEmpty():
            self.__last = new
        else:
            new.setNext(self.getFirst())
            self.__last.setNext(new)
            self.__last = new
        return True

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception('Cannot delete from an empty list')
        elif self.getFirst().getNext() is None: 
            self.__last = None
        else:
            deleteData = self.getLast().getNext().getData()
            self.getLast().setNext(self.getFirst().getNext())

        return deleteData

    def search(self, goal, key=identity): 
        # Find the first item whose key matches the goal
        link = self.find(goal, key)
        if link is not None:
            return link.getData()

    def isEmpty(self):
        return self.__last is None

    def __str__(self):
        ans = '['
        link = self.__last.getNext()
        flag = True
        while flag:
            if len(ans) > 1: 
                ans += ', '
            ans += str(link.getData())
            if link is self.__last:
                flag = False
            else: 
                link = link.getNext()
        ans += ']'
        return ans

    def step(self): 
        # Move __last to the next link
        if self.isEmpty():
            raise Exception('List is empty')
        if self.__last.getNext() is None:
            raise Exception('List is contain just 1 link')
        else: 
            self.__last = self.__last.getNext()
        
    def seek(self, goal, key=identity):
        if self.isEmpty():
            raise Exception('List is empty')
        else:
            link = self.__last.getNext()
            while link is not self.__last:
                if key(link.getData()) == goal:
                    self.__last = link
                else:
                    link = link.getNext()
        return link

# queue = SinglyLinkedList()

# for i in [(1, 'Hien'), (2, 'Phuong'), (3, 'Quy'), (4, 'Binh')]:
#     queue.insertLast(i)
# print('The queue contains: ', queue)

# queue.insertFirst((5, 123412341))
# print('Queue after insert fifth link: ', queue)

# print('Deleting first link: ', queue.deleteFirst())
# print('Queue after delete first link ', queue)



            
        
