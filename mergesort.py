import random
random.seed()
array=[]

for i in range(0,100):
        array.append(random.randrange(100))
def merge(left, right, arr):
    i=0;
    j=0;
    k=0;
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k]= left[i]
            i=i + 1
            k=k + 1
        else:
            arr[k]=right[j]
            j=j + 1
            k=k + 1
    while i < len(left):
        arr[k]=left[i]
        i=i + 1
        k=k + 1
    while j < len(right):
        arr[k]=right[j]
        j=j + 1
        k=k + 1
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid=len(arr) // 2
    left = arr[:mid]
    right = arr[mid :]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)
print(array)
mergeSort(array)
print(array)
