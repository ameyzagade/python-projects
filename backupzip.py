#compression and backup utility version 5
# while executing provide argument
#	-v, --verbose	verbose output
#	-q, --quiet	quiet output
# defaults to quiet output on no arguments


import zipfile
import os
import time
import argparse


#define zipfn function to build a zip
def zipfn(flag):
	#source directory path
	#enter your target directory path in between the single quotes
	source_dir = ''
	if flag == 1: 
		print('Source directory is at {0}'.format(source_dir))
	

	#target directory path
	#enter your target directory path in between the single quotes
	target_dir = ''


	#check if target directory exists
	if not os.path.exists(target_dir):
		os.mkdir(target_dir)
		if flag == 1: 
			print("Target directory isn't available.")
			print("Creating target directory...")
			print('Target directory successfully created!')
	if flag == 1:
		print('Target directory is at {0}'.format(target_dir))

	#target path i.e, subdirectory in the target directory
	#it will be named according to current date in YYYYMMDD format
	target_path = target_dir + os.sep + time.strftime('%Y%m%d')


	#check if subdirectory exists, if not create one
	if not os.path.exists(target_path):
		os.mkdir(target_path)
			

	#user comments, if any
	print('Add comments if, any, comments will be appended to name of the target file!')
	comment = input('Enter your comment >>>')

	#name of the zip file
	if(len(comment) == 0):
		zip_name = time.strftime('%H%M%S') + '.zip'
	else:
		zip_name = time.strftime('%H%M%S') + '_' + comment.replace(' ', '_') + '.zip'


	#absolute path of to be created target zip file
	target_filepath = target_path + os.sep + zip_name
	if flag == 1: 
		print('Compressed file will be saved at {}'.format(target_filepath))


	#creating a zipfile object variable
	if flag == 1: 
		print('Creating zip file...')
	MyZipFile = zipfile.ZipFile( target_filepath, 'w')


	#absolute path of the source directory
	parent_path = os.path.dirname(source_dir)


	#adding files to the created zip
	#walk through the directory and subdirectories as well
	for root, dirs, filenames in os.walk(source_dir):
		for dir_iterator in dirs:
			absolute_path = root + os.sep + dir_iterator
			relative_path = absolute_path.replace((parent_path) + '/', '')
			MyZipFile.write(absolute_path, relative_path, zipfile.ZIP_DEFLATED)

		for filename in filenames:
			absolute_path = root + os.sep + filename
			relative_path = absolute_path.replace((parent_path) + '/', '')
			MyZipFile.write(absolute_path, relative_path, zipfile.ZIP_DEFLATED)


	#close the zipfile object
	MyZipFile.close()
	
	#display the location where zip file is stored
	print('ZIP file created successfully at', target_path)


def main():
	#create a parser object reference using ArgumentParser object to get arguments from command line
	parser = argparse.ArgumentParser(description='''Compression and Backup Utility version 5.\
	Default is quiet output for given directory. Add directories by typing their entire path after\
	the arguments to the script.''')

	#positional arguments

	#optional arguments
	#parser.add_argument('-', "--blank", action='store_true', help="Default action, quiet output.")
	parser.add_argument('-v', "--verbose", action='store_true', help="Verbose Output.")
	parser.add_argument('-q', "--quiet", action='store_true', help="Quiet Output.")
	args=parser.parse_args()


	if args.verbose:
		zipfn(flag=1)
	elif args.quiet:
		zipfn(flag=0)
	else:
		print("Enter valid arguments")


if __name__ == "__main__":
	main()
