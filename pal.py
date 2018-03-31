import math
#ZADANIE 1
word=input("Podaj słowo: ")
#print(word)
#print(len(word))
flag=0
#Napotkała typa.Zapytała: Kto Pan?
i=0
j=len(word)-1

while i<math.ceil(len(word)/2) and flag==0:
    #print(math.ceil(len(word)/2))
    if (not word[i].isalpha()):
        #print('i')
        i+=1
    elif not word[j].isalpha():
        #print('j')
        j-=1
    elif word[i]==word[j]:
        i+=1
        j-=1
        flag=0
        #print('=')
    else:
        #print('!')
        flag=1
        
print(flag)

if (flag==0):
    print("jest palindromem")
else:
    print("nie jest")
