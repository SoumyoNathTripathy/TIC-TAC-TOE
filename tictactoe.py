'''
------------------------------------------------------------
This is a TicTacToe game in python.
This code consists of 3 parts:
1. wingame(l1,l2,l3) checks if someone has won
2. check(l1,l2,l3) checks if all positions are filled.
3. place(l1,l2,l3,pos,val) places user input on the grid.
4. printlist(l1,l2,l3) prints the grid.
5. main() function integrates all the other functions.
-------------------------------------------------------------
'''
def wingame(l1,l2,l3):
    if (l1[0]==l1[1] and l1[1]==l1[2]): # and l1[0]=='O'):
        return l1[0]
    elif (l2[0]==l2[1] and l2[1]==l2[2]): # and l2[0]=='O'):
        return l2[0]
    elif (l3[0]==l3[1] and l3[1]==l3[2]):# and l3[0]=='O'):
        return l3[0]

    
    elif (l1[0]==l2[0] and l2[0]==l3[0]): # and l1[0]=='O'):
        return l1[0]
    elif (l1[1]==l2[1] and l2[1]==l3[1]): # and l1[1]=='O'):
        return l1[1]
    elif (l1[2]==l2[2] and l2[2]==l3[2]): # and l1[2]=='O'):
        return l1[2]

    
    elif (l1[0]==l2[1] and l2[1]==l3[2]): # and l1[0]=='O'):
        return l1[0]
    elif (l1[2]==l2[1] and l2[1]==l3[0]): # and l1[2]=='O'):
        return l1[2]
    else:
        return 'draw'
def check(l1,l2,l3):
    if ' ' in l1 or ' ' in l2 or ' ' in l3:
        return False
    return True

def place(l1,l2,l3,pos,val):
    if int(pos[0])==1:
        l1[int(pos[1])-1]= val
    elif int(pos[0])==2:
        l2[int(pos[1])-1]= val    
    elif int(pos[0])==3:
        l3[int(pos[1])-1]= val
    return l1,l2,l3

def printlist(l1,l2,l3):
    print(l1)
    print(l2)
    print(l3)

def main():
    print("Player 1")
    print("Enter Your name")
    p1 = input()
    print("Press 1 for O and 2 for X")
    i1 ='O' if int(input()) == 1 else 'X'
    print("Player 2")
    print("Enter Your name")
    p2 = input()
    i2 = 'X' if i1 == 'O' else 'O'
    turn = 0
    l1=[' ',' ',' ']
    l2=[' ',' ',' ']
    l3=[' ',' ',' ']
    s=0
    while(check(l1,l2,l3)==False):
        print("Turn = {}".format(turn+1))
        print("Player 1 choose position as 2 spaced integers")
        pos1 = (input().split())
        l1,l2,l3 = place(l1,l2,l3,pos1,i1)
        print("Current state")
        printlist(l1,l2,l3)
        r = wingame(l1,l2,l3)
        if r!=' ':
            if r=='draw' and turn<5:
                    s=1
            else:
                    print("Win for {}".format(r))
                    s=0
                    break
        print("Player 2 choose position as 2 spaced integers")
        pos1 = (input().split())
        l1,l2,l3 = place(l1,l2,l3,pos1,i2)
        print("Current state")
        printlist(l1,l2,l3)

        
        r = wingame(l1,l2,l3)
        print(r)
        if r!=' ':
            if r=='draw' and turn<5:
                    s=1
                    continue
            else:
                    print("Win for {}".format(r))
                    s=0
                    break
        turn+=1

    if(s==1) or check(l1,l2,l3) and wingame(l1,l2,l3)=='draw':
        print("DRAW")
            
