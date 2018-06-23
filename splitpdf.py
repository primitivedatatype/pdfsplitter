from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import sys
TMP_PATH = 'tmp.pdf'
# Much of this code originated from an answer provided at:
# https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
def split(file_path=None, name=None):
	if file_path == None:
		file_path = TMP_PATH
	if name == None:
		base_name = os.path.basename(file_path).split('.pdf')[0]
	else:
		base_name = os.path.basename(name).split('.pdf')[0]

	print ("base: {}".format(base_name))
	inputpdf = PdfFileReader(open(file_path, "rb"))
	names = []
	cur_dir = os.getcwd()
	new_dir_name = os.path.join(cur_dir, 'pages')

	if not os.path.exists(new_dir_name):
		os.makedirs(new_dir_name)

	for i in range(inputpdf.numPages):
	    output = PdfFileWriter()
	    output.addPage(inputpdf.getPage(i))
	    name = os.path.join(new_dir_name, "{}_p{}.pdf".format(base_name, i+1))
	    names.append(name)
	    with open(name, "wb") as outputStream:
	        output.write(outputStream)
	    print ("\tCreating {}".format(name))

	print ("All done!")
	return new_dir_name, names

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

def main():
	argv = sys.argv[1:]
	if len(argv) == 0:
		file_path = raw_input("Enter path of pdf to split: ")
	else:
		file_path = argv[0]

	if not os.path.exists(file_path):
		print "File not found: {}".format(file_path)
		print "Run as\n\tpython splitpdf.py <file_to_pdf>"
		sys.exit(-1)

	split(file_path=file_path)

if __name__ == "__main__":
	main()
	