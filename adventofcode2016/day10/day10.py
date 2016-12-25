"""
--- Day 10: Balance Bots ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, bots take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the bots must use some logic to decide what to do with each chip. You access the local control computer and download the bots' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.
In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

Your puzzle answer was 101.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?


"""
import collections
import re

VALUE_CMD = 0
BOT_CMD = 1


def parse_line(line):
    instr = {}
    
    if line.startswith('value'):
        instr['command'] = VALUE_CMD
    elif line.startswith('bot'):
        instr['command'] = BOT_CMD
    else:
        raise Exception("Invalid line!")
    
    if instr['command'] == VALUE_CMD:
        regex = 'value (\d+) goes to bot (\d+)'
        m = re.search(regex, line)
        instr['value'] = int(m.group(1))
        instr['bot'] = int(m.group(2))
        
    elif instr['command'] == BOT_CMD:
        regex = 'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'
        m = re.search(regex, line)
        instr['bot'] = int(m.group(1))
        instr['low_dest_type'] = m.group(2)
        instr['low_dest_num'] = int(m.group(3))
        instr['high_dest_type'] = m.group(4)
        instr['high_dest_num'] = int(m.group(5))
        
    return instr
        
class Bot():
    def __init__(self):
        self.low_dest_type = None
        self.low_dest_num = None
        self.high_dest_type = None
        self.high_dest_num = None
        self.values_held = []
        self.comparisons_made = []
    
    def __str__(self):
        out = ""
        out += "Low to %s %d\n" % (self.low_dest_type, self.low_dest_num)
        out += "High to %s %d\n" % (self.high_dest_type, self.high_dest_num)
        out += "Holding %s \n" % self.values_held
        out += "Comparsisons %s\n " % self.comparisons_made
        return out

def test_phase1():
    data = """\
    value 5 goes to bot 2
    bot 2 gives low to bot 1 and high to bot 0
    value 3 goes to bot 1
    bot 1 gives low to output 1 and high to bot 0
    bot 0 gives low to output 2 and high to output 0
    value 2 goes to bot 2"""
    instrs = []
    for line in data.split('\n'):
        line = line.strip()
        instr = parse_line(line)
        instrs.append(instr)
        
    process_instrs(instrs)
        
def process_instrs(instrs):

    bots = collections.defaultdict(Bot)
    for instr in instrs:
        if instr['command'] == VALUE_CMD:
            bot_num = instr['bot']
            bots[bot_num].values_held.append(instr['value'])
        elif instr['command'] == BOT_CMD:
            bot_num = instr['bot']
            bots[bot_num].low_dest_type = instr['low_dest_type']
            bots[bot_num].low_dest_num = instr['low_dest_num']
            bots[bot_num].high_dest_type = instr['high_dest_type']
            bots[bot_num].high_dest_num = instr['high_dest_num']
    
    # Print initial state
    print "Initial"
    for bot_num in sorted(bots):
        print bot_num, bots[bot_num].values_held
    
    print "Processing"
    # Now run until steady-state
    
    outputs = collections.defaultdict(list)
    
    keep_going = True
    while keep_going:
        keep_going = False
        for bot_num in sorted(bots):
            bot = bots[bot_num]
            if bot.values_held:
                #print "bot #%d has values %s" % (bot_num, bot.values_held)
                if len(bot.values_held) == 2:
                    keep_going = True
                    low, high = sorted(bot.values_held)
                    bot.comparisons_made.append((low, high))
                    bot.values_held = []
                    if bot.low_dest_type == 'bot':
                        bots[bot.low_dest_num].values_held.append(low)
                        #print "Printing ", bot_num
                        #print bot
                        print "%d gave %d to %d. %d now holds:%s" % (bot_num, low, bot.low_dest_num, bot.low_dest_num, bots[bot.low_dest_num].values_held)
                    elif bot.low_dest_type == 'output':
                        outputs[bot.low_dest_num].append(low)
                        
                    if bot.high_dest_type == 'bot':
                        bots[bot.high_dest_num].values_held.append(high)
                        #print "Printing ", bot_num
                        #print bot
                        print "%d gave %d to %d. %d now holds:%s" % (bot_num, high, bot.high_dest_num, bot.high_dest_num, bots[bot.high_dest_num].values_held)
                    elif bot.high_dest_type == 'output':
                        outputs[bot.high_dest_num].append(high)
    print "Comparisons"
    for bot_num in sorted(bots):
        print bot_num, bots[bot_num].comparisons_made   
    
    print "Solution"
    for bot_num in sorted(bots):
        if (17,61) in bots[bot_num].comparisons_made:
            print bot_num
            
    for output in sorted(outputs):
        print output, outputs[output]
    
    print outputs[0][0]*outputs[1][0]*outputs[2][0]

def phase1():
    data = open('input.txt','r').read()
    instrs = []
    for line in data.split('\n'):
        line = line.strip()
        instr = parse_line(line)
        instrs.append(instr)
        
    process_instrs(instrs)

    
def test_phase2():
    pass
        
def phase2():
    pass
    
def main():
    #test_phase1()
    phase1()
    #test_phase2()
    #phase2()
    

if __name__ == "__main__":
    main()
