#setup code
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shift = input("What would you like the shift to be? (integer between 1 and 26): ")
msg = input("Please enter a message to be ciphered: ")
newmessagelist = []

#ciphers the message
def msgCreater(msg):
    for i in msg:
        if (int(shift) % 26 == 0):
            newmessagelist.append(i)
            continue
        if (i == " "):
            index = index + 1
            newmessagelist.append(" ")
            continue
        index = alphabet.index(i)
        newindex = index + int(shift)
        if (newindex >= 25):
            newindex = (newindex % 25) - 1
            newletter = alphabet[newindex]
            newmessagelist.append(newletter)
        else:
            newletter = alphabet[newindex]
            newmessagelist.append(newletter)


#list to string
def listToString(newmessagelist):
    str = ""
    for i in newmessagelist:
        str = str + i
    return str

#function code
print("Old message is:", msg)
msgCreater(msg)
print("Ciphered message is:", listToString(newmessagelist))
