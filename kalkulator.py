a=int(input("podaj liczbe a"))
b=int(input("podaj liczbe b"))
znak=input("podaj znak")



def licz():
    result=0
    if (znak=='+'):
        result=a+b
        return result
    elif(znak=="-"):
        result=a-b
        return result
    elif(znak=="*"):
        result=a*b
        return result
    elif(znak=='/'):
        if(b==0):
            print('error')
        else:
            result=a/b
            return result
    elif(znak=='^'):
        result=a
        for i in range(b-1):
            result*=a
        return result

res=licz()
print(res)
