###zadanie 3 ŚLIMAK

###docelowo h=100
##h=0
###trasa dzień
##x=20
###upadek noc
##y=-10
###zostaje na noc co 20cm:
##z=30
##
##day_count=0
##
##while(h<100):
##    if h>0 and h%z==0:
##        day_trav=x
##        day_count+=1
##    else:
##        day_trav=x+y
##        day_count+=1
##    h+=day_trav
##    print(day_trav)
##    print(day_count)
##    
##print(day_count)
##
###zadanie 1

import random
random.seed()

n=10
arr=[]
for i in range(n):
    arr.append(random.randrange(10))
print(arr)

def mini(arr,a):
    min_=10
    for i in range(a,10,1):
        if min_>arr[i]:
            min_=arr[i]
            index=i
    return min_,index
#print(mini(arr))


for i in range(0,10,1):
    min_,ind_=mini(arr,i)
        #print(mini(arr,i))

    if(ind_!=i):
        tmp=min_
        arr[ind_]=arr[i]
        arr[i]=tmp
#return (arr)

print(arr)

#zadanie 3
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __del__(self):
        print('')

    def __str__(self):
        return "Data: {self.data}".format(self=self)

class Queue:
    def __init__(self):
        self.head=None

    def Push(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            n=self.head
            while(n.next!=None):
                n=n.next
            n.next=new

    def Pop(self):
        print(self.head)
        n=self.head
        self.head=n.next
        n.__del__()
        
    def Pop1(self):
        #print(self.head)
        n=self.head
        self.head=n.next
        #n.__del__()
        return n.data
            
    def Print(self):
        n=self.head
        while(n):
            print(n)
            n=n.next
        print('\n')
ll=Queue()
ll.Push("tutut")
ll.Push("lolol")
ll.Push("amama")
ll.Print()
print(ll.Pop1())
ll.Print()
