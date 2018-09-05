from hangmantextart import hangmanPics, wordToBlanks
import random

selection = random.choice(list(open('phrases.txt')))

lowerCase = selection.lower()
blanks = list(wordToBlanks(selection))

i = 0
alreadyGuessed = []

while(True):

	if '-' not in blanks:

		print('\n' + "".join(blanks).capitalize() + '\n' + 'YOU WIN!')
		break

	print(hangmanPics[i] + '\n\n' + "".join(blanks) + '\n')

	guess = input("Guess your letter: ")
	formattedGuess = guess.lower()

	if (len(formattedGuess) != 1 or not formattedGuess.isalpha()):
	
		print('\n' + 'INVALID GUESS')
		continue

	if formattedGuess in alreadyGuessed:
		print('\n' + "YOU'VE ALREADY GUESSED THAT LETTER")
		continue

	if formattedGuess in lowerCase:

		alreadyGuessed.append(formattedGuess)
		occurances = []

		for x in range(len(lowerCase)):

			if formattedGuess == lowerCase[x]:

				occurances.append(x)

		for y in occurances:

			blanks[y] = formattedGuess

	else:

		i += 1

		if (i == (len(hangmanPics) - 1)):

			print(hangmanPics[i] + '\n\n' + 'GAME OVER! The phrase was:')
			print('\n' + selection)
			break




#for x in range(0, len(hangmanPics)):
#	print(hangmanPics[x])