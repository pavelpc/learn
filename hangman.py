# модули
import random

# константы
# список слов
word_list = ['python', 'java', 'kotlin', 'javascript']
# загадываем слово
word_pc = random.choice(word_list)
# считаем буквы
len_ = len(word_pc)
# скрываем часть слова
part_len = len_ - 3
hidden = '-' * part_len
# поле догадок
guess = '-' * len_
# меняем поле
guess = list(guess)# попытки
tries = 8
# это я уже видел
was = []
action = ''
# привет
print('H A N G M A N')
print('The game will be available soon.')
while action != 'exit' :
	print('H A N G M A N')
	# что делать?
	action = input('Type "play" to play the game, "exit" to quit:')
	if action == "exit" :
		exit()
	# есть попытки и слово не угадано
	while tries > 0 and '-' in guess :
		# пробел
		print()
		# рисуем поле
		print(''.join(guess))
		# ваша буква
		letter = input('Input a letter:')
		# 1 буква!!
		if len(letter) != 1 :
			print('You should print a single letter')
			continue
		# только букв
		if not letter.isascii() or not letter.islower() :
			print('It is not an ASCII lowercase letter')
			continue
		# не повторяйся
		if letter in set(was) :  # было
			print('You already typed this letters')  # ы
			continue  # о
		# дибил да??
		if letter in set(guess) :  # было
			print('No improvements')  # ы
			tries -= 1  # л
			continue  # о
		# запомнили
		was.append(letter)
		# буква в слове?
		if letter in set(word_pc) :
			# перебор букв
			for i in word_pc :
				# индекс
				j = [j for j, x in enumerate(word_pc) if i in x][0]
				# нашел
				if i == letter :
					# записал
					guess[j] = i
		# неа
		else :
			print('No such letter in the word')
			tries -= 1
		# формирую результат
		word = ''.join(guess)
	# вывожу результат
	print('Guess the word', word_pc, 'you: >', word)
	# проверяю
	if word == word_pc :
		print('You guessed the word!!')
		print('You survived!')
	# ты труп
	else :
		print('You are hanged!')
