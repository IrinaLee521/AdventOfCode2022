import heapq

def day4_part1(filename):
	numRanges = 0

	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		rangeNums = parseRanges(line)
		# first range contains second range
		if rangeNums[0][0] <= rangeNums[1][0] and rangeNums[0][1] >= rangeNums[1][1]:
			numRanges += 1
		# second range contains first range
		elif rangeNums[0][0] >= rangeNums[1][0] and rangeNums[0][1] <= rangeNums[1][1]:
			numRanges += 1
		line = f.readline()

	print(numRanges)
	f.close()
	

def day4_part2(filename):
	numRanges = 0

	# process input
	f = open(filename, 'r')
	line = f.readline()
	while line:
		line = line.rstrip()
		rangeNums = parseRanges(line)
		rangeNums = sorted(rangeNums, key=lambda x: x[0])

		if rangeNums[0][1] >= rangeNums[1][0]:
			numRanges += 1
		line = f.readline()

	print(numRanges)
	f.close()

def parseRanges(line):
	ranges = line.split(",")
	firstRange = ranges[0]
	sndRange = ranges[1]
	nums = firstRange.split("-")
	nums2 = sndRange.split("-")
	return [[int(nums[0]), int(nums[1])], [int(nums2[0]), int(nums2[1])]]

day4_part1("day4input.txt")
day4_part2("day4input.txt")