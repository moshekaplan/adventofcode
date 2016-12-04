"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

Your puzzle answer was 1050.

--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

Your puzzle answer was 1921.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

def is_triangle(s1, s2, s3):
    sides = sorted([s1, s2, s3])
    smaller_sum = sides[0] + sides[1]
    largest = sides[2]
    if smaller_sum > largest:
        return True
    else:
        return False

        
def solve_1():
    cnt_valid = 0
    data = open('input.txt').read()
    lines = data.split('\n')
    for line in lines:
        s1, s2, s3 = [int(s) for s in line.split()]
        if is_triangle(s1, s2, s3):
            cnt_valid += 1
    print cnt_valid

def examine_3_lines(line1, line2, line3):
    # Returns count of valid triangles
    # Each line is 3 numbers.
    s1, s2, s3 = [int(s) for s in line1.split()]
    s4, s5, s6 = [int(s) for s in line2.split()]
    s7, s8, s9 = [int(s) for s in line3.split()]
    
    cnt_valid = 0
    columns = ( (s1, s4, s7), (s2, s5, s8), (s3, s6, s9))
    for column in columns:
        if is_triangle(*column):
            cnt_valid += 1
    return cnt_valid
        
    
    
def solve_2():
    cnt_valid = 0
    data = open('input.txt').read()
    lines = data.split('\n')
    for i in range(0, len(lines), 3):
        line1, line2, line3 = lines[i:i+3]
        cnt_valid += examine_3_lines(line1, line2, line3)
    print cnt_valid
    
solve_2()