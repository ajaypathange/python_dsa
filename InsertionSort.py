def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position - 1
        A[position] = cvalue


A = []
x = int(input("Enter the length of an array : "))
for arr in range(x):
    print("Enter the Element at index ",arr)
    l = int(input())
    A.append(l)
print('Original Array:',A)
insertionsort(A)
print('Sorted Array:',A)
