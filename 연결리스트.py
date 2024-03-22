class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

def getAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        return None
    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr

def traverse(self):
    answer = []
    curr = self.head
    while curr is not None:
        answer.append(curr.data)
        curr = curr.next
    return answer

def getLength(self):
    return self.nodeCount

def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False
    
    if pos == 1:
        newNode.next = self.head
        self.head = newNode
    else:
        if pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        newNode.next = prev.next
        prev.next = newNode
    if pos == self.nodeCount + 1:
        self.tail = newNode

    self.nodeCount += 1
    return True

def popAt(self, pos):
    if pos < 1 or self.nodeCount < pos:
        raise IndexError
    
    if pos == 1:
        res = self.head.data
        if self.nodeCount == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    else:
        prev = self.getAt(pos - 1)
        curr = prev.next
        res = curr.data
        if pos == self.nodeCount:
            prev.next = None
            self.tail = prev
        else:
            prev.next = curr.next
            
    self.nodeCount -= 1
    
    return res