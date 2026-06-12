class Deque(object): 
    def __init__(self, size):
        self.__maxSize = size
        self.__que = [None] * self.__maxSize
        self.__left = 0
        self.__right = 1
        self.__nItems = 0

    def insertLeft(self, item): 
        if self.isFull(): 
            raise Exception("Queue is full")
        self.__left += 1
        if self.__left == self.__maxSize: 
            self.__left = 0
        self.__que[self.__left] = item
        self.__nItems += 1
        return True
    
    def insertRight(self, item):
        if self.isFull():
            raise Exception("Queue is full")
        self.__right -= 1
        if self.__right < 0: 
            self.__right = self.__maxSize - 1
        self.__que[self.__right] = item
        self.__nItems += 1
        return True
    
    def removeLeft(self): 
        if self.isEmpty(): 
            raise Exception("Queue is empty")
        removeItem = self.__que[self.__left] 
        self.__que[self.__left] = None
        self.__left -= 1
        if self.__left < 0: 
            self.__left == self.__maxSize - 1
        self.__nItems -= 1

        return removeItem

    def removeRight(self): 
        if self.isEmpth():
            raise Exception("Queue is empty")
        removeItem = self.__que[self.__right] 
        self.__right += 1 
        if self.__right == self.__maxSize:
            self.__left = 0
        self.__nItems -= 1

        return removeItem 

    def peekLeft(self):
        return self.__que[self.__left]

    def peekRight(self):
        return self.__que[self.__right]

    def isFull(self): 
        return self.__nItems == self.__maxSize
    
    def isEmpty(self):
        return self.__nItems <= 0

    def __len__(self): 
        return self.__nItems

    def __str__(self): 
        ans = "["
        if self.__left > self.__right:
            for i in range (self.__left, self.__right - 1, -1): 
                if len(ans) > 1: 
                    ans += ", "
                ans += str(self.__que[i]) 
        else: 
            a = self.__left 
            while a <= self.__left or a >= self.__right:
                if len(ans) > 1: 
                    ans += ", "
                if a == 0: 
                    ans += str(self.__que[a])
                    a = self.__maxSize - 1
                elif a > 0: 
                    ans += str(self.__que[a])
                    a -= 1
                elif a < self.__maxSize:
                    ans += str(self.__que[a])
                    a -= 1
        ans += "]"
        return ans

        