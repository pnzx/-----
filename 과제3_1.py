class Node:
  def __init__(self, item, next=None, prev=None):
    self.item = item
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, i:int, x:int):
    """insert x in ith element"""

  def delete(self, i):
    """delete ith element"""

  def printList(self):
    curr = self.head
    while curr:
      print(curr.x, "->")
      curr = curr.next
      if(curr=None):
        print("end")