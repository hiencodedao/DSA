class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if n >= 0 and n <= self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if n >= 0 and n <= self.__nItems:
            self.__a[n] = value
        
    def insert(self, item): 
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def search(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item: 
                return i
        return None

    def find(self, item):
        for j in range (self.__nItems):
            if self.__a[j] == item:
                return j
            else:
                return -1

    def delete(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                self.__nItems -= 1
                for k in range(i, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True
            return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def getMaxNum(self):
        if self.__nItems != 0:
            max_num = self.__a[1]
            for j in range(self.__nItems): 
                if isinstance(self.__a[j], (int, float)) and self.__a[j] > max_num:
                    max_num = self.__a[j]
            return max_num
        else:
            return None

    def deleteMaxNum(self):
        if self.__nItems != 0:
            max_num = self.__a[1]
            for j in range(self.__nItems): 
                if isinstance(self.__a[j], (int, float)) and self.__a[j] > max_num:
                    max_num = self.__a[j]
            self.delete(max_num)
            return max_num
        else:
            return None
                