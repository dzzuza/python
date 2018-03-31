#ZADANIE 1

##osemkowa=input("podaj: ")
##wynik=int(osemkowa[0])
###print(wynik)
##
##for i in range(0,len(osemkowa)-1):
##    if (osemkowa[i].isdigit() and int(osemkowa[i])>=0 and int(osemkowa[i])<=7):
##        wynik*=8
##        #print(wynik)
##        wynik+=int(osemkowa[i+1])
##        print(wynik)
##    else:
##        print("Podana liczba nie jest w systemie osemkowym")


#ZADANIE 2
import random
import time
random.seed()

height=7
width=11
arr=[]

for k in range(0,7):
    drop=random.randint(0,width-1)
    arr.insert(0,drop)
    print(arr)
    for i in range(0,height):
        wiersz=' '
        for j in range(0,width):
            if(i<=k and j==arr[i]):
                wiersz+="x"
            else:
                wiersz+="0"
        print(wiersz)
    time.sleep(0.3)
    print("\n")

#ZADANIE 3
##class Node:
##    def __init__(self, name, score):
##        self.name=name
##        self.score=score
##        self.next=None
##
##    def __del__(self):
##        print(" ")        
##
##    def __str__(self):
##        return "Name: {self.name}, Score: {self.score}".format(self=self)
##
##class StudentList:
##    def __init__(self):
##        self.top=None
##        self.size=0
##
##    def FrontAdd(self,name,score):
##        n=Node(name,score)
##        if self.top==None:
##            self.top=n
##            self.size+=1
##        else:
##            n.next=self.top
##            self.top=n
##            self.size+=1
##
##    def PrintList(self):
##        n=self.top
##        while n:
##            print(n)
##            n=n.next
##        print("\n")
##
##    def Pop(self):
##        if self.top!=None:
##            n=self.top
##            print(n)
##            self.top.__del__()
##            self.top=n.next
##            self.size-=1
##            
##    def FindMax(self):
##        m=self.top
##        x=self.top.next
##        aa=StudentList()
##        for i in range(0,self.size-1):
##            if(m.score < x.score):
##                m=x
##                for i in range(0,self.size-1):
##                    aa.Pop()
##                aa.FrontAdd(x.name,x.score)
##                print("<")
##                aa.PrintList()
##            elif(m.score==x.score):
##                aa.FrontAdd(x.name,x.score)
##                aa.PrintList()
##                print("=")
##            x=x.next
##        if(self.top.score==m.score):
##            aa.FrontAdd(self.top.name, self.top.score)
##            
##            
##        print("Max score: ")
##        aa.PrintList()
##
##
##ll=StudentList()
##ll.FrontAdd("Ala", 7)
##ll.FrontAdd("Adam", 6)
##ll.FrontAdd("Ada", 3)
##ll.FrontAdd("Roma", 7)
##ll.FrontAdd("Bolek", 7)
##ll.PrintList()
##ll.FindMax()
##ll.Pop()
##ll.PrintList()








