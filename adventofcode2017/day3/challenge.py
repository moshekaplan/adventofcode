"""
--- Day 3: Spiral Memory ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 277678.

Your puzzle answer was 475.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 277678.


"""

import math

def find_position1(goal_position_num):
    spiral_num = int(math.sqrt(goal_position_num))
    if spiral_num %2 == 0:
        spiral_num -= 1
    prev_spiral_end = spiral_num**2
    next_spiral_end = (spiral_num+2)**2
    numbers_per_side = (next_spiral_end - prev_spiral_end)//4
    
    x_displacement = (spiral_num-1)/2
    y_displacement = -(spiral_num-1)/2
    current_position_num = prev_spiral_end
    
    if current_position_num == goal_position_num:
        return abs(x_displacement) + abs(y_displacement)
        
    # steps are 1 to the right, 1/4-1 up, 1/4 left, 1/4 down, 1/4 right
    # Move 1 to the right
    x_displacement += 1
    current_position_num += 1
    if current_position_num == goal_position_num:
        return abs(x_displacement) + abs(y_displacement)
    
    # Move 1/4-1 up
    for i in xrange(numbers_per_side-1):
        current_position_num += 1
        y_displacement += 1
        if current_position_num == goal_position_num:
            return abs(x_displacement) + abs(y_displacement)

    # Move 1/4 left
    for i in xrange(numbers_per_side):
        current_position_num += 1
        x_displacement -= 1
        if current_position_num == goal_position_num:
            return abs(x_displacement) + abs(y_displacement)

    # Move 1/4 down
    for i in xrange(numbers_per_side):
        current_position_num += 1
        y_displacement -= 1
        if current_position_num == goal_position_num:
            return abs(x_displacement) + abs(y_displacement)

    # Move 1/4 right
    for i in xrange(numbers_per_side):
        current_position_num += 1
        x_displacement += 1
        if current_position_num == goal_position_num:
            return abs(x_displacement) + abs(y_displacement)            
    raise Exception("Couldn't find it!")


    
def tests1():
    tests = [
        [1, 0],
        [12, 3],
        [23, 2],
        [1024, 31]
    ]
    success = True
    test_function = find_position1
    for input, output in tests:
        test_result = test_function(input)
        if test_result != output:
            print "TEST FAILED input:%s, output: %s, expected: %s" % (input, test_result, output)
            success = False
    return success
    
# Maps (x,y) -> number
coords_position = {}  
    
# Maps (x,y) -> sum
# positions_numbers = {}
# positions_numbers[(0, 0)] = 1

#def sum_surrounding(x, y):
#    return sum(positions_numbers.get(( x+i, y+j),0) for i in range(-1, 1+1) for j in range(-1, 1+1)) - positions_numbers((x,y))

xy_to_number = {}
number_to_xy = {}
xy_to_sums = {(0,0):1}

def calc_sum(x, y):
    return xy_to_sums.get((x-1,y-1), 0) + xy_to_sums.get((x,y-1), 0) + xy_to_sums.get((x+1,y-1), 0) + \
    xy_to_sums.get((x-1,y), 0) + xy_to_sums.get((x,y), 0) + xy_to_sums.get((x+1,y), 0) + \
    xy_to_sums.get((x-1,y+1), 0) + xy_to_sums.get((x,y+1), 0) + xy_to_sums.get((x+1,y+1), 0)

def find_sums(goal):
    for spiral_num in xrange(1, 10000, 2):
        prev_spiral_end = spiral_num**2
        next_spiral_end = (spiral_num+2)**2
        numbers_per_side = (next_spiral_end - prev_spiral_end)//4
        
        x_coords = (spiral_num-1)/2
        y_coords = -(spiral_num-1)/2
        current_position_num = prev_spiral_end
        
        xy_to_number[(x_coords, y_coords)] = current_position_num
        number_to_xy[current_position_num] = (x_coords, y_coords)
        xy_to_sums[(x_coords, y_coords)] = calc_sum(x_coords, y_coords)
        print (x_coords, y_coords), xy_to_sums[(x_coords, y_coords)]
        if xy_to_sums[(x_coords, y_coords)] > goal:
            return xy_to_sums[(x_coords, y_coords)]
        
        # steps are 1 to the right, 1/4-1 up, 1/4 left, 1/4 down, 1/4 right
        # Move 1 to the right
        x_coords += 1
        current_position_num += 1
        xy_to_number[(x_coords, y_coords)] = current_position_num
        number_to_xy[current_position_num] = (x_coords, y_coords)
        xy_to_sums[(x_coords, y_coords)] = calc_sum(x_coords, y_coords)
        print (x_coords, y_coords), xy_to_sums[(x_coords, y_coords)]
        if xy_to_sums[(x_coords, y_coords)] > goal:
            return xy_to_sums[(x_coords, y_coords)]
            
        # Move 1/4-1 up
        for i in xrange(numbers_per_side-1):
            current_position_num += 1
            y_coords += 1
            xy_to_number[(x_coords, y_coords)] = current_position_num
            number_to_xy[current_position_num] = (x_coords, y_coords)
            xy_to_sums[(x_coords, y_coords)] = calc_sum(x_coords, y_coords)
            print (x_coords, y_coords), xy_to_sums[(x_coords, y_coords)]
            if xy_to_sums[(x_coords, y_coords)] > goal:
                return xy_to_sums[(x_coords, y_coords)]

        # Move 1/4 left
        for i in xrange(numbers_per_side):
            current_position_num += 1
            x_coords -= 1
            xy_to_number[(x_coords, y_coords)] = current_position_num
            number_to_xy[current_position_num] = (x_coords, y_coords)
            xy_to_sums[(x_coords, y_coords)] = calc_sum(x_coords, y_coords)
            print (x_coords, y_coords), xy_to_sums[(x_coords, y_coords)]
            if xy_to_sums[(x_coords, y_coords)] > goal:
                return xy_to_sums[(x_coords, y_coords)]
                
        # Move 1/4 down
        for i in xrange(numbers_per_side):
            current_position_num += 1
            y_coords -= 1
            xy_to_number[(x_coords, y_coords)] = current_position_num
            number_to_xy[current_position_num] = (x_coords, y_coords)
            xy_to_sums[(x_coords, y_coords)] = calc_sum(x_coords, y_coords)
            print (x_coords, y_coords), xy_to_sums[(x_coords, y_coords)]
            if xy_to_sums[(x_coords, y_coords)] > goal:
                return xy_to_sums[(x_coords, y_coords)]
            
        # Move 1/4 right
        for i in xrange(numbers_per_side-1):
            current_position_num += 1
            x_coords += 1
            xy_to_number[(x_coords, y_coords)] = current_position_num
            number_to_xy[current_position_num] = (x_coords, y_coords)
            xy_to_sums[(x_coords, y_coords)] = calc_sum(x_coords, y_coords)
            print (x_coords, y_coords), xy_to_sums[(x_coords, y_coords)]
            if xy_to_sums[(x_coords, y_coords)] > goal:
                return xy_to_sums[(x_coords, y_coords)]
    
if __name__ == "__main__":
    tests1()
    data = 277678
    print find_position1(data)
    
    print find_sums(277678)
    #print checksum_sheet2(data)