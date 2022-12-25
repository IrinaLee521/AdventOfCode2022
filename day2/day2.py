import heapq

def day2_part1(filename):
	myMove = {'X' : 'Rock', 'Y': 'Paper', 'Z' : 'Scissors'}
	opMove = {'A' : 'Rock', 'B': 'Paper', 'C' : 'Scissors'}
	moveScore = {'Rock' : 1, 'Paper': 2, 'Scissors': 3}

	totalScore = 0

	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		moves = line.split(" ")

		opponent = opMove[moves[0]]
		me = myMove[moves[1]]

		score = moveScore[me]
		if me == opponent:
			score += 3
		else:
			if me == 'Rock' and opponent == 'Scissors':
				score += 6
			elif me == 'Scissors' and opponent == 'Paper':
				score += 6
			elif me == 'Paper' and opponent == 'Rock':
				score += 6
		totalScore += score

		line = f.readline()

	print(totalScore)
	f.close()
	

def day2_part2(filename):
	opMove = {'A' : 'Rock', 'B': 'Paper', 'C' : 'Scissors'}
	moveScore = {'Rock' : 1, 'Paper': 2, 'Scissors': 3}
	outcomeScore = {'X' : 0, 'Y' : 3, 'Z': 6}
	winDict = {'Rock' : 'Paper', 'Scissors' : 'Rock', 'Paper' : 'Scissors'}
	loseDict = {'Rock' : 'Scissors', 'Scissors' : 'Paper', 'Paper' : 'Rock'}

	totalScore = 0

	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		moves = line.split(" ")

		opponent = opMove[moves[0]]
		outcome = moves[1]

		score = outcomeScore[outcome]
		if outcome == 'Y':
			me = opponent
		elif outcome == 'X':
			me = loseDict[opponent]
		elif outcome == 'Z':
			me = winDict[opponent]
		score += moveScore[me]

		totalScore += score

		line = f.readline()

	print(totalScore)
	f.close()

day2_part1("day2input.txt")
day2_part2("day2input.txt")