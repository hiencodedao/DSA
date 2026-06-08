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

    def swap(self, j, k): 
        if (0 <= j <= self.__nItems) and (0 <= k <= self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

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

    def __str__(self): 
        ans = '['
        for i in range(self.__nItems):
            if len(ans) > 1: 
                ans += ', '
            ans += str(self.__a[i])
        ans += ']'
        return ans

    def bubbleSort(self):
        for outer in range(self.__nItems - 1, 0 , -1):
            for inner in range(outer):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)

    def twoWayBubbleSort(self):
        end_outer = self.__nItems
        begin_outer = 0
        while end_outer > begin_outer:
            for inner in range(begin_outer, end_outer - 1):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)
            end_outer -= 1
            for inner in range(end_outer - 1, begin_outer, -1): 
                if self.__a[inner] < self.__a[inner - 1]:
                    self.swap(inner, inner - 1)
            begin_outer += 1

    def selectionSort(self):
        for outer in range(self.__nItems - 1): 
            min = outer
            for inner in range(outer + 1, self.__nItems):
                if self.__a[inner] < self.__a[min]:
                    min = inner
            self.swap(min, outer) 

    def insertionSort(self):
        copy_number = 0
        comparison_number = 0
        for outer in range(1, self.__nItems):
            temp = self.__a[outer]
            inner = outer
            while inner > 0:
                comparison_number += 1
                if self.__a[inner - 1] > temp:
                    self.__a[inner] = self.__a[inner - 1]
                    inner -= 1
                    copy_number += 1
                else:   
                    break

            self.__a[inner] = temp
        
        print('Số lần so sánh:', comparison_number)
        print('Số lần đổi chỗ: ', copy_number)

    def median(self):
        median_index = (self.__nItems)/2
        if isinstance(median_index, float):
            median_index += (1/2 - 1) # Minus 1 to get the index of median
            median_index = int(median_index)
        print("The index of median is: ", median_index)
        print("\nThe value of median is: ", self.__a[median_index])
        for j in range(median_index):
            print(self.__a[j])
        for k in range(median_index + 1, self.__nItems - 1):
            print(self.__a[k])

        return self.__a[median_index]
    
    def deduplicate(self):
        dst = 0
        for src in range(1, self.__nItems - 1):
            if self.__a[src] != self.__a[dst]: 
                dst += 1
                self.__a[dst] = self.__a[src]
        
        self.__nItems = dst + 1

    def oddEvenSort(self): 
        passcount = 0
        swap = True

        while swap:
            passcount += 1
            swap = False
            for i in range(1, self.__nItems - 1, 2):
                if self.__a[i] > self.__a[i + 1]:
                    self.__a[i], self.__a[i + 1] = self.__a[i + 1], self.__a[i]
                    swap = True
            
            for j in range(0, self.__nItems - 1, 2):
                if self.__a[j] > self.__a[j + 1]: 
                    self.__a[j], self.__a[j + 1] = self.__a[j + 1], self.__a[j]
                    swap = True

        print("Số pass cần thiết: ", passcount)
                    
    def insertionSortDedup(self): 
        dup_count = 0

        # Sort the array and group the duplicates
        for outer in range(1, self.__nItems): 
            temp = self.__a[outer]
            inner = outer
            
            while inner > 0: 
                if self.__a[inner - 1] > temp :
                    self.__a[inner] = self.__a[inner - 1]
                    inner -= 1
                elif self.__a[inner - 1] == temp and temp != float('-inf'):
                    temp = float('-inf')
                    dup_count += 1
                    self.__a[inner] = self.__a[inner - 1]
                    inner -= 1
                else: 
                    break
            
            self.__a[inner] = temp

        # Remove duplicate and shift the array to the right position
        item_num = self.__nItems - dup_count
        for j in range(item_num):
            self.__a[j] = self.__a[j + dup_count]

        self.__nItems = item_num
        
        
        
            
    

    
                