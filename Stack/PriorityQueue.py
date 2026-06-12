def identity(x): return x 

class PrioritizeQueue(object):
    def __init__(self, size, pri=identity): 
        self.__maxSize = size
        self.__que = [None] * size
        self.__pri = pri
        self.__nItems = 0

    def insert(self, item): 
        if self.isFull(): 
            raise Exception("The queue is full") 
        j = self.__nItems - 1
        while j >= 0 and self.__pri(item) >= self.__pri(self.__que[j]): 
            self.__que[j+1] = self.__que[j]
            j -= 1
        self.__que[j+1] = item
        self.__nItems += 1

        return True
    
    def remove(self): 
        if self.isEmpty(): 
            raise Exception("The queue is empty")
        self.__nItems -= 1
        front = self.__que[self.__nItems]
        self.__que[self.__nItems] = None 
        return front

    def peek(self): 
        if not self.isEmpty(): 
            return self.__que[self.__nItems-1]
        else: 
            return None

    def isEmpty(self): return self.__nItems == 0

    def isFull(self): return self.__nItems >= self.__maxSize

    def __len__(self): return self.__nItems

    def __str__(self): 
        ans = '['
        for i in range(self.__nItems - 1, -1, -1): 
            if len(ans) > 1: 
                ans += ', ' 
            ans += str(self.__que[i])
        ans += ']'
        return ans
    


