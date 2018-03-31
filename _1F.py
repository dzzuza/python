#zadanie 1
class Node:
    def __init__(self,number):
        self.number=number
        self.next=None

    def __str__(self):
        return str("{self.number}").format(self=self)

class Stack:
    def __init__(self):
        self.top=None

    def Push(self,number):
        n=Node(number)
        if self.top==None:
            self.top=n
        else:
            n.next=self.top
            self.top=n

    def Pop (self):
        n=self.top
        self.top=self.top.next
        #print(n)
        return n.number

L=Stack()
data=input(str("Podaj dzialanie: "))
result=0
i=0
while(i<len(data)):
    if data[i]==" ":
        i+=1
    elif data[i]=="+" or data[i]=="-" or data[i]=="*" or data[i]=="/":
        a=int(L.Pop())
        b=int(L.Pop())
        if data[i]=="+":
            result=a+b
        #    L.Push(result)
        elif data[i]=="-":
            result=a-b
        #    L.Push(result)
        elif data[i]=="*":
            result=a*b
        #    L.Push(result)
        elif data[i]=="/":
            result=b/a
        L.Push(result)
        i+=1
    else:
        j=i
        number=""
        while data[j]!=None and data[j].isdigit():
            number=number + data[j]
            j+=1
        L.Push(number)
        i=j
        i+=1
print(L.Pop())
###zadaniw 2
##import random
##random.seed()
##arr=[]
##for i in range(50):
##    arr.append(random.randrange(50))
##print(arr)
##
##def bub(tab):
##    for i in range(50):
##        for j in range(len(arr)-1):
##            if tab[j]>tab[j+1]:
##                tmp=tab[j]
##                tab[j]=tab[j+1]
##                tab[j+1]=tmp
##bub(arr)
##print(arr)

###zadanie 3
##def fibo(n):
##    fib=0
##    for i in range(0,n+1,1):
##        if i==0:
##            fib=1
##        elif i==1:
##            fib=1
##        elif i==2:
##            fib=2
##        else:
##            fib=fibo(i-1)+fibo(i-2)+fibo(i-3)
##    #print(fib)
##    return fib
##print(fibo(4))
##print(fibo(5))
##
##print('\n')
##def it(n):
##    fib=0
##    b=0
##    c=0
##    for i in range(n+1):
##        if i==0:
##            a=1
##            fib=a
##        elif i==1:
##            b=1
##            fib=b
##        elif i==2:
##            c=2
##            fib=c
##        else:            
##            fib=a+b+c
##            a=b
##            b=c
##            c=fib
##        print(fib)
##    return fib
##
##print(it(5))
