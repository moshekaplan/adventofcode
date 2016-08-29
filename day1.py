import sys

def find_floor(directions):

	up = directions.count('(')
	down = directions.count(')')
	
	end_floor = up - down
	return end_floor

def find_floor2(directions):

	floor = 0
	
	for i, step in enumerate(directions):
		if step == '(':
			floor += 1
		elif step == ')':
			floor -= 1
			
		if floor == -1:
			return i	
	
	
def main():
	if len(sys.argv) != 2:
		print "USAGE: python sourcefile"
		sys.exit(1)
	else:
		with open(sys.argv[1]) as fh:
			data = fh.read().strip()
		print find_floor2(data)
		
if __name__ == "__main__":
	main()
	