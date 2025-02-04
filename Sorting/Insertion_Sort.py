def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position - 1
        A[position] = cvalue

A = [64, 25, 12, 22, 11]
print("Original Array : ",A)
insertion_sort(A)
print("Sorted Array : ", A)
