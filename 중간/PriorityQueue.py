class PriorityQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1
    
    def findMaxindex(self):
        if self.isEmpty():
            return -1
        highest = 0
        for i in range(1, self.size):
            if self.array[i] > self.array[highest]:
                highest = i
        return highest
    
    def dequeue(self):
        highest = self.findMaxindex()
        if highest != -1:
            self.size -= 1
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]
        return self.array[self.size]
    
    def peek(self):
        highest = self.findMaxindex()
        if highest != -1:
            return self.array[highest]
        
    def __str__(self) -> str:
        return str(self.array[0:self.size])
    
    '''def main():
        q = PriorityQueue()
        q.enqueue( 34 )
        q.enqueue( 18 )
        q.enqueue( 27 )
        q.enqueue( 45 )
        q.enqueue( 15 )

        print("PQueue:", q)
        while not q.isEmpty() :
            print("Max Priority = ", q.dequeue() )

    if __name__ == "__main__":
        main()'''