from nt import remove


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
        return -1

    def delete(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                self.__nItems -= 1
                for k in range(i, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                self.__nItems -= 1
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def deleteMaxNum(self):
        if self.__len__() != 0: 
            maxNum = self.__a[0]
            for j in range(self.__len__()):
                if isinstance(self.__a[j], (float, int)) and self.__a[j] > maxNum:
                    maxNum = self.__a[j]
            self.delete(maxNum)
        else: 
            return None
        return maxNum

    def removeDuplicate(self, arr):
        removeDupArr = Array(len(arr))
        while len(arr) > 0:
            x = arr.deleteMaxNum() 
            if x != None:
                if removeDupArr.find(x) == -1 and isinstance(x, (int, float)):
                    removeDupArr.insert(x)
        return removeDupArr