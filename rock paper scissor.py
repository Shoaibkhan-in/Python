from random import randrange

num=randrange(3)
print(num)

#as for now we consider 0 as rock 1 as paper 2 and scissors
'''
rock 0
paper 1
scissors 2
'''
'''
for 0==0 && 1==1 && 2==2 is draw
for 0&1 so paper wins, user
for 0&2 rock wins, computer
for 1&0 paper wins user 
for 1&2 sciossr wins computer
for 2&0 rock wins user
fro 2&1 scissor wins computer
'''

print("Enter Youre Choices \n 0:-ROCK\n 1:-PAPER\n 2:-SCISSOR\n")
a=int(input())
if((num==1 and a==1) or (num==2 and a==2) or (num==0 and a==0 )):
    print("BOTH HAVE MADE SAME DECISION ITS DRAW\n")

if(num==0 and a==1):
    print("COMPUTER CHOSE ROCK AND YOU CHOSE PAPER\n")
    print("YOU WON")

if(num==0 and a==2):
    print("COMPUTER CHOSE ROCK AND YOU CHOSE SCISSOR\n")
    print("YOU LOST")
if(num==1 and a==0):
    print("COMPUTER CHOSE PAPER AND YOU CHOSE ROCK\n")
    print("YOU LOST")
if(num==1 and a==2):
    print("COMPUTER CHOSE PAPER AND YOU CHOSE SCISSOR\n")
    print("YOU WON")

if(num==2 and a==0):
    print("COMPUTER CHOSE SCISSOR AND YOU CHOSE ROCK\n")
    print("YOU WON")
if(num==2 and a==1):
    print("COMPUTER CHOSE SCISSOR AND YOU CHOSE PAPER\n")
    print("YOU LOST")
