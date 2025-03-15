import random
print(".-.-.-.WELCOME TO SNAKE wATER AND GUN GAME.-.-.-.")
def check(comp,man):
    if man!=0 and man!=1 and man!=2:
        return 10
    else:
        if comp==man:
            return 0
        elif comp==0 and man==1:
            return -1
        elif comp==1 and man==2:
            return -1
        elif comp==2 and man==0:
            return -1
        else:
            return 1
while True:
    comp=random.randint(0,2)
    man=(input("Enter your choice\n0 for SNAKE\n1 for WATER\n2 for GUN\n anything else to EXIT\n : "))
    try:
        type(eval(man)) ==type(1)
        iman=int(man)
        result=check(comp,iman)
    except:
        result=check(comp,man)
    
    if result==0:
        print(f"Your choice : {man}\nComputer choice : {comp}")
        print("ITS A DRAW")
    elif result==1:
        print(f"Your choice : {man}\nComputer choice : {comp}")
        print("YOU WON")
    elif result==-1:
        print(f"Your choice : {man}\nComputer choice : {comp}")
        print("YOU LOST")
    else:
        print("THANK YOU FOR PLAYING")
        break
    