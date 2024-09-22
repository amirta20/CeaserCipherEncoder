
def encrpyt(word,shift):
    encp1 = []
    wi = []
    for i in word:
        wi.append(i)
    for i in wi:
        if i in alpha:
            index=alpha.index(i)
            ind=int(index)
            enc=(ind+shift)%26
            encp1+=alpha[enc]
        else:
            encp1+=i
    for i in encp1:
        print(i,end="")
    print()

def decrypt(word,shift):
    encp = []
    w = []
    for i in word:
        w.append(i)
    for i in w:
        if i in alpha:
            index2=alpha.index(i)
            ind2=int(index2)
            d=ind2-shift
            if (d < 0):
                d+=26
            dec=(d)%26
            encp+=alpha[dec]
        else:
            encp+=i
    for i in encp:
        print(i,end="")
    print()




alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
end=False
while not end:
    action = input("Enter encrypt or decrypt : ")
    word = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if action=="encrypt":
            encrpyt(word,shift)
    elif action=="decrypt":
            decrypt(word,shift)
    else:
            print("Invalid action")
    cont=input("Do you want to continue ? ")
    if cont=="yes":
        continue
    else:
        end=True
        print("Over")







