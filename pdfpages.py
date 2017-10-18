from PyPDF2 import PdfFileReader
import os

total_count = 0
document = 0
source = '/home/ameyzagade/Documents/NTAL'
for root, dirs, files in os.walk(source):
	print('In directory' + root)
	for filename in files:
		pathname = source + os.sep + filename
		pdf = PdfFileReader(open(str(pathname), 'rb'))
		count = pdf.getNumPages()
		total_count += count
		document += 1
		print(filename + ' , ' + 'Pages: ' + str(count) +'\n')

print('Total Count of ' + str(document) + ' is ' + str(total_count))
