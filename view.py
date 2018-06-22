import Tkinter, tkFileDialog
import tkMessageBox

import os, sys
import splitpdf

TMP_PATH = 'tmp.pdf'
FILESIZE_THRESHOLD = 5000000
root = Tkinter.Tk()

# Credit: https://code.activestate.com/recipes/438123-file-tkinter-dialogs/
def get_users_file():
	'''
		Copies user specified file to tmp file
		Returns original file name
	'''
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
	print "file: ", file.name
	if file != None:
	    data = file.read()
	    file.close()

	    size = len(data)
	    print ("I got {} bytes from {}".format(size, os.path.basename(file.name)))
	    # copy it over, so that the original file isn't tampered with.
	    with open(TMP_PATH, 'wb') as f:
	    	f.write(data)
	return file.name, size

def remove_tmp_file(ask=False):
	'''
		Cleans up tmp file
	'''
	if os.path.exists(TMP_PATH):
		if ask == True:
			answer = raw_input("Remove temp file {} (y/n)?".format(TMP_PATH))
			if answer.lower() == 'y' or answer.lower() == 'yes': 
				os.remove(TMP_PATH)
			else:
				print ("ok, we won't remove it.")
		elif ask == False:
			os.remove(TMP_PATH)

# def ask_question(title, question):
	# tkMessageBox.showinfo(title, question)
	# button_yes = Tkinter.Button(root, text="Yes", command=remove_tmp_file)
	# button_no = Tkinter.Button(root, text="No", command=exit)
	# button_yes.pack()
	# button_no.pack()

def ask_remove_tmp_file(msg=None):
	title = "\"Wait! Don't go!\""
	question = "Remove temp file {}?".format(TMP_PATH)
	if msg != None:
		question += "\n"+msg
	ans = tkMessageBox.askyesno(title, question, parent=root)
	root.destroy()
	if ans:
		remove_tmp_file()

if __name__ == "__main__":
	original_name, size = get_users_file()
	splitpdf.split(TMP_PATH, name=original_name)

	if size > FILESIZE_THRESHOLD:
		ask_remove_tmp_file(msg="Size: {} bytes".format(size))