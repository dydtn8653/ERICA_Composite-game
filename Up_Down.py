import random
def GAMEUPDOWN():
	# random "UP DOWN" game

	rn = random.randrange(1, 101, 1)
	num = -1

	t_cnt = 0 # Try
	
	print("1~100 Number Up & Down Game start !!!")
	print("---------------------------")
	while ( rn != num ):
	
	    num = int(input("Please enter a number between 1 ~ 100. : "))
	
	    if (num > rn):
	        print("Down")
	    elif (num < rn):
	        print("Up")

	    t_cnt += 1
	print("---------------------------")
	print("You got the right answer in", t_cnt, "times.")
def game2():
	GAMEUPDOWN()
