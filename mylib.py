import sys

def removeWhitespace(string):
    return "".join(string.split())

def removeNewlines(string):
    return string.replace('\n','')

def getFileData(pathToFile):
    openedFile = open(pathToFile, 'r')
    data = openedFile.readlines()
    openedFile.close()
    return data


'''
    This method checks if two files of the same name but in different directories
    fulfill some condition. 
    
    This call can then be made by passing the file as an input to the script:
        python checkIfFilesHaveSameContent.py < myTestCases.someExtension
    
    If a file is passed in, it should be structured as such: 

        pathToDirectory1
        pathToDirectory2
        filename1
        filename2
        ...
'''

def checkFileOperationOutputMatch(operation):
    allFiles = []
    
    comparisonInput = sys.stdin.readlines()
    path1 = comparisonInput[0]
    path2 = comparisonInput[1]
    filenames = comparisonInput[2:]
    for filename in filenames:
        allFiles.append((removeNewlines(path1 + filename), removeNewlines(path2 + filename)))
    
    failed = []

    for pair in allFiles:
        filesAreIdentical = operation(getFileData(pair[0]),getFileData(pair[1]))
        if not getFileData(pair[0])==getFileData(pair[1]):
            failed.append(pair[0].split('/')[-1])

    if len(failed) is 0:
        print "All checks passed"
    else:
        print "Failed check for:\n" + '\n'.join(failed)
