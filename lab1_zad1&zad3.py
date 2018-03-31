#wys=int(input("wysokosc"))
#szer=int(input("szerokosc"))

#if((szer>0) and (wys>0)):
#  print("pole trojkata:")
#  print((wys*szer)/2)
  
  
import random
random.seed()
losowana = random.randrange(10) 
#print(losowana)
flag=0
while(flag==0):
  liczba=int(input("Podaj liczbe"))
  if(liczba==losowana):
    print("tak")
    flag=1
  elif(liczba < losowana):
    print("za mala")
  elif(liczba > losowana):
    print("za duza")
