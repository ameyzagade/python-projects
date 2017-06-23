# backup utility version 6
# while executing provide atleast one directory to backup

import zipfile
import os
import time
import argparse
import getpass


def getdir():
	# parser object to get arguments from terminal
	parser = argparse.ArgumentParser(''' Backup Utility version 6. Add directories to be zipped and for backup. ''')

	# one optional argument to backup
	parser.add_argument('-d', nargs="*", help="name of directories to be zipped.")

	args = parser.parse_args()	

	# check for user passes atleast one directory as an argument
	if (args.d is not None) and (len(args.d) >=1):
		makezip(args.d)
	else:
		print('Enter atleast one directory.')

# building a zip to store source directories
def makezip(dir_list):
	# default target directory will always be at /home/username for the current user
	target_dir = '/home/' + getpass.getuser() + os.sep + 'Backup' + time.strftime('_%Y-%m-%d_%H:%M:%S')
	print('Default Target Directory is', target_dir)

	# option to change target directory
	decide = input('Do you wish to change default target directory? [y/n]')
	if (decide == 'y') or (decide == 'Y'):
		new_loc = input('Enter new target directory location:')
		target_dir = new_loc + os.sep + 'Backup' + time.strftime('_%Y-%m-%d_%H:%M:%S')
		print('New Target Directory is', target_dir)
	elif (decide == 'n') or (decide == 'N'):
		pass
	else:
		print('improper choice. Default target directory will be used.')


	if not os.path.exists(target_dir):
		os.mkdir(target_dir)


	zip_name = 'backup.zip'

	target_fullpath = target_dir + os.sep + zip_name

	MyZipFile = zipfile.ZipFile(target_fullpath, 'w')

	# walk through the directory and subdirectories as well for all source directories
	for source in dir_list:
		parent_path = os.path.dirname(source)
		for root, dirs, files in os.walk(source):
			for dir_iterator in dirs:
				absolute_path = root + os.sep + dir_iterator
				relative_path = absolute_path.replace((parent_path) + '/', '')
				MyZipFile.write(absolute_path, relative_path, zipfile.ZIP_DEFLATED)
	
			for filename in files:
				absolute_path = root + os.sep + filename
				relative_path = absolute_path.replace((parent_path) + '/', '')
				MyZipFile.write(absolute_path, relative_path, zipfile.ZIP_DEFLATED)

	MyZipFile.close()

def main():
	getdir()

if __name__ == "__main__":
	main()