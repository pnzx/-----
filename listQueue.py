class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]
        
    def isEmpty(self) -> bool:
        return (len(self.__queue) == 0)