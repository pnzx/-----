def selectionSort(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

def theLargest(A, last:int) -> int:
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = i
        return largest
    

def selectionSortRec(A, n):
    if(n>2):
        k = theLargest4Rec(A, n-1)
        A[k], A[n-1] = A[n-1], A[k]
        selectionSortRec(A, n-1)

def theLargest4Rec(A, last:int) -> int:
    largest = 0
    for i in range(last):
        if A[i] > A[largest+1]:
            largest = i
    return largest