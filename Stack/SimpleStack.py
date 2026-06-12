class stack(object):
    def __init__(self, max):
        self.__stackList = [None] * max
        self.__top = -1

    def push(self, item):
        if self.isFull(): 
            raise Exception("Stack overflow")
        self.__top += 1
        self.__stackList[self.__top] = item

    def pop(self):
        if self.isEmpty(): 
            raise Exception("Stack is empty")
        top = self.__stackList[self.__top]
        self.__stackList[self.__top] = None
        self.__top -= 1

        return top

    def peek(self):
        if not self.isEmpty():
            top = self.__stackList[self.__top]
        return top

    def isEmpty(self):
        return self.__top < 0

    def isFull(self):
        return self.__top >= len(self.__stackList) - 1 

    def __len__(self):
        return self.__top + 1

    def __str__(self):
        ans = "["
        for i in range(self.__top + 1):
            if len(ans) > 1: 
                ans += ", "
            ans += self.__stackList[i] 
        ans += "]"
        return ans