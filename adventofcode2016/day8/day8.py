"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

Your puzzle answer was 128.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

"""
import re
import copy

ROW_LENGTH = 50
COLUMN_LENGTH = 6

def create_pixels():
    # The screen is 50 pixels wide and 6 pixels tall, all of which start off:
    # The screen is accessed as [y][x]
    # 0,0 0,1 0,2
    # 1,0 1,1 1,2
    # 2,0 2,1 2,2
    pixels = []
    for row in range(COLUMN_LENGTH):
        pixels.append([False for i in range(ROW_LENGTH)])
    return pixels

def rect(pixels, A, B):
    # rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    """
    rect 3x2 creates a small rectangle in the top-left corner:
    ###....
    ###....
    .......
    """
    for x in range(A):
        for y in range(B):
            pixels[y][x] = True
    return pixels
            

def copy_rect(pixels):
    return copy.deepcopy(pixels)
    
def rotate_row(pixels, A, B):
    # "rotate row y=A by B" shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
    # effectively shift and rotate
    pixels_copy = copy_rect(pixels)
    for x in range(ROW_LENGTH):
        pixels[A][(x+B) % ROW_LENGTH] = pixels_copy[A][x]
    
def rotate_column(pixels, A, B):
    # "rotate column x=A by B" shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
    # effectively shift and rotate
    pixels_copy = copy_rect(pixels)
    for y in range(COLUMN_LENGTH):
        pixels[(y+B) % COLUMN_LENGTH][A] = pixels_copy[y][A]

def print_pixels(pixels):
    for row in pixels:
        out = []
        for pixel in row:
            #print pixel
            if pixel:
                out.append('#')
            else:
                out.append('.')
        print "".join(out)
    print
    
def count_pixels(pixels):
    cnt = 0
    for row in pixels:
        for pixel in row:
            if pixel:
                cnt += 1
    return cnt

def test_phase1():
    pixels = create_pixels()
    print_pixels(pixels)
    rect(pixels, 3, 2)
    print_pixels(pixels)
    rotate_column(pixels, 1,1)
    print_pixels(pixels)
    rotate_row(pixels, 0,4)
    print_pixels(pixels)
    rotate_column(pixels, 1,1)
    print_pixels(pixels)
    
    
def parse_data(data):
    commands = []
    lines = data.split('\n')
    for line in lines:
        if 'rect' in line:
            m = re.search('rect (\d+)x(\d+)', line)
            if m is None:
                print line
            cmd = {'cmd':'rect', 'A':int(m.group(1)), 'B':int(m.group(2)) }
        if 'column' in line:
            m = re.search('rotate column x=(\d+) by (\d+)', line)
            cmd = {'cmd':'column', 'A':int(m.group(1)), 'B':int(m.group(2)) }
            if m is None:
                print line
        if 'row' in line:
            m = re.search('rotate row y=(\d+) by (\d+)', line)
            cmd = {'cmd':'row', 'A':int(m.group(1)), 'B':int(m.group(2)) }
            if m is None:
                print line
        commands.append(cmd)
    return commands

def run_commands(pixels, commands):
    for cmd in commands:
        if cmd['cmd'] == 'rect':
            rect(pixels, cmd['A'], cmd['B'])
        if cmd['cmd'] == 'column':
            rotate_column(pixels, cmd['A'], cmd['B'])
        if cmd['cmd'] == 'row':
            rotate_row(pixels, cmd['A'], cmd['B'])

def phase1(commands):
    pixels = create_pixels()
    run_commands(pixels, commands)
    print count_pixels(pixels)

def phase2(commands):
    pixels = create_pixels()
    run_commands(pixels, commands)
    print_pixels(pixels)
    
def main():
    commands = parse_data(data)
    phase1(commands)
    phase2(commands)

data = """\
rect 1x1
rotate row y=0 by 7
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 7
rect 6x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 10
rotate row y=0 by 3
rotate column x=0 by 1
rect 2x1
rotate column x=20 by 1
rotate column x=15 by 1
rotate column x=5 by 1
rotate row y=1 by 5
rotate row y=0 by 2
rect 1x2
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 15
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=8 by 1
rotate column x=5 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=27 by 1
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=42 by 1
rotate column x=40 by 1
rotate column x=22 by 1
rotate column x=17 by 1
rotate column x=12 by 1
rotate column x=7 by 1
rotate column x=2 by 1
rotate row y=3 by 10
rotate row y=2 by 5
rotate row y=1 by 3
rotate row y=0 by 10
rect 1x4
rotate column x=37 by 2
rotate row y=3 by 18
rotate row y=2 by 30
rotate row y=1 by 7
rotate row y=0 by 2
rotate column x=13 by 3
rotate column x=12 by 1
rotate column x=10 by 1
rotate column x=7 by 1
rotate column x=6 by 3
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=38 by 3
rotate row y=3 by 12
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=7 by 1
rotate column x=5 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=4 by 20
rotate row y=3 by 25
rotate row y=2 by 10
rotate row y=0 by 15
rotate column x=12 by 1
rotate column x=10 by 1
rotate column x=8 by 3
rotate column x=7 by 1
rotate column x=5 by 1
rotate column x=3 by 3
rotate column x=2 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=34 by 1
rotate row y=1 by 45
rotate column x=47 by 1
rotate column x=42 by 1
rotate column x=19 by 1
rotate column x=9 by 2
rotate row y=4 by 7
rotate row y=3 by 20
rotate row y=0 by 7
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 6x1
rotate row y=4 by 8
rotate row y=3 by 5
rotate row y=1 by 5
rotate column x=5 by 1
rotate column x=4 by 1
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=1 by 3
rotate column x=0 by 1
rect 6x1
rotate column x=36 by 3
rotate column x=25 by 3
rotate column x=18 by 3
rotate column x=11 by 3
rotate column x=3 by 4
rotate row y=4 by 5
rotate row y=3 by 5
rotate row y=2 by 8
rotate row y=1 by 8
rotate row y=0 by 3
rotate column x=3 by 4
rotate column x=0 by 4
rect 4x4
rotate row y=4 by 10
rotate row y=3 by 20
rotate row y=1 by 10
rotate row y=0 by 10
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=0 by 40
rotate column x=44 by 1
rotate column x=35 by 5
rotate column x=18 by 5
rotate column x=15 by 3
rotate column x=10 by 5
rotate row y=5 by 15
rotate row y=4 by 10
rotate row y=3 by 40
rotate row y=2 by 20
rotate row y=1 by 45
rotate row y=0 by 35
rotate column x=48 by 1
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=40 by 1
rotate column x=38 by 2
rotate column x=37 by 3
rotate column x=36 by 2
rotate column x=32 by 2
rotate column x=31 by 2
rotate column x=28 by 1
rotate column x=23 by 3
rotate column x=22 by 3
rotate column x=21 by 5
rotate column x=20 by 1
rotate column x=18 by 1
rotate column x=17 by 3
rotate column x=13 by 1
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 5
rotate column x=6 by 5
rotate column x=5 by 1
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 5"""

if __name__ == "__main__":
    main()
