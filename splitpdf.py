from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import sys
TMP_PATH = 'tmp.pdf'
# Much of this code originated from an answer provided at:
# https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
def split(file_path=None, dir_name=None, name=None):
	if file_path == None:
		file_path = TMP_PATH
	if name == None:
		base_name = os.path.basename(file_path).split('.pdf')[0]
	else:
		base_name = os.path.basename(name).split('.pdf')[0]
	if dir_name==None:
		cur_dir = os.getcwd()
		dir_name = os.path.join(cur_dir, 'pages')

	if not os.path.exists(dir_name):
		os.makedirs(dir_name)


	print ("base: {}".format(base_name))
	inputpdf = PdfFileReader(open(file_path, "rb"))
	names = []
	
	for i in range(inputpdf.numPages):
	    output = PdfFileWriter()
	    output.addPage(inputpdf.getPage(i))
	    name = os.path.join(dir_name, "{}_p{}.pdf".format(base_name, i+1))
	    names.append(name)
	    with open(name, "wb") as outputStream:
	        output.write(outputStream)
	    print ("\tCreating {}".format(name))

	print ("All done!")
	return dir_name, names

def combine_files(file_paths, name=None):
	print ("combining: {}".format(file_paths))

	output = PdfFileWriter()
	for i in range(len(file_paths)):
		inputpdf = PdfFileReader(open(file_paths[i], 'rb'))
		for page_num in range(inputpdf.getNumPages()):
			output.addPage(inputpdf.getPage(page_num))
		if name == None:
			name = "combined.pdf"
		with open(name, 'wb') as outputStream:
			output.write(outputStream)
		print ("\tCombining {} into {}".format(\
			os.path.basename(file_paths[i]), name))