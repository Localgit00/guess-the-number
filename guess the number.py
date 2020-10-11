#Игра Угадай число от 1 до 20 за 5 попыток.

import random
print('Hello, what is your name?')
name=input()
secretNumber=random.randint(1,20)
print('Well,'+name+', i thinking of a number between 1 and 20')

for guessTaken in range (1,6):
	
	try:
		print('Take a guess. Your try is '+str(guessTaken))
		guess=int(input())
		if guess<secretNumber:
			print('Your guess is too low.')
		elif guess>secretNumber:
			print('Your guess is too high.')
		else:
			break #Правильный ответ?
	except ValueError:

		print('Error')

if guess==secretNumber:
	print('Угадал! Я загадал число '+ str(secretNumber)+'. Ты угадал за '+str(guessTaken)+' шаг(а/ов)')
else:
	print('Nope. Я загадал число '+ str(secretNumber))
