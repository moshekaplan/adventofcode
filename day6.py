import re
import sys

DEBUG = False
def print_dbg(*msg):
    if DEBUG:
        print msg


def solve(data):
    grid = {}
    for x in range(1000):
        for y in range(1000):
            grid[(x,y)] = 0
    
    for line in data:
        m = re.search(r'([\w ]+) ([\d]+),([\d]+) through ([\d]+),([\d]+)', line)
        op = m.group(1)
        start_x = int(m.group(2))
        start_y = int(m.group(3))
        end_x = int(m.group(4))
        end_y = int(m.group(5))
        print_dbg(op, start_x, start_y, end_x, end_y)
    
        for x in xrange(start_x, end_x+1):
            for y in xrange(start_y, end_y+1):
                if op == 'turn on':
                    grid[(x,y)] = 1
                elif op == 'turn off':
                    grid[(x,y)] = 0
                elif op == 'toggle':
                    grid[(x,y)] = (grid[(x,y)] + 1) % 2
                else:
                    raise Exception("Invalid op" + op)
    return sum(grid.values())

def solve2(data):
    grid = {}
    for x in range(1000):
        for y in range(1000):
            grid[(x,y)] = 0
    
    for line in data:
        m = re.search(r'([\w ]+) ([\d]+),([\d]+) through ([\d]+),([\d]+)', line)
        op = m.group(1)
        start_x = int(m.group(2))
        start_y = int(m.group(3))
        end_x = int(m.group(4))
        end_y = int(m.group(5))
        print_dbg(op, start_x, start_y, end_x, end_y)
    
        for x in xrange(start_x, end_x+1):
            for y in xrange(start_y, end_y+1):
                if op == 'turn on':
                    grid[(x,y)] = grid[(x,y)] + 1
                elif op == 'turn off':
                    grid[(x,y)] = max(grid[(x,y)]-1, 0)
                elif op == 'toggle':
                    grid[(x,y)] = grid[(x,y)] + 2
                else:
                    raise Exception("Invalid op" + op)
    return sum(grid.values())    
    
def main():
    with open(sys.argv[1]) as fh:
        data = fh.read().split('\n')
    print solve(data)
    print solve2(data)

if __name__ == "__main__":
    if sys.argv < 2:
        print "USAGE: python %s file.dat" % sys.argv[0]
        sys.exit(1)
    main()