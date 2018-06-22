import Tkinter, tkFileDialog
import os, sys
import splitpdf

TMP_PATH = 'tmp.pdf'

# Credit: https://code.activestate.com/recipes/438123-file-tkinter-dialogs/
def get_users_file():
	'''
		Copies user specified file to tmp file
		Returns original file name
	'''
	root = Tkinter.Tk()
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
	print "file: ", file.name
	if file != None:
	    data = file.read()
	    file.close()

	    print ("I got {} bytes from {}".format(len(data), os.path.basename(file.name)))
	    # copy it over, so that the original file isn't tampered with.
	    with open(TMP_PATH, 'wb') as f:
	    	f.write(data)
	return file.name



if __name__ == "__main__":
	original_name = get_users_file()

	splitpdf.split(TMP_PATH, name=original_name)