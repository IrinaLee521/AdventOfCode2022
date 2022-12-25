import heapq

def day1(filename):
	minH = []
	heapq.heappush(minH, -1)

	# process input
	f = open(filename, 'r')
	line = f.readline()
	load = 0
	while line:
		line = line.rstrip()
		if len(line) == 0:
			load = 0
		else:
			load += int(line)
			if load > minH[0]:
				if len(minH) < 3:
					heapq.heappush(minH, load)
				else:
					heapq.heapreplace(minH, load)
		line = f.readline()
	f.close()
	print(sum(minH))

day1("day1input.txt")