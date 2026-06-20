class Link(object): 
    def __init__(self, datum, next = None):
        self.__data = datum
        self.__next = next 

    def getData(self): 
        return self.__datum 

    def setData(self, datum): 
        self.__datum = datum

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

