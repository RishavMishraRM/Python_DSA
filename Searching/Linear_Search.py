def linearsearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key :
            return index
        index = index + 1
    return "Not Found"

A = [84, 21, 47, 96, 15]
found = linearsearch(A,960)
print('Result:',found)
