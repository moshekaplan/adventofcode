"""
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?

Your puzzle answer was 95549.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

You start at "5" and don't move at all (up and left are both edges), ending at 5.
Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
Finally, after five more moves, you end at 3.
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

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

def move_1(pos_x, pos_y, direction):
    if direction == "U":
        return pos_x, max(pos_y-1, 0)
    elif direction == "D":
        return pos_x, min(pos_y+1, 2)
    elif direction == "R":
        return min(pos_x+1, 2), pos_y
    elif direction == "L":
        return max(pos_x-1, 0), pos_y

def get_number_1(pos_x, pos_y):
    pad = ([1,2,3], [4,5,6], [7,8,9])
    return pad[pos_y][pos_x]
    
def solve_part1(fdata):
    pos_x = 1
    pos_y = 1
    
    lines = fdata.split()
    for line in lines:
        line = line.strip()
        for step in line:
            pos_x, pos_y = move_1(pos_x, pos_y, step)
        print get_number_1(pos_x, pos_y)



def move_2(pos_x, pos_y, direction):
    # Data is in a diamond of 5 x 5 in the center
    if direction == "U":
        attempt = pos_x, pos_y-1
    elif direction == "D":
        attempt = pos_x, pos_y+1
    elif direction == "R":
        attempt = pos_x+1, pos_y
    elif direction == "L":
        attempt = pos_x-1, pos_y

    #print get_number_2(pos_x, pos_y), "moving", direction
    if is_valid_2(*attempt):
        #print "success"
        return attempt
    else:
        #print "fail"
        return pos_x, pos_y

        
def is_valid_2(pos_x, pos_y):
    try:
        get_number_2(pos_x, pos_y)
        return True
    except:
        return False

def get_number_2(pos_x, pos_y):
    pad = ([None, None, 1, None, None], [None,2,3,4,None], [5,6,7,8,9], [None,'A','B','C',None], [None,None,'D',None,None])
    if -1 in [pos_x, pos_y]:
        raise Exception("invalid")
    value = pad[pos_y][pos_x]
    if value is None:
        raise Exception("invalid")
    return value
    
    
def solve_part2(fdata):
    pos_x = 0
    pos_y = 2
    #print get_number_2(pos_x, pos_y)
    lines = fdata.split()
    for line in lines:
        line = line.strip()
        for step in line:
            pos_x, pos_y = move_2(pos_x, pos_y, step)
            #print get_number_2(pos_x, pos_y)
            #print
        print get_number_2(pos_x, pos_y)

    
if __name__ == "__main__":
    fdata_test = """ULL
RRDDD
LURDL
UUUUD"""

    fdata = """ DLRURUDLULRDRUDDRLUUUDLDLDLRLRRDRRRLLLLLDDRRRDRRDRRRLRRURLRDUULRLRRDDLULRLLDUDLULURRLRLDUDLURURLDRDDULDRDRDLDLLULULLDDLRRUDULLUULRRLLLURDRLDDLDDLDRLRRLLRURRUURRRRLUDLRDDDDRDULRLLDDUURDUDRLUDULLUDLUDURRDRDUUUUDDUDLLLRLUULRUURDLRLLRRLRLLDLLRLLRRRURLRRLURRLDLLLUUDURUDDLLUURRDRDRRDLLDDLLRDRDRRLURLDLDRDLURLDULDRURRRUDLLULDUDRURULDUDLULULRRRUDLUURRDURRURRLRRLLRDDUUUUUDUULDRLDLLRRUDRRDULLLDUDDUDUURLRDLULUUDLDRDUUUDDDUDLDURRULUULUUULDRUDDLLLDLULLRLRLUDULLDLLRLDLDDDUUDURDDDLURDRRDDLDRLLRLRR
