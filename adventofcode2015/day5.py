import sys

DEBUG = True
def print_dbg(msg):
    if DEBUG:
        print msg
    
def is_nice(line):
    # vowels:
    vowel_count = 0
    for vowel in 'aeiou':
        vowel_count += line.count(vowel)
    if vowel_count < 3:
        print_dbg("Vowel count failed")
        return False
        
    # Repeated char
    for i in xrange(len(line) - 1):
        if line[i] == line[i+1]:
            break
    else:
        print_dbg("Repeat failed")
        return False
        
    # Bad strings
    badstrings = ('ab', 'cd', 'pq', 'xy')
    for badstring in badstrings:
        if badstring in line:
            print_dbg("Badstring failed")
            return False
            
    # All good!
    return True

def is_nice2(line):        
    # Repeated char
    for i in xrange(len(line) - 3):
        if line[i:i+2] in line[i+2:]:
            break
    else:
        print_dbg("Repeat (double) failed")
        return False
        
    # Repeated char
    for i in xrange(len(line) - 2):
        if line[i] == line[i+2]:
            break
    else:
        print_dbg("Repeat (between) failed")
        return False
            
    # All good!
    return True    
    
def main():
    nice_strings = 0
    
    with open(sys.argv[1]) as fh:
        data = fh.read().split('\n')
    
    for line in data:
        if is_nice2(line):
            nice_strings += 1
    print nice_strings

if __name__ == "__main__":
    if sys.argv < 2:
        print "USAGE: python day5.py file.dat"
        sys.exit(1)
    main()