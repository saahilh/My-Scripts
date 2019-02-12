def checkIfIdenticalFileContent(path1, path2, filename):
    file1 = open(path1 + filename, 'r')
    file2 = open(path2 + filename, 'r')
    
    filesAreIdentical = False

    if(file1.readlines()==file2.readlines()):
        filesAreIdentical = True

    file1.close()
    file2.close()
    return filesAreIdentical

files = ['AndForkTestMergedBranches.jucm', 'andfork.jucm', 'andjoin.jucm', 'belief.jucm', 'connect.jucm', 'failurepoint.jucm', 'orjoin.jucm', 'resource.jucm', 'timer.jucm', 'waitingplace.jucm']
failed = []

for filename in files:
    filesAreIdentical = checkIfIdenticalFileContent('../eclipse-workspace/TURNtoURN/ATLProject/Output/', '../oracleOutputs/', filename)
    if not filesAreIdentical:
        failed.append(filename)

if len(failed) is 0:
    print "All tests passed"
else:
    print "Failed tests for: " + str(failed)
