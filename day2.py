import sys

def calculate_wrapping(presents):
	total_wrapping = 0
	for present in presents:
		l, w, h = present
		surface_area = 2*l*w + 2*w*h + 2*h*l
		slack = min(l*w, w*h, h*l)
		wrapping = surface_area + slack
		total_wrapping += wrapping
	return total_wrapping

def calculate_ribbon(presents):
	total_ribbon = 0
	for present in presents:
		l, w, h = present
		shortest_side = min(2*l + 2*w, 2*w + 2*h, 2*h + 2*l)
		cubic_feet = l*w*h
		ribbon = shortest_side + cubic_feet
		total_ribbon += ribbon
	return total_ribbon
	
	
def main():
	if len(sys.argv) != 2:
		print "USAGE: python sourcefile"
		sys.exit(1)
	else:
		with open(sys.argv[1]) as fh:
			data = fh.read().strip()
		
		presents = []
		for line in data.split('\n'):
			line = line.strip()
			l, w, h = line.split('x')
			presents.append( (int(l),int(w),int(h)) )
		
		wrapping_needed = calculate_wrapping(presents)
		print wrapping_needed
		ribbon_needed = calculate_ribbon(presents)
		print ribbon_needed
		
		
if __name__ == "__main__":
	main()
	