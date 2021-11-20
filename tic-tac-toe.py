'''
Documentation, License etc.

Tic-Tac-Toe by Alessandro Hamuche
v1.0-Beta
Created: 11/20/2021
Modified: not modified

@package tictac
'''
# 111000000 <- -..
# 000111000 <- *-.
# 000000111 <- **_
# 100010001 <- \
# 010010010 <- .|.
# 001010100 <- /
# 100100100 <- |..
# 001001001 <- ..|

game=True
count=0
list_converted=[0, 0, 0, 0, 0, 0, 0, 0, 0]
player="x"

list7=[1, 1, 1, 0, 0, 0, 0, 0, 0]
list56=[0, 0, 0, 1, 1, 1, 0, 0, 0]
list73=[1, 0, 0, 1, 0, 0, 1, 0, 0]
list84=[0, 0, 1, 0, 1, 0, 1, 0, 0]
list146=[0, 1, 0, 0, 1, 0, 0, 1, 0]
list263=[1, 0, 0, 0, 1, 0, 0, 0, 1]
list292=[0, 0, 1, 0, 0, 1, 0, 0, 1]
list448=[0, 0, 0, 0, 0, 0, 1, 1, 1]

list_check=[list7, list56, list73, list84, list146, list263, list292, list448]

def list_convert(alist):
    blist=[]
    for x in range(len(alist)):
        if player==alist[x]:
            blist.append(1)
        else:
            blist.append(0)
    return blist

tictac=["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(str(tictac[0:3]) + "\n" + str(tictac[3:6]) + "\n" + str(tictac[6:9]))

while game:

    x_in=input("pos " + player + ": ")

    count+=1

    check=True
    while check:

        if x_in=="q":
            check=False
            game=False
            break

        for x in range(len(tictac)):
            if (x_in==tictac[x]):
                tictac[x]=player
                check=False
                print(str(tictac[0:3]) + "\n" + str(tictac[3:6]) + "\n" + str(tictac[6:9]))

        if check:
            x_in=input("Retry, pos " + player + ": ")

    if count>4:
        list_converted=list_convert(tictac)
        for x in range(len(list_check)):
            match=0

            for y in range(len(list_check[x])):
                if list_check[x][y]==list_converted[y]:
                    if list_converted[y]>0:
                        match+=1

            if match==3:
                print("Player " + player + " has won!")
                game=False
                break

    if count==9:
        print("Game tie")
        game=False

    if player=="x":
        player="o"
    else:
        player="x"
