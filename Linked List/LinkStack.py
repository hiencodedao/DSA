from LinkedList import *

class LinkStack(object):
    def __init__(self):
        self.__stack = LinkedList()

    def push(self, item):
        self.__stack.insert(item)

    def pop(self):
        return self.__stack.deleteFirst()

    def peek(self):
        return self.__stack.first()

    def isEmpty(self):
        return self.__stack.isEmpty()

    def __len__(self):
        return len(self.__stack)

    def __str__(self):
        return str(self.__stack)

class Stack(LinkedList):
    push = LinkedList.insert
    pop = LinkedList.deleteFirst
    peek = LinkedList.getFirst