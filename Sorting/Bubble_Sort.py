def bubble_sort(arr):
    n = len(arr)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

A = [64, 25, 12, 22, 11]
print("Original Array : ",A)
bubble_sort(A)
print("Sorted Array : ", A)
