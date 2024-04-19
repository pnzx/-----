from PriorityQueue import *

if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue( 34 )
    q.enqueue( 18 )
    q.enqueue( 27 )
    q.enqueue( 45 )
    q.enqueue( 15 )

    print("PQueue:", q)
    while not q.isEmpty() :
        print("Max Priority = ", q.dequeue() )