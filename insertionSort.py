def insertionSort(A):
    for i in range(1, len(A)):
        loc = i-1
        newitem = A[i]
        while loc >= 0 and newitem < A[loc]:
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = newitem

def insertionSortRec(A, start, end):
    value = A[start]
    loc = start
    while loc > 0 and A[loc-1] > value:
        A[loc] = A[loc-1]
        loc -= 1
    A[loc] = value
    if start + 1 < end:
        insertionSortRec(A, start+1, end)