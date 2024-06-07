from 연결리스트 import *

class ListStack:
    def __init__(self) -> None:
        self.__stack = []
    
    def push(self, x):
        self.__stack.append(x)
    
    def pop(self):
        return self.__stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[-1]
    
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    
    def popAll(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack form top:", end=' ')
        for i in range(len(self.__stack)-1, -1, -1):
            print(self.__stack[i], end=' ')
        print()

class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
    
    def push(self, x):
        self.__list.insert(0, x)
    
    def pop(self):
        return self.__list.pop(0)
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.get(0)
        
    def isEmpty(self) -> bool:
        return self.__list.isEmpty()
    
    def popAll(self):
        self.__list.clear()