from __future__ import division
"""
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?

Your puzzle answer was 34925.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?

Although it hasn't changed, you can still get your puzzle input.
"""


def checksum_row1(row):
    # Solve the wrapping around
    nums = [int(i) for i in row.split() if i]
    checksum = max(nums) - min(nums)
    return checksum

def checksum_sheet1(sheet):
    rows = sheet.split("\n")
    checksum_total = 0
    for row in rows:
        checksum_total += checksum_row1(row)
    return checksum_total
    
def tests1():
    tests = [
        ["5 1 9 5", 8],
        ["7 5 3", 4],
        ["2 4 6 8", 6]
    ]
    success = True
    test_function = checksum_row1
    for input, output in tests:
        test_result = test_function(input)
        if test_result != output:
            print "TEST FAILED", input, test_result, output
            success = False
    return success
    
def checksum_row2(row):
    # Solve the wrapping around
    nums = [int(i) for i in row.split() if i]
    nums = sorted(nums, reverse=True)
    for i in range(len(nums)):
        for denom in nums[i+1:]:
            num = nums[i]
            if denom == 0:
                continue
            if num/denom == int(num/denom):
                return num/denom
    raise Exception("No checksum!")

def checksum_sheet2(sheet):
    rows = sheet.split("\n")
    checksum_total = 0
    for row in rows:
        checksum_total += checksum_row2(row)
    return checksum_total
    
def tests2():
    tests = [
        ["5 9 2 8", 4],
        ["9 4 7 3", 3],
        ["3 8 6 5", 2]
    ]
    success = True
    test_function = checksum_row2
    for input, output in tests:
        test_result = test_function(input)
        if test_result != output:
            print "TEST FAILED", input, test_result, output
            success = False
        else:
            print "TEST PASED", input, test_result
    return success
    
if __name__ == "__main__":
    tests1()
    data = open('infile.txt').read()
    print checksum_sheet1(data)
    
    tests2()
    data = open('infile.txt').read()
    print checksum_sheet2(data)