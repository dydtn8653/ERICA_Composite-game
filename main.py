import Odd_Even
import Up_Down
import Number_BaseBall
print("\n****Welcome to the Composite game.****")
while True:
	print("\n    1. Odd and Even game\n    2. Up and Down\n    3. Number BaseBall\n    4. Exit")
	a = int(input("  Please select the game you want.\n  Game Number: "))
	if a==1 :
		Odd_Even.game1()
	elif a==2 :
		Up_Down.game2()
	elif a==3 :
		Number_BaseBall.game3()
	elif a==4 :
		print("\n  **Thank you for playing the game.**")
		break
	else :
		print("        **Error**")
		print("**Please re-enter the number**")

