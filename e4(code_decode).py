import random
import string

print("WELCOME to the page of CODING AND DECODING")

messages = input("Enter the message to be coded or decoded : ").split( )

a=input("Enter 1 for coding and 0 for decoding : ")

c=[]

while (a!="1" and a!="0"):
    a=input("\n INVALID INPUT!!!\nPlease enter 1 for coding and 0 for decoding correctly : ")

if(a=="1"):
    for message in messages:
        if len(message)>=3:
            c.append("".join(random.choices(string.ascii_letters,k=3))+message[1:]+message[0]+"".join(random.choices(string.ascii_letters,k=3)))
        else:
            c.append(message[::-1])
else:
    for message in messages:
        if len(message)>=3:
            c.append(message[-4]+message[3:-4])
        else:
            c.append(message[::-1])

print(" ".join(c))