def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if A[j] < A[position]:
                position = j
        A[i], A[position] = A[position], A[i]

A = [64, 25, 12, 22, 11]
print("Original Array : ",A)
selection_sort(A)
print("Sorted Array : ", A)
