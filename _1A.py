##import math
##
###ZADANIE 3
##divisors=[]
##n=28
##def div(n):
##    for i in range(1,n,1):
##        if(n%i==0):
##            divisors.append(i)
##    return divisors
##
##def sum_div(n):
##    arr=(div(n))
##    print(arr)
##    divsum=0
##    for i in range(0,len(arr)):
##       divsum=divsum + arr[i]
##    #print (divsum)
##    return divsum
##
##def perfect(n):
##    sum_=sum_div(n)
##    if(sum_==n):
##        print("liczba jest doskonala")
##    else:
##        print("nie jest")
##    return(sum_)
##
##print(perfect(n))

#ZADANIE 1
import random
random.seed()
arr=[]
for i in range(100):
    arr.append(random.randrange(100))
print(arr)

def babel(arr):
    for j in range(len(arr)-1):
        for i in range(0,len(arr)-1,1):
            if arr[i]>arr[i+1]:
                tmp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=tmp
    return arr
print (babel(arr))

#ZADANIE 2
class Node:
    def __init__(self, day, month):
        self.day=day
        self.month=month
        self.prev=None
        self.next=None
        

    def __del__(self):
        print("")

    def __str__(self):
        return 'day : {self.day}, month: {self.month}'.format(self=self)

class Organizer:
    def __init__(self):
        self.head=None
        self.size=0

    def BackAdd(self,day,month):
        n=self.head
        new=Node(day,month)
        if self.head==None:
            self.head=new
            self.size+=1
        else:
            while(n.next!=None):
                n=n.next
            n.next=new
            new.prev=n
            self.size+=1

    def BackRem(self):
        n=self.head
        while(n.next!=None):
            n=n.next
        m=n.prev
        m.next=None
        #n.__del__()
        self.size-=1

    def Print(self):
        top=self.head
        print("oto lista: ")
        while(top):
            print(top)
            top=top.next


            

oo=Organizer()
oo.BackAdd("20","05")
oo.BackAdd("21","07")
oo.BackAdd("21","02")

oo.BackRem()
##babel(oo)
oo.Print()
##m=int(oo.head)
##x=int(m.next.month)
##for i in range(oo.size):
##    if(m<x):
##        print("p")
#print(oo.size)

            
    




        
