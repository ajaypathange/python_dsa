def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1,n):
            if A[j] < A[position]:
                position = j 
        temp = A[i]
        A[i] = A[position]
        A[position] = temp
        
A = []
arr = int(input("Enter the number of elements in the array : "))
for array in range(0,arr):
    print("Enter the Element of index : ",array)
    l = int(input())
    A.append(l)
print("The Original Array is : ", A)
selectionsort(A)
print("The Sorted Array is : ", A)