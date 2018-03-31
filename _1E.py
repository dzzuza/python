#grupa 5
#zadanie 1
import math
n=10000
##n_2=220
#sum_2=0
def divisors(n):
    divisors=[]
    for i in range(1,math.ceil(n/2)+1,1):
        if n%i==0:
            divisors.append(i)
    return divisors

def sum(n):
    div=divisors(n)
    sum_=0
    for i in div:
            sum_+=i
    return sum_


for i in range(1,n):
    suma_1=sum(i)
    suma_2=sum(suma_1)
    if suma_2==i:
        if i!=suma_1:
            print(i,suma_1)
        #return True
            
arr=divisors(n)
print(arr)
print(friend(n))

##class Node:
##    def __init__(self,number):
##        self.number=number
##        self.next=None
##        
##    def __str__(self):
##        return "{self.number}".format(self=self)
##
##class Stack:
##    def __init__(self):
##        self.top=None
##
##    def Push(self,number):
##        n=Node(number)
##        if(self.top==None):
##            self.top=n
##        else:
##            n.next=self.top
##            self.top=n
##
##    def Pop(self):
##        m=self.top
##        self.top=self.top.next
##        return m.number
####    def Print(self):
####        n=self.top
####        while(n):
####            print(n)
####            n=n.next
##code=str(input("Podaj działanie: "))
##
##ll=Stack()
##result=0
##i=0
##
##while(i<len(code)):
##    if code[i]==" ":
##        i+=1
##    elif code[i]=="+" or code[i]=="-" or code[i]=="*" or code[i]=="/":
##        a=int(ll.Pop())
##        b=int(ll.Pop())
##        if code[i]=="+":
##            result=a+b
##        if code[i]=="-":
##            result=a-b
##        if code[i]=="*":
##            result=a*b
##        if code[i]=="/":
##            result=b/a
##        ll.Push(result)
##        i+=1
##    else:
##        j=i
##        number=""
##        while code[j]!=None and code[j].isdigit():
##            number=number+code[j]
##            j=j+1
##        ll.Push(number)
##        i=j
##        i+=1
##print(ll.Pop())

years=[2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
months=["sty","lut","mar","kwi","maj","cze","lip","sie","wrz","paz","lis","gru"]
month1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
month2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
month3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
month4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
days=["pon","wto","sro","czw","pia","sob","nie"]

#year=2016
z=4

for year in years:
    if year%4!=0:
        for month in months:
            if (month=="sty" or month=="mar" or month=="maj" or month=="lip"
                or month=="sie" or month=="paz" or month=="gru"):
                for i in month1:
                    day=days[z]
                    if(z==6):
                        z=0
                    else:
                        z+=1
                    if(i==13 and day=="pia"):
                        print(str(year)+str(month))
            if (month=="kwi" or month=="cze" or month=="wrz" or month=="lis"):
                for i in month2:
                    day=days[z]
                    if(z==6):
                        z=0
                    else:
                        z+=1
                    if(i==13 and day=="pia"):
                        print(str(year)+str(month))
            if (month=="lut"):
                for i in month4:
                    day=days[z]
                    if(z==6):
                        z=0
                    else:
                        z+=1
                    if(i==13 and day=="pia"):
                        print(str(year)+str(month))
    if(year%4==0):
        for month in months:
            if (month=="sty" or month=="mar" or month=="maj" or month=="lip"
                or month=="sie" or month=="paz" or month=="gru"):
                for i in month1:
                    day=days[z]
                    if(z==6):
                        z=0
                    else:
                        z+=1
                    if(i==13 and day=="pia"):
                        print(str(year)+str(month))
            if (month=="kwi" or month=="cze" or month=="wrz" or month=="lis"):
                for i in month2:
                    day=days[z]
                    if(z==6):
                        z=0
                    else:
                        z+=1
                    if(i==13 and day=="pia"):
                        print(str(year)+str(month))
            if (month=="lut"):
                for i in month3:
                    day=days[z]
                    if(z==6):
                        z=0
                    else:
                        z+=1
                    if(i==13 and day=="pia"):
                        print(str(year)+str(month))
