##liczba = str("1100")
##z=2
##do=16
##dec=0
##val="0123456789abcdefghijklmnoprstuwvxyz"
##for V in liczba:
##    dec=dec*z
##    v=0
##    print ('dec',dec)
##    while V!=val[v]:
##        v+=1
##    print(dec)
##    dec=dec+v
##    print(dec)
##liczba=str("")
##while dec>0:
##    v=int(dec)%do
##    #print(v)
##    liczba=str(val[v])+liczba   
##    dec=int(dec/do)
##print(liczba)

number=str("1100")
base=2
expect=10
dec=0
val="0123456789abcdefghijklmnoprstuwvxyz"

for i in number:
    dec=dec*base
    v=0
    while i!=val[v]:
        v+=1
    dec=dec+v
number=str("")

while dec>0:
    v=int(dec)%expect
    number=str(val[v])+number
    dec=int(dec/expect)
print(number)
