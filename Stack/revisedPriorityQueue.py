def identity(x): return x 

class PrioritizeQueue(object):
    def __init__(self, size, pri=identity): 
        self.__maxSize = size
        self.__que = [None] * size
        self.__pri = pri
        self.__nItems = 0

    def insert(self, item):
        if self.isFull(): 
            raise Exception("The question is full")
        self.__que[self.__nItems] = item
        self.__nItems += 1
        
        return True

    def remove(self):
        if self.isEmpty(): 
            raise Exception("The queue is empty")
        j = self.__nItems - 1
        highest_pri = self.__que[j] 
        while j>0 and self.__pri(self.__que[j]) > self.__pri(self.__que[j-1]): 
            highest_pri = self.__que[j-1]
            j -= 1
        for k in range(j-1, self.__nItems - 1):
            self.__que[k] = self.__que[k+1]
        self.__nItems -= 1
        
        return highest_pri

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
        for i in range(self.__nItems): 
            if len(ans) > 1: 
                ans += ', ' 
            ans += str(self.__que[i])
        ans += ']'
        return ans
    


