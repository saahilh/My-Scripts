import sys
from mylib import removeNewlines

'''
    This script checks if two files of the same name but in different directories
    have the same text. It can be called with arguments either directly passed in
    from the console or passed in from a file. 
    
    If passed in from the console, the call should be: 
        python checkIfFilesHaveSameContent.py path1 path2

    If a file is passed in, it should be structured as such: 

        pathToDirectory1
        pathToDirectory2
        filename1
        filename2
        ...

    This call can then be made by passing the file as an input to the script:
        python checkIfFilesHaveSameContent.py < myTestCases.someExtension
    
    Note that in the file method, I have assumed that filenames are the same in both directories.
'''

def filesHaveSameContent(path1, path2):
    path1 = removeNewlines(path1)
    path2 = removeNewlines(path2)

    file1 = open(path1, 'r')
    file2 = open(path2, 'r')
    
    filesAreIdentical = False

    if(file1.readlines()==file2.readlines()):
        filesAreIdentical = True

    file1.close()
    file2.close()
    return filesAreIdentical

failed = []

# If called using console argument
if(len(sys.argv)>1):
    path1 = sys.argv[1]
    path2 = sys.argv[2]

    if(filesHaveSameContent(path1, path2)):
        print "True"
    else:
        print "False"
# If called using a file
else:
    comparisonInput = sys.stdin.readlines()
    path1 = comparisonInput[0]
    path2 = comparisonInput[1]
    filenames = comparisonInput[2:]

    for filename in filenames:
        filesAreIdentical = filesHaveSameContent(path1 + filename, path2 + filename)
        if not filesAreIdentical:
            failed.append(filename)

    if len(failed) is 0:
        print "All tests passed"
    else:
        print "Failed tests for: " + str(failed)
