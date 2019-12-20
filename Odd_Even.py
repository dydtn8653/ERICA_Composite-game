import random
import time
def game():
    """
    GameStart
    """
    ans = ""
    money0 = 10000
    money1 = money0 + 1
    print("Start Odd/Even game!\nNow you have 10000$.\nGuess if the sum of the two dice is odd or even.")
    while ans != "Stop":
        dicesum = dice()
        betmoney = money_betting(money0)
        num = number_choice()
        dicerst = dicesum%2
        print("Rolling dice....")
        time.sleep(3)
        if num == dicerst:
            money1 = money0 + betmoney
        else:
            money1 = money0 - betmoney
        print("The sum of the dice", dicesum,"!!")
        print("(Before batting)", money0,"===>",money1,"(After batting)")
        
        if money1 > 0:
          ans = input("Please enter 'Stop' to stop playing.\nPress any button to start the game again.")
          money0 = money1
        else:
          print("You have lost all your money. You lost..")
          break
        if ans == "STOP":
        	print("Exit the game.")
        
def dice():
    """
    add function
    """
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    return dice_sum


def money_betting(money):
    """
    User bet money
    """
    if money>=0:        
        while True:
            bet_money = int(input("Please enter the amount you want to bet on: "))
            if bet_money <= money and bet_money > 0:
                break
            elif bet_money <= 0:
                print("Please enter the betting amount correctly.")
            else:
                print("The betting amount cannot exceed the current budget.")
    else:
        print("You don't have enough money to go ahead with the game.")    
    return bet_money

def number_choice():
    """
    user choice odd/even function
    """
    while True:
        bet_num = input("Please enter Odd/Even .")
        if bet_num == "Odd":
            bet_num = 1
            break
        elif bet_num == "Even":
            bet_num = 0
            break
        else:
            print("You can only enter Odd/Even")
    return bet_num
def game1() :
	game() #game start
