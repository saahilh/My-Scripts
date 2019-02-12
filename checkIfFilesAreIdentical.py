import sys
from mylib import removeNewlines

'''
    This script checks if two files of the same name but in different directories
    have the same text. It takes as input any file structured such that its first line 
    is the path to the first directory, the second line the path to the second directory,
    and the remaining lines filenames to be tested.
'''

def checkIfIdenticalFileContent(path1, path2, filename):
    path1 = removeNewlines(path1)
    path2 = removeNewlines(path2)
    filename = removeNewlines(filename)

    file1 = open(path1 + filename, 'r')
    file2 = open(path2 + filename, 'r')
    
    filesAreIdentical = False

    if(file1.readlines()==file2.readlines()):
        filesAreIdentical = True

    file1.close()
    file2.close()
    return filesAreIdentical

comparisonInput = sys.stdin.readlines()
path1 = comparisonInput[0]
path2 = comparisonInput[1]
filenames = comparisonInput[2:]

failed = []

for filename in filenames:
    filesAreIdentical = checkIfIdenticalFileContent(path1, path2, filename)
    if not filesAreIdentical:
        failed.append(filename)

if len(failed) is 0:
    print "All tests passed"
else:
    print "Failed tests for: " + str(failed)
