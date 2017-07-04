import argparse
import re

def get_arg():
	''' UNIX replace command. This will replace all instances of 'from' string with 'from to' string in the mentioned file(s).
	If the -- option is not given, replace reads the standard input and writes to the standard output.'''

	__version__ = '1.0'
	parser = argparse.ArgumentParser("replace.py (-v/-s) (from_string) (to_string) ... file_name (file_name) ... ")
	parser.add_argument('-s', action='store_true', help="Silent mode. Print less information about what the program does. Default action.")
	parser.add_argument('-v', action='store_true', help="Verbose mode. Print more information about what the program does.")
	parser.add_argument('--version', action='version', version='Version: {version}'.format(version=__version__), help="Display version information and exit.")
	parser.add_argument('original_string', nargs='?')
	parser.add_argument('replacement_string', nargs='?')
	parser.add_argument('files', nargs='*')
	args = parser.parse_args()

	is_silent = True
	if args.s:
		replace(is_silent, args.original_string, args.replacement_string, args.files)
	elif args.v:
		is_silent = False
		replace(is_silent, args.original_string, args.replacement_string, args.files)
	else:
		# default to silent output
		replace(is_silent, args.original_string, args.replacement_string, args.files)

def replace(is_silent, from_string, to_string, dirs):
	if (from_string is None) or (to_string is None):
		print('Orginal String or Replace String is absent.')
	elif (len(dirs) == 0):
		print(to_string)
	else:
		for filename in dirs:
			if not is_silent:
				print('Modifying file', filename)
			file_lines = list()
			# first open file for reading in the memory
			with open(filename, 'r') as file:
				file.seek(0)
				# look for word in the file line by line
				for line in file:
					line = re.sub(r'\b'+from_string+r'\b', to_string, line)
					file_lines.append(line)

			# next open the same file for writing modified lines
			with open(filename, 'w') as file:
				file.seek(0)
				for line in file_lines:
					file.write(line)
			if not is_silent:
				print('Done!')
					
def main():
	get_arg()	

if __name__ == "__main__":
	main()