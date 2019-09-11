import sys
from my_lib import remove_whitespace

'''
    This script looks through the input file to find all 
    duplicate lines. It keeps track of the duplicates
    found and prints out the line and its number of 
    occurences.
'''

def find_duplicate_lines(lines):
    line_count = {}

    for line_num in xrange(len(lines)):
        lines[line_num] = remove_whitespace(lines[line_num])

    for line in lines:
        if line and line in lines[1:]:
            if not line in line_count.keys():
                line_count[line] = 2
            else:
                line_count[line] += 1

        lines = lines[1:]

    return line_count

def find_duplicate_lines_and_print(text_to_examine):
    file_lines = text_to_examine.split('\n')
    duplicate_lines = find_duplicate_lines(file_lines)

    if not duplicate_lines:
        print "No duplicate lines found."
    else:
        for duplicate_line in duplicate_lines.keys():
            number_of_occurrences = duplicate_lines[duplicate_line]
            print str(number_of_occurrences) + " " + duplicate_line

text = "".join(sys.stdin.readlines())
find_duplicate_lines_and_print(text)