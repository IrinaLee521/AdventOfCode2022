
def day6_part1(filename):
	global freq
	f = open(filename, 'r')
	inputLine = f.readline()
	# initizlie 4-char window
	i = 0
	j = 0
	freq = dict()
	while j < 4:
		addNewLetter(inputLine[j])
		j += 1
	# find marker
	while j < len(inputLine):
		if len(freq) == 4:
			return j
		addNewLetter(inputLine[j])
		freq[inputLine[i]] -= 1
		if freq[inputLine[i]] == 0:
			freq.pop(inputLine[i])
		i += 1
		j += 1
	f.close()
	

def day6_part2(filename):
	global freq
	f = open(filename, 'r')
	inputLine = f.readline()
	# initizlie 4-char window
	i = 0
	j = 0
	freq = dict()
	while j < 14:
		addNewLetter(inputLine[j])
		j += 1
	# find marker
	while j < len(inputLine):
		if len(freq) == 14:
			return j
		addNewLetter(inputLine[j])
		freq[inputLine[i]] -= 1
		if freq[inputLine[i]] == 0:
			freq.pop(inputLine[i])
		i += 1
		j += 1
	f.close()

def addNewLetter(curr):
	global freq
	if curr not in freq:
		freq[curr] = 1
	else:
		freq[curr] += 1

print(day6_part1("day6input.txt"))
print(day6_part2("day6input.txt"))