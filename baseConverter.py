def isBaseX(numString, numBase):
	for num in numString:
		if (int(num) >= numBase):
			return False
	return True

def toBase10(numString, numBase):
	x = 0
	length = len(numString)
	for z in range(0, length):
		x += int(numString[z]) * (numBase ** (length - z - 1))
	return x

def toBaseX(number, numBase):
	x = ""
	n = number
	while (n//numBase != 0):
		x += str(n % numBase)
		n = n//numBase
	x += str(n % numBase)
	return int(x[::-1])

print("\nThis program converts a number in bases 2 to 10 to another number in bases 2 to 10\n")

num = input("Enter a number: ")

if not num.isnumeric():
	print("Numbers don't have letters!")
	quit()

initialBase = int(input("Enter that number's base: "))

if (not isBaseX(num, initialBase)):
	print("The number you entered isn't possible with your given base.")
	quit()

if (initialBase < 2) or (initialBase > 10):
	print("This program only supports bases between 2 and 10.")
	quit()

finalBase = int(input("Enter the base to translate your number into: "))

if (finalBase < 2) or (initialBase > 10):
	print("This program only supports bases between 2 and 10.")
	quit()

number = toBase10(num, initialBase)
newNumber = toBaseX(number, finalBase)

print("Your number is",newNumber)