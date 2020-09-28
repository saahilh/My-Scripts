import sys, re
from mylib import checkFileOperationOutputMatch
'''
    Operating under the assumption that even if ID numbers are different in the two files.
    If the total number of times each ID occurs is the same, then the two files are likely
    the same, just with different ID numbers
'''
def getTotalNumberOfIdOccurrences(s1, s2):
    s1 = "".join(s1)
    s2 = "".join(s2)

    s1 = re.sub('[^0-9]+', ' ', s1)
    s2 = re.sub('[^0-9]+', ' ', s2)

    s1 = s1.split()
    s2 = s2.split()

    sum1 = 0
    for number in s1:
        sum1 += s1.count(number)

    sum2 = 0
    for number in s2:
        sum2 += s2.count(number)
    
    return sum1==sum2

checkFileOperationOutputMatch(getTotalNumberOfIdOccurrences)
