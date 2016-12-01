"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?

Your puzzle answer was 307.

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Your puzzle answer was 165.
"""

import sys

def main():
    if len(sys.argv) < 2:
        print "Needs input filename"
        print "USAGE: %s %s <filename>" % (sys.executable, sys.argv[0])
        sys.exit(1)
    
    arg_fname = sys.argv[1]
    fdata = open(arg_fname, 'r').read()
    solve_part1(fdata)

def solve_part1(fdata):
    UP, RIGHT, DOWN, LEFT = range(4)
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    facing_direction = UP
    pos_x = 0
    pos_y = 0
    
    steps = fdata.split(', ')
    for step in steps:
        turn = step[0]
        num_steps = int(step[1:])
        
        if turn == 'R':
            facing_direction = (facing_direction + 1) % len(DIRECTIONS)
        elif turn == 'L':
            facing_direction = (facing_direction - 1) % len(DIRECTIONS)
            
        if facing_direction == UP:
            pos_y += num_steps
        elif facing_direction == RIGHT:
            pos_x += num_steps
        elif facing_direction == DOWN:
            pos_y -= num_steps
        elif facing_direction == LEFT:
            pos_x -= num_steps
        
    print "Final position is pos_x: %d, pos_y: %d" % (pos_x, pos_y)
    print "Total distance is %d" % (abs(pos_x) + abs(pos_y))


def solve_part2(fdata):
    UP, RIGHT, DOWN, LEFT = range(4)
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

    facing_direction = UP
    pos_x = 0
    pos_y = 0
    
    visited = set()

    pos = pos_x, pos_y
    visited.add(pos)

    revisited = False
    steps = fdata.split(', ')
    for step in steps:
            
        turn = step[0]
        num_steps = int(step[1:])
        
        if turn == 'R':
            facing_direction = (facing_direction + 1) % len(DIRECTIONS)
        elif turn == 'L':
            facing_direction = (facing_direction - 1) % len(DIRECTIONS)
        
        for i in range(num_steps):
            if facing_direction == UP:
                pos_y += 1
            elif facing_direction == RIGHT:
                pos_x += 1
            elif facing_direction == DOWN:
                pos_y -= 1
            elif facing_direction == LEFT:
                pos_x -= 1
        
            pos = pos_x, pos_y
            if pos in visited:
               revisited = True 
               break
            else:
                visited.add(pos)
        if revisited:
            break
        
    print "Final position is pos_x: %d, pos_y: %d" % (pos_x, pos_y)
    print "Total distance is %d" % (abs(pos_x) + abs(pos_y))

    
if __name__ == "__main__":
    #main()
    fdata = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"
    fdata = "R8, R4, R4, R8"
    solve_part2(fdata)
