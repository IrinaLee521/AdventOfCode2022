
class Directory:

	def __init__(self, name, parent):
		self.name = name
		self.files = []
		self.dirs = {}
		self.parent = parent

def day7_part1(filename):
	global totalSizeUnderLimit
	global sizeMap
	totalSizeUnderLimit = 0
	sizeMap = {}
	root = buildTree(filename)
	calculateSize(root)
	print(totalSizeUnderLimit)


def day7_part2(filename):
	global sizeMap
	unusedSpace = 70000000 - sizeMap['/']
	spaceDiff = 30000000 - unusedSpace
	minDir = ""
	minSpace = float("inf")
	for d in sizeMap:
		if sizeMap[d] >= spaceDiff and sizeMap[d] < minSpace:
			minDir = d
			minSpace = sizeMap[d]
	print(minSpace)

def buildTree(filename):
	f = open(filename, 'r')
	line = f.readline()
	root = Directory('/', None)
	curr = root
	parent = None
	while line:
		line = line.strip()
		if line.find('$ cd ..') != -1:
			parent = parent.parent
			curr = curr.parent
		elif line.find('$ cd') != -1:
			if line != '$ cd /':
				dirName = line.split(' ')[2]
				parent = curr
				curr = curr.dirs[dirName]
		elif line.find('dir') == 0:
			dirName = line.split(' ')[1]
			curr.dirs[dirName] = Directory(dirName, curr)
		elif line[0].isnumeric():
			size = line.split(' ')[0]
			fileName = line.split(' ')[1]
			curr.files.append((fileName, size))
		line = f.readline()
	f.close()
	return root

def calculateSize(d):
	global totalSizeUnderLimit
	totalSize = 0
	for f in d.files:
		totalSize += int(f[1])
	for nextDir in d.dirs.keys():
		totalSize += calculateSize(d.dirs[nextDir])
	if totalSize < 100000:
		totalSizeUnderLimit += totalSize
	sizeMap[d.name] = totalSize
	return totalSize

day7_part1("day7input.txt")
day7_part2("day7input.txt")