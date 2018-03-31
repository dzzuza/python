def podstaw(text,alpha):
    cipheredText=''
    key=1
    for letter in text:
        if letter in alphabet:
            x=alphabet[(alphabet.index(letter)+key)%(len(alphabet))]
            cipheredText+=x
        else:
            cipheredText+=letter
    return cipheredText


alphabet ="abcdefghijklmnopqrstuvwxyz"
text=input('enter you message: ')
print(podstaw(text,alphabet))

#print(deCezar(unText,3))
def dePodstaw(text,key):
    cipheredText=''
    for letter in text:
        if letter in alphabet:
            x=alphabet[((alphabet.index(letter)-key)+len(alphabet))%(len(alphabet))]
            cipheredText+=x
        else:
            cipheredText+=letter
    return cipheredText

print(dePodstaw(podstaw(text,alphabet),1))