RLDUDURDRLLLLDDRRRURLLLRUUDDLRDRDDDUDLLUDDLRDURLDRDLLDRULDDRLDDDRLDRDDDRLLULDURRRLULDRLRDRDURURRDUDRURLDRLURDRLUULLULLDLUDUDRDRDDLDDDDRDURDLUDRDRURUDDLLLRLDDRURLLUDULULDDLLLDLUDLDULUUDLRLURLDRLURURRDUUDLRDDDDDRLDULUDLDDURDLURLUURDLURLDRURRLDLLRRUDRUULLRLDUUDURRLDURRLRUULDDLDLDUUDDRLDLLRRRUURLLUURURRURRLLLUDLDRRDLUULULUDDULLUDRLDDRURDRDUDULUDRLRRRUULLDRDRLULLLDURURURLURDLRRLLLDRLDUDLLLLDUUURULDDLDLLRRUDDDURULRLLUDLRDLUUDDRDDLLLRLUURLDLRUURDURDDDLLLLLULRRRURRDLUDLUURRDRLRUDUUUURRURLRDRRLRDRDULLDRDRLDURDDUURLRUDDDDDLRLLRUDDDDDURURRLDRRUUUDLURUUDRRDLLULDRRLRRRLUUUD
RDRURLLUUDURURDUUULLRDRLRRLRUDDUDRURLLDLUUDLRLLDDURRURLUDUDDURLURLRRURLLURRUDRUDLDRLLURLRUUURRUDDDURRRLULLLLURDLRLLDDRLDRLLRRDLURDLRDLDUDRUULLDUUUDLURRLLRUDDDUUURLURUUDRLRULUURLLRLUDDLLDURULLLDURDLULDLDDUDULUDDULLRDRURDRRLLDLDDDDRUDLDRRLLLRLLLRRULDLRLRLRLLDLRDRDLLUDRDRULDUURRDDDRLLRLDLDRDUDRULUDRDLDLDDLLRULURLLURDLRRDUDLULLDLULLUDRRDDRLRURRLDUDLRRUUDLDRLRLDRLRRDURRDRRDDULURUUDDUUULRLDRLLDURRDLUULLUDRDDDLRUDLRULLDDDLURLURLRDRLLURRRUDLRRLURDUUDRLRUUDUULLRUUUDUUDDUURULDLDLURLRURLRUDLULLULRULDRDRLLLRRDLU
RRRRDRLUUULLLRLDDLULRUUURRDRDRURRUURUDUULRULULRDRLRRLURDRRRULUUULRRUUULULRDDLLUURRLLDUDRLRRLDDLDLLDURLLUDLDDRRURLDLULRDUULDRLRDLLDLRULLRULLUDUDUDDUULDLUUDDLUDDUULLLLLURRDRULURDUUUDULRUDLLRUUULLUULLLRUUDDRRLRDUDDRULRDLDLLLLRLDDRRRULULLLDLRLURRDULRDRDUDDRLRLDRRDLRRRLLDLLDULLUDDUDDRULLLUDDRLLRRRLDRRURUUURRDLDLURRDLURULULRDUURLLULDULDUDLLULDDUURRRLDURDLUDURLDDRDUDDLLUULDRRLDLLUDRDURLLDRLDDUDURDLUUUUURRUULULLURLDUUULLRURLLLUURDULLUULDRULLUULRDRUULLRUDLDDLRLURRUUDRLRRRULRUUULRULRRLDLUDRRLL
ULRLDLLURDRRUULRDUDDURDDDLRRRURLDRUDDLUDDDLLLRDLRLLRRUUDRRDRUULLLULULUUDRRRDRDRUUUUULRURUULULLULDULURRLURUDRDRUDRURURUDLDURUDUDDDRLRLLLLURULUDLRLDDLRUDDUUDURUULRLLLDDLLLLRRRDDLRLUDDUULRRLLRDUDLLDLRRUUULRLRDLRDUDLLLDLRULDRURDLLULLLRRRURDLLUURUDDURLDUUDLLDDRUUDULDRDRDRDDUDURLRRRRUDURLRRUDUDUURDRDULRLRLLRLUDLURUDRUDLULLULRLLULRUDDURUURDLRUULDURDRRRLLLLLUUUULUULDLDULLRURLUDLDRLRLRLRDLDRUDULDDRRDURDDULRULDRLRULDRLDLLUDLDRLRLRUDRDDR"""
    
    solve_part2(fdata)
