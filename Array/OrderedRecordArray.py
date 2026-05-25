def identity(x):
    return x

class OrderedRecordArray(object): 
    def __init__(self, initialize, key=identity):
        self.__a = [None] * initialize
        self.__nItems = 0
        self.__key = key
    
    def __len__(self):
        return self.__nItems

    def get(self, n):    # return value at index n
        if self.__nItems > n and n >= 0:
            return self.__a[n] 
        raise IndexError("Index " + str(n) + " is out of range")
    
    def traverse(self, function=print):     # Traverse all items
        for j in range (self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for j in range(self.__nItems):
            if len(ans) > 1: 
                ans += ", "
            ans += str(self.__a[j])
        ans += "]"
        return ans

    def find(self, key): # Find index at or just below the key
        lo = 0
        hi = self.__nItems - 1

        while lo <= hi:
            mid = (lo + hi)//2 
            if self.__key(self.__a[mid]) == key: 
                return mid
            elif self.__key(self.__a[mid]) < key:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    def insert(self, item):     # Insert a item into the correct position
        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")

        j = self.find(self.__key(item))

        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k-1]
            
        self.__a[j] = item
        self.__nItems += 1

    def delete(self, item):     # Delete any occurrence
        j = self.find(self.__key(item))
        if self.__a[j] == item and j < self.__nItems:
            self.__nItems -= 1
            for k in range(j, self.__nItems):
                self.__a[k] = self.__a[k+1]
            return True
        return False

    def merge(self, arr, key_fn):
        mergeArr = OrderedRecordArray(self.__nItems + arr.__nItems, key=key_fn)
        
        if self.__key is arr.__key:
            i = 0
            j = 0

            while i < self.__nItems and j < arr.__nItems:
                if self.__key(self.__a[i]) <= arr.__key(arr.__a[j]):
                    mergeArr.insert(self.__a[i])
                    i += 1
                else:
                    mergeArr.insert(arr.__a[j])
                    j += 1

            while i < self.__nItems:
                mergeArr.insert(self.__a[i])
                i += 1

            while j < arr.__nItems:
                mergeArr.insert(arr.__a[j])
                j += 1

            return mergeArr
        else: 
            return None

    