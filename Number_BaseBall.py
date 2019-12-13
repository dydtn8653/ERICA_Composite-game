import random
game=0
out=0
temp=[]
print('===== Number baseball  =====')
print('====== OSS PROJECT ======')
print()

myNum=random.sample(range(0,9),3)

# Check Function
def Check(y):

    y=guess

    if len(y)!=3:
        return 1
    elif y[0]==y[1] or y[1]==y[2] or y[2]==y[0]:
        return 2
    else:
        return 0

# Check Function
def StrikeBall(x):

    global strike; strike=0
    for j in range(3):
        if x[j]==myNum[j]:
            strike+=1

    global ball; ball=0
    for k in x:
        if k in myNum:
            ball+=1


# Main
while True:
    
    if game==9:
        print('> game over')
        print('The answer was {}{}{}'.format(myNum[0],myNum[1],myNum[2]))
        break
    elif out==3:
        print('> game over')
        print('The answer was {}{}{}'.format(myNum[0],myNum[1],myNum[2]))
        break
    else:
        while True:
            guess=input('> {} guess : '.format(game+1))

            if Check(guess)==1:
                print('Please enter a three-digit number.')
                print()
            elif Check(guess)==2:
                print('Please enter it so that it cannot be duplicated.')
                print()
            else:
                break

        for i in range(3):
            temp.append(int(guess[i]))

        StrikeBall(temp)
        temp=[]
        
        if strike==ball==0:
            print('{} out'.format(out+1))
            print()
            out+=1

        else:
            print('{} strike, {} ball'.format(strike,ball-strike))
            print()
            if strike==3:
                print('> You win')
                break
        game+=1
