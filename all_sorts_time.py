import random
random.seed()
array=[]

for i in range(0,50):
        array.append(random.randrange(50))
#------------------------------------------------
def bubbel(tablica):
    for i in range(len(tablica)):
        for j in range (len(tablica)-1):
            if (tablica[j]>tablica[j+1]):
                tmp=tablica[j]
                tablica[j]=tablica[j+1]
                tablica[j+1]=tmp
    return tablica
#------------------------------------------------
def insert(lista):
    for i in range (1,len(lista)):
        index =i
        value = lista[i]
        while index>0 and lista[index-1]>value:
            lista[index],lista[index-1]=lista[index-1],lista[index]
            index=index-1
#------------------------------------------------
def minimum(tab,a):
    m=50
    start=a
    for j in range (start,len(tab),1):
        if (m>tab[j]):
            m=tab[j]
            mind=j
    return(m,mind)

def select(tablica):
    n=len(tablica)
    for i in range(0,n-1,1):
        m, x=minimum(tablica,i)
        if x!=i:
            temp=[]
            temp=tablica[i:x]
            tablica[i]=m
            tablica[i+1:x+1]=temp
#------------------------------------------------
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
#------------------------------------------------
def heapify(lista,start,end):
    parent=start
    while True:
        child=parent*2+1
        if child>end:
                break
        if child+1<=end and lista[child]<lista[child+1]:
                child=child+1
        if(lista[parent]<lista[child]):
                lista[parent],lista[child]=lista[child],lista[parent]
                parent=child
        else:
                break

def heapSort(lista):
  for i in range((len(lista)//2),-1,-1):
    heapify(lista,i,len(lista)-1) 
  for j in range (len(lista)-1,-1,-1):
    lista[j],lista[0]=lista[0],lista[j]
    heapify(lista,0,j-1)
  return lista
#------------------------------------------------
def quicksort(lista,start,end):
    pivot=lista[(start+end)//2]
    left=start
    right=end
    while(left<=right):
        while(lista[left]<pivot):
            left+=1
        while(lista[right]>pivot):
            right-=1
        if(left<=right):
            lista[left],lista[right]=lista[right],lista[left]
            left+=1
            right-=1
    if(start<right):
        quicksort(lista,start,right)
    if(end>left):
        quicksort(lista,left,end)

#------------------------------------------------
print('LISTA NIEPOSORTOWANA')
print(array)
array1=list(array)
array2=list(array)
array3=list(array)
array4=list(array)
array5=list(array)

bubbel(array)
print('LISTA PO SORTOWANIU BĄBELKOWYM')
print(array)
#---------------------
insert(array1)
print('LISTA PO SORTOWANIU PRZEZ WSTAWIANIE')
print(array1)
#---------------------
select(array2)
print('LISTA PO SORTOWANIU PRZEZ WYBIERANIE')
print(array2)
#---------------------
mergeSort(array3)
print('LISTA PO SORTOWANIU PRZEZ SCALANIE')
print(array3)
#--------------------
heapSort(array4)
print('LISTA PO SORTOWANIU PRZEZ KOPCOWANIE')
print(array4)
#--------------------
quicksort(array5,0,len(array)-1)
print('LISTA PO SORTOWANIU QUICKSORT')
print(array5)
