import sys
from my_lib import remove_newlines

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

def get_num_different_lines(path_to_first_file, path_to_second_file):
    first_file = open(path_to_first_file, 'r')
    second_file = open(path_to_second_file, 'r')
    
    num_different_lines = 0

    first_file_lines = first_file.readlines()
    second_file_lines = second_file.readlines()

    for i in xrange(min(len(first_file_lines), len(second_file_lines))):
        if (first_file_lines[i] != second_file_lines[i]) :
            num_different_lines += 1

    first_file.close()
    second_file.close()

    return num_different_lines + abs(len(first_file_lines) - len(second_file_lines))

def check_if_files_have_same_content_and_print(arguments):
    # If called using console argument
    if(len(arguments)>1):
        path_to_first_file = sys.argv[1]
        path_to_second_file = sys.argv[2]
        print 'Number of different lines: ' + str(get_num_different_lines(path_to_first_file, path_to_second_file))

    # If called using a file
    else:
        file_data = sys.stdin.readlines()
        path_to_first_directory = remove_newlines(file_data[0])
        path_to_second_directory = remove_newlines(file_data[1])
        file_names = file_data[2:]

        failed_tests = []

        for file_name in file_names:
            file_name = remove_newlines(file_name)
            path_to_first_file = path_to_first_directory + file_name
            path_to_second_file = path_to_second_directory + file_name

            num_different_lines = get_num_different_lines(path_to_first_file, path_to_second_file)
            if (num_different_lines != 0):
                failed_tests.append(file_name + ' ' + str(num_different_lines))

        if not failed_tests:
            print "All checks passed"
        else:
            print "Failed checks for: \n\n" + "\n".join(failed_tests)

check_if_files_have_same_content_and_print(sys.argv)
