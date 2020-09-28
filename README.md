Current files:
* check_if_files_have_same_content.py
	* Description:
		* This can be useful to verify that changes haven't impacted the output of files produced. It can also be useful to reduce the set of files that need analysis if changes did occur.
	* Methods:
		* files_have_same_content(path_to_first_file, path_to_second_file)
		* check_if_files_have_same_content_and_print(arguments)
* search_for_duplicate_lines.py
	* Description:
		* This is useful if you're analyzing the code of a serial copy-paster. It helps you find sections of code where repetition occurs so that you can refactor it into methods.
	* Methods:
		* find_duplicate_lines(lines)
		* find_duplicate_lines_and_print(text_to_examine)
* my_lib.py
	* Description:
		* Contains utilities called by the other scripts in this repository
	* Methods:
		* remove_whitespace(string)
		* remove_newlines(string)
