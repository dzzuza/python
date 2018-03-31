#grupa4

#zadanie 1

##import math
##
##number=str("321")
##
##result=""
##penta=""
##while(int(number)>0):
##    for i in number:
##        #if i.isdigit() and int(i)>=0 and int(i)<5:
##            x=int(number)%5
##            penta=str(x)+penta
##            number=math.floor(int(number)/5)
##        else:
##            print("SYSTEM OBCY")
####for i in range(-1,-len(result)-1,-1):
####    penta+=result[i]
##print(penta)

#zadanie 2
##
##class Node:
##    def __init__(self, number):
##        self.number=number
##        self.next=None
##
##    def __str__(self):
##        return "{self.number}".format(self=self)
##
##class Stack:
##    def __init__(self):
##        self.top=None
##        self.size=0
##
##    def Push(self,number):
##        n=Node(number)
##        if(self.top==None):
##            self.top=n
##        else:
##            m=self.top
##            self.top=n
##            n.next=m
##
##    def Pop(self):
##        m=self.top
##        self.top=self.top.next
##        return m.number
##
##code=str(input("Podaj działanie: "))
##
##L=Stack()
##result=0
##
##i=0






##while (i<len(code)):
##    if code[i]==" ":
##        i+=1
##    elif code[i]=="+" or code[i]=="-" or code[i]=="*" or code[i]=="/":
##        a=int(L.Pop())
##        b=int(L.Pop())
##        if code[i]=="+":
##            result=b+a
##        elif code[i]=="-":
##            result=b-a
##        elif code[i]=="*":
##            result=b*a
##        elif code[i]=="/":
##            result=b/a
##        L.Push(result)
##        i+=1
##    else:
##        j=i
##        number=""
##        while code[j]!=None and code[j].isdigit():
##            number=number+code[j]
##            j=j+1
##        L.Push(number)
##        i=j
##        i+=1
##print(L.Pop())

    
#ZADANIE 3
days = ["poniedzialek","wtorek","sroda","czwartek","piatek","sobota","niedziela"]
months = ["sty","lut","marz","kwi","maj","czerw","lip","sierp","wrze","paz","lis","gru"]
month1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
month2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
month3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
month4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
years = [2018,2019,2020,2021,2022,2023,2024,2025]

print("Piatki trzynastego w latach 2016-2025")
#month = "sty"
z = 0
day = days[z]
#year = 2017
print(day)
 
for year in years:
    if(year%4!=0):
        #print(year)
        for month in months:
            if (month=="sty" or month=="marz" or month=="maj" or month=="lip" or month=="sierp" or month =="paz" or month=="gru"):
                #print('m',month)
                for i in month1:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    if (i==13 and day == "piatek"):
                        print(days[z],day)
                        print(str(year)+str(month))
                
            if (month=="kwi" or month=="czerw" or month=="wrze" or month=="lis"):
                #print('m',month)
                for i in month2:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    if (i==13 and day == "piatek"):
                        print(str(year)+str(month))
            if (month=="lut"):
                #print('m',month)
                for k in month3:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z +=1
                    if (k==13 and day == "piatek"):
                        print(str(year) + str(month))
    #print(day)
    if(year%4==0):
        #print(year)
        for month in months:
            if (month=="sty" or month=="marz" or month=="maj" or month=="lip" or month=="sierp" or month =="paz" or month=="gru"):
                #print('m',month)
                for i in month1:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    
                    if (i==13 and day == "piatek"):
                        print(str(year)+str(month))
                
            if (month=="kwi" or month=="czerw" or month=="wrze" or month=="lis"):
                #print('m',month)
                for i in month2:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    #print(day)
                    if (i==13 and day == "piatek"):
                        print(str(year)+str(month))
            if (month=="lut"):
                #print('m',month)
                for k in month4:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z +=1
                    if (k==13 and day == "piatek"):
                        print(str(year) + str(month))













        





        
        
