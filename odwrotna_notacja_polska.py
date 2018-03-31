class Node:
    
    def __init__(self, liczba):
        self.liczba=liczba
        self.prev=None

    def __str__(self):
        return str(self.liczba)
        
class Lista:
    
    def __init__(self):
        self.top=None
        
    def dodaj(self, wartosc):
        n=Node(wartosc)
        n.prev=self.top
        self.top=n
        
    def pop(self):
        if (self.top!=None):
            zwracane=self.top
            self.top=self.top.prev
            return zwracane

dzialanie=input("Podaj działanie: ")
blad=False
       
ll=Lista()

while (dzialanie!=''):
    indeks=dzialanie.find(' ')
#    print(indeks)
    if (indeks>=0):
        człon=dzialanie[:dzialanie.find(' ')]
        dzialanie=dzialanie[dzialanie.find(' ')+1:]
    else:
        człon=dzialanie
        dzialanie=''
    print(człon)
    if (człon.isdigit()==True):
        ll.dodaj(int(człon))
    elif (człon=='+'):
        print('+')
        wartosc=ll.pop().liczba+ll.pop().liczba
        ll.dodaj(wartosc)

    else:
        blad=True
    
if (blad==False):
    print(ll.pop())
else:
    print ("Błędne działanie!")
