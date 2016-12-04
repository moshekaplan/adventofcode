"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

Your puzzle answer was 245102.

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

Your puzzle answer was 324.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

import sys
import collections

def main():
    if len(sys.argv) < 2:
        print "Needs input filename"
        print "USAGE: %s %s <filename>" % (sys.executable, sys.argv[0])
        sys.exit(1)
    
    arg_fname = sys.argv[1]
    fdata = open(arg_fname, 'r').read()
    fdata_test1 = """aaaaa-bbb-z-y-x-123[abxyz]
    a-b-c-d-e-f-g-h-987[abcde]
    not-a-real-room-404[oarel]
    totally-real-room-200[decoy]"""
    fdata_test2 = """qzmt-zixmtkozy-ivhz-343"""
    #print decrypt('qzmt-zixmtkozy-ivhz', 343)
    solve_part2(fdata)


def is_real(name, checksum):
    name = name.replace("-", "")
    counter = collections.Counter(name)
    most_common = counter.most_common()
    def sorter(x, y):
        # Check count
        if y[1] > x[1]:
            return -1
        elif x[1] > y[1]:
            return 123
        # must be equal, check alphabetization
        if y[0] > x[0]:
            return 1
        elif x[0] > y[0]:
            return -1
            
    calc_checksum_pt1 = sorted(most_common, sorter,reverse=True)
    #print calc_checksum_pt1
    calc_checksum = ""
    for i in calc_checksum_pt1:
        calc_checksum = calc_checksum + i[0]
    valid = calc_checksum[:len(checksum)] == checksum
    #print valid, calc_checksum, checksum
    return valid
    

def solve_part1(fdata):

    sum_sector_ids = 0

    lines = fdata.split('\n')
    for line in lines:
        line = line.strip()
        
        name, x = line.rsplit('-', 1)
        sector_id, checksum = x.split('[')
        checksum = checksum[:-1]
        print name, sector_id, checksum
        if is_real(name, checksum):
            sum_sector_ids += int(sector_id)
    print sum_sector_ids

def decrypt(name, sectorid):
    decrypted = ""
    for char in name:
        if char == '-':
            decrypted = decrypted + " "
        else:
            decrypted = decrypted + chr((ord(char) + sectorid - ord('a')) % 26 + ord('a'))
    return decrypted

def solve_part2(fdata):

    lines = fdata.split('\n')
    for line in lines:
        line = line.strip()
        
        name, x = line.rsplit('-', 1)
        sector_id, checksum = x.split('[')
        sector_id = int(sector_id)
        checksum = checksum[:-1]
        #print name, sector_id, checksum
        if is_real(name, checksum):
            decrypted = decrypt(name, sector_id)
            if 'north' in decrypted.lower():
                print decrypted, sector_id


main()