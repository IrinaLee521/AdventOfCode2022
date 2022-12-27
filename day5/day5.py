
def day5_part1(filename):
	global arr
	arr = []
	numStacks = findNumStacks(filename)
	# initialize matrix
	for i in range(numStacks):
		arr.append([])
	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		if len(line) > 0:
			if line[0] != 'm':
				parseStackLine(line)
			else:
				numCrates, src, dst = parseInstructionLine(line)
				for i in range(numCrates):
					crate = arr[src-1].pop()
					arr[dst-1].append(crate)
		line = f.readline()
	# finalize output
	result = ""
	for stack in arr:
		result += stack[-1]
	print(result)
	f.close()
	

def day5_part2(filename):
	global arr
	arr = []
	numStacks = findNumStacks(filename)
	# initialize matrix
	for i in range(numStacks):
		arr.append([])
	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		if len(line) > 0:
			if line[0] != 'm':
				parseStackLine(line)
			else:
				numCrates, src, dst = parseInstructionLine(line)
				pileToMove = arr[src-1][-1 * numCrates:]
				arr[src-1] = arr[src-1][:-1 * numCrates]
				arr[dst-1] += pileToMove
		line = f.readline()
	# finalize output
	result = ""
	for stack in arr:
		result += stack[-1]
	print(result)
	f.close()

def findNumStacks(filename):
	f = open(filename, 'r')
	line = f.readline()
	numStacks = -1
	while line:
		line = line.strip()
		if len(line) > 0 and line[0].isnumeric():
			numStacks = int(line[-1])
		line = f.readline()
	f.close()
	return numStacks

def parseStackLine(line):
	global arr
	for i in range(1, len(line), 4):
		if line[i] != ' ':
			arr[(i-1)//4] = [line[i]] + arr[(i-1)//4] 

def parseInstructionLine(line):
	global arr
	numCrates = int(line[line.find('move')+5:line.find('from')-1])
	src = int(line[line.find('from')+5:line.find('to')-1])
	dst = int(line[line.find('to')+3:])
	return [numCrates, src, dst]

day5_part1("day5input.txt")
day5_part2("day5input.txt")