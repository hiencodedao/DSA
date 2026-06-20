class linkedList(object): 
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
        