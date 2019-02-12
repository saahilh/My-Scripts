import sys
from mylib import removeWhitespace

'''
    This script looks through the input file to find all 
    duplicate lines. It keeps track of the duplicates
    found and prints out the line and its number of 
    occurences.
'''

code = sys.stdin.readlines()
code = "".join(code)
code = "".join(code.split('\t'))
code = code.split('\n')

for line in code:
      line = removeWhitespace(line)

lines = {}
for lineNum in range(0, len(code)-1):
    line = code[lineNum]
    if line!="" and line in code[lineNum + 1:-1]:
        if not line in lines.keys():
            lines[line] = 2
        else:
            lines[line] += 1

for key in lines.keys():
    print str(lines[key]) + " " + key
