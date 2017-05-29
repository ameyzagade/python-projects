#compression and backup utility version 2

import zipfile
import os, time

#source directory path
#enter your target directory path in between the single quotes
source_dir = ''

#target directory path
#enter your target directory path in between the single quotes
target_dir = ''

#check if target directory exists
if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	print("Target directory isn't available.")
	print("Creating target directory...")
	print('Target directory successfully created!', target_dir)


#target path that is., subdirectory in the target directory
#it will be named according to current date in YYYYMMDD format
target_path = target_dir + os.sep + time.strftime('%Y%m%d')

#check if subdirectory exists, if not create one
if not os.path.exists(target_path):
	os.mkdir(target_path)

#user comments, if any
comment = input('Enter your comment >>')

#name of the zip file
if(len(comment) == 0):
	zip_name = time.strftime('%H%M%S') + '.zip'
else:
	zip_name = time.strftime('%H%M%S') + '_' + comment.replace(' ', '_') + '.zip'

#absolute path of to be created target zip file
target_filepath = target_path + os.sep + zip_name


#creating a zipfile object variable
print('Creating zip file...')
MyZipFile = zipfile.ZipFile( target_filepath, 'w')


#adding files to the created zip
#walk through the directory
#this version deals with the files in subdirectory as well
for root, dirs, filenames in os.walk(source_dir):
		for filename in filenames:
			fpath = root + os.sep + filename
			MyZipFile.write(fpath, os.path.basename(fpath), zipfile.ZIP_DEFLATED)

#close the zipfile object
MyZipFile.close()

print('ZIP file created successfully at', target_path)
