#Игра Угадай число от 1 до 20 за 5 попыток.

import random
print('Привет, как тебя зовут?')
name=input()
secretNumber=random.randint(1,20)
print('Отлично,'+name+', я загадал число от 1 до 20')

for guessTaken in range (1,6):
	
	try:
		print('Угадай! Твоя попытка номер '+str(guessTaken))
		guess=int(input())
		if guess<secretNumber:
			print('Твой ответ меньше.')
		elif guess>secretNumber:
			print('Твой ответ больше.')
		else:
			break #Правильный ответ?
	except ValueError:

		print('Error')

if guess==secretNumber:
	print('Yes! Я загадал число '+ str(secretNumber)+'. Ты угадал за '+str(guessTaken)+' шаг(а/ов)')
else:
	print('Nope. Я загадал число '+ str(secretNumber))
