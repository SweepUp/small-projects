class Group:
	name = ""
	country1 = ""
	country2 = ""
	country3 = ""
	country4 = ""
	winner = ""
	runnerUp = ""
	def __init__(self, nam, c1, c2, c3, c4):
		self.name = nam
		self.country1 = c1
		self.country2 = c2
		self.country3 = c3
		self.country4 = c4

class Match:
	name = ""
	country1 = ""
	country2 = ""
	winner = ""
	def __init__(self, nam, c1, c2):
		self.name = nam
		self.country1 = c1
		self.country2 = c2

groupA = Group("Group A", "Russia", "Egypt", "Uruguay", "Saudi Arabia")
groupB = Group("Group B", "Morocco", "Iran", "Portugal", "Spain")
groupC = Group("Group C", "France", "Denmark", "Australia", "Peru")
groupD = Group("Group D", "Argentina", "Iceland", "Nigeria", "Croatia")
groupE = Group("Group E", "Brazil", "Costa Rica", "Serbia", "Switzerland")
groupF = Group("Group F", "Germany", "Mexico", "South Korea", "Sweden")
groupG = Group("Group G", "Belgium", "Panama", "England", "Tunisia")
groupH = Group("Group H", "Poland", "Colombia", "Japan", "Senegal")

groups = [groupA, groupB, groupC, groupD, groupE, groupF, groupG, groupH]

for x in range(len(groups)):
	print("\nHere are the teams in "+groups[x].name+":")
	print("-" * 30)
	print(groups[x].country1+"\n"+groups[x].country2+"\n"+groups[x].country3+"\n"+groups[x].country4)
	print("-" * 30)
	while True:
		first = input("Who do you think will win this group?\n\n")
		if (first == groups[x].country1) or (first == groups[x].country2) or (first == groups[x].country3) or (first == groups[x].country4):
			groups[x].winner = first
			break
		else:
			print("\nEnter the country's name exactly as it is.")
	while True:
		second = input("\nWho do you think will be the runner-up?\n\n")
		if (second == groups[x].winner):
			print("\nYou've already selected them as the group winner!")
		elif (second == groups[x].country1) or (second == groups[x].country2) or (second == groups[x].country3) or (second == groups[x].country4):
			groups[x].runnerUp = second
			break
		else:
			print("\nEnter the country's name exactly as it is.")

roundOf16_1 = Match("1", groupA.winner, groupB.runnerUp)
roundOf16_2 = Match("2", groupC.winner, groupD.runnerUp)
roundOf16_3 = Match("3", groupB.winner, groupA.runnerUp)
roundOf16_4 = Match("4", groupD.winner, groupC.runnerUp)
roundOf16_5 = Match("5", groupE.winner, groupF.runnerUp)
roundOf16_6 = Match("6", groupG.winner, groupH.runnerUp)
roundOf16_7 = Match("7", groupF.winner, groupE.runnerUp)
roundOf16_8 = Match("8", groupH.winner, groupG.runnerUp)

roundOf16 = [roundOf16_1, roundOf16_2, roundOf16_3, roundOf16_4, roundOf16_5, roundOf16_6, roundOf16_7, roundOf16_8]

for x in range(len(roundOf16)):
	print("\nGame #"+roundOf16[x].name+" of the Round of Sixteen will be:")
	print("-" * 40)
	print(roundOf16[x].country1 + " vs. " + roundOf16[x].country2)
	print("-" * 40)
	while True:
		victor = input("Who do you think will win this game?\n\n")
		if (victor == roundOf16[x].country1) or (victor == roundOf16[x].country2):
			roundOf16[x].winner = victor
			break
		else:
			print("\nEnter the country's name exactly as it is.")

qrtrs1 = Match("1", roundOf16_1.winner, roundOf16_2.winner)
qrtrs2 = Match("2", roundOf16_5.winner, roundOf16_6.winner)
qrtrs3 = Match("3", roundOf16_7.winner, roundOf16_8.winner)
qrtrs4 = Match("4", roundOf16_3.winner, roundOf16_4.winner)

quarterFinals = [qrtrs1, qrtrs2, qrtrs3, qrtrs4]

for x in range(len(quarterFinals)):
	print("\nQuarter Final #"+quarterFinals[x].name+" will be:")
	print("~" * 25)
	print(quarterFinals[x].country1 + " vs. " + quarterFinals[x].country2)
	print("~" * 25)
	while True:
		nonLoser = input("Who do you think will win this game?\n\n")
		if (nonLoser == quarterFinals[x].country1) or (nonLoser == quarterFinals[x].country2):
			quarterFinals[x].winner = nonLoser
			break
		else:
			print("\nEnter the country's name exactly as it is.")

semi1 = Match("1", qrtrs1.winner, qrtrs2.winner)
semi2 = Match("2", qrtrs3.winner, qrtrs4.winner)

semiFinals = [semi1, semi2]

for x in range(len(semiFinals)):
	print("\nSemi Final #"+semiFinals[x].name+" will be:")
	print("><" * 11)
	print(semiFinals[x].country1 + " vs. " + semiFinals[x].country2)
	print("><" * 11)
	while True:
		finalist = input("Who do you think will win this game?\n\n")
		if (finalist == semiFinals[x].country1) or (finalist == semiFinals[x].country2):
			semiFinals[x].winner = finalist
			break
		else:
			print("\nEnter the country's name exactly as it is.")

print("\nHere are your teams in the World Cup final:")
print(">=" +"<=>" * 13 +"=<")
print(semi1.winner + " vs. " +semi2.winner)
print(">=" +"<=>" * 13 +"=<")
while True:
		champion = input("Who do you think will win this game?\n\n")
		if (champion == semi1.winner) or (champion == semi2.winner):
			print("\nYour World Cup 2018 champion is "+champion+"!")
			break
		else:
			print("\nEnter the country's name exactly as it is.")