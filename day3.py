import sys

def walk_houses(steps):
	visited = set()
	x, y = (0,0)
	
	position = (x,y)
	visited.add( position )
	for step in steps:
		if step == '^':
			y += 1
		elif step == 'v':
			y -= 1
		elif step == '<':
			x -= 1
		elif step == '>':
			x += 1
		position = (x,y)
		visited.add( position )
	return len(visited)

def walk_houses_part2(steps):
	visited = set()
	santa = [0,0]
	robo = [0,0]
	
	visited.add( tuple(santa) )
	
	walker = santa
	
	for step in steps:
		if step == '^':
			walker[1] += 1
		elif step == 'v':
			walker[1] -= 1
		elif step == '<':
			walker[0] -= 1
		elif step == '>':
			walker[0] += 1
		position = tuple(walker)
		visited.add( position )

		if walker == santa:
			walker = robo
		else:
			walker = santa
			
	return len(visited)	
	
	
def main():
	if len(sys.argv) != 2:
		print "USAGE: python stepsfile"
		sys.exit(1)
	else:
		with open(sys.argv[1]) as fh:
			steps = fh.read().strip()
		print walk_houses_part2(steps)
		
if __name__ == "__main__":
	main()
	