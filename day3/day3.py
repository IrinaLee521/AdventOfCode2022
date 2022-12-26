import heapq

def day3_part1(filename):
	totalPriority = 0

	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		mid = int(len(line)/2)
		first = line[:mid]
		snd = line[mid:]

		letter_set = (set(first)) & (set(snd))
		letter = letter_set.pop()
		totalPriority += find_priority(letter)

		line = f.readline()

	print(totalPriority)
	f.close()
	

def day3_part2(filename):
	totalPriority = 0

	# process input
	f = open(filename, 'r')
	line = f.readline()
	i = 0
	group = []
	while line:
		line = line.rstrip()
		group.append(line)
		if (i+1) % 3 == 0:
			letter_set = set(group[0]) & set(group[1]) & set(group[2])
			letter = letter_set.pop()
			totalPriority += find_priority(letter)
			group = []
		
		line = f.readline()
		i += 1

	print(totalPriority)
	f.close()

def find_priority(letter):
	if letter.isupper():
		priority = ord(letter) - 38
	else:
		priority = ord(letter) - 96
	return priority

day3_part1("day3input.txt")
day3_part2("day3input.txt")