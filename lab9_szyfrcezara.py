alphabet ="abcdefghijklmnopqrstuvwxyz"

def cezar(text,key):
    cipheredText=''
    for letter in text:
        if letter in alphabet:
            x=alphabet[(alphabet.index(letter)+key)%(len(alphabet))]
            cipheredText+=x
        else:
            cipheredText+=letter
    return cipheredText

def deCezar(unText,key):
    uncipheredText=''
    for letter in unText:
        if letter in alphabet:
            x=alphabet[((alphabet.index(letter)-key)+len(alphabet))%(len(alphabet))]
            uncipheredText+=x
        else:
            uncipheredText+=letter
    return uncipheredText

text=input('enter you message: ')

print(cezar(text,5))

unText=(cezar(text,11))

print(deCezar(unText,11))
