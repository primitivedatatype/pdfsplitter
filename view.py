import Tkinter, tkFileDialog
import tkMessageBox

import os, sys
import splitpdf

FILESIZE_THRESHOLD = 5000000
WIDTH_PIXELS = 200
HEIGHT_PIXELS = 100
# Credit: https://code.activestate.com/recipes/438123-file-tkinter-dialogs/
def get_users_file():
    '''
        Copies user specified file to tmp file
        Returns original file name
    '''
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        print ("file: ", file.name)
        data = file.read()
        file.close()
        size = len(data)
        print ("I got {} bytes from {}".format(size, os.path.basename(file.name)))
        # copy it over, so that the original file isn't tampered with.
        with open(splitpdf.TMP_PATH, 'wb') as f:
            f.write(data)
            return file.name, size
    else:
        return None, None

def remove_tmp_file(ask=False):
    '''
        Cleans up tmp file. 
        First verifies action through cmdline if ask==True.
    '''
    if os.path.exists(splitpdf.TMP_PATH):
        if ask == True:
            answer = raw_input("Remove temp file {} (y/n)?".format(TMP_PATH))
            if answer.lower() == 'y' or answer.lower() == 'yes': 
                os.remove(splitpdf.TMP_PATH)
            else:
                print ("ok, we won't remove it.")
        elif ask == False:
            os.remove(splitpdf.TMP_PATH)

def ask_remove_tmp_file(msg=None):
    title = "\"Wait! Don't go!\""
    question = "Remove temp file {}?".format(TMP_PATH)
    if msg != None:
        question += "\n"+msg
    ans = tkMessageBox.askyesno(title, question, parent=root)
    root.destroy()
    if ans: #user replied 'yes'
        remove_tmp_file()

def start_split():
    '''
        Begin Splitting Functionality
    '''
    original_name, size = get_users_file()
    if original_name != None and size != None:
        splitpdf.split(name=original_name)
        if size > FILESIZE_THRESHOLD:
            ask_remove_tmp_file(msg="Size: {} bytes".format(size))
    else:
        print ("no file selected...")

def get_users_files():
    '''
        Collects file_paths from user
        At some point, there was a bug that shows on windows machines that 
         is worth keeping track of:
        https://stackoverflow.com/questions/
            4116249/parsing-the-results-of-askopenfilenames 
        ...will need to test this on windows
    '''
    file_paths = tkFileDialog.askopenfilenames()
    return file_paths

def start_combine():
    '''
        Collects multiple filenames from user through dialog box
        Calls combine function
    '''
    file_paths = get_users_files()
    if len(file_paths) > 0:
        splitpdf.combine_files(file_paths, name="combined.pdf")
        print ("done!!")
    else:
        print ("no files were selected...")

def choose_option(title, texts, functions):
    '''
        Displays buttons with text from texts list
        Calls corresponding function from functions list upon button click
    '''
    num_options = len(texts)
    for i in range(num_options):
        b = Tkinter.Button(root, text=texts[i], command=functions[i])
        
        if num_options > 2:
            rely=(i * HEIGHT_PIXELS/float(len(texts)))/HEIGHT_PIXELS
        else:
            rely=(i+1)*0.25
        b.place(relx=0.2, rely=rely) 

if __name__ == "__main__":
    title="PDF Organizer"
    texts = ["Split Pdfs", "Combine Pdfs"]
    funcs = [start_split, start_combine]
    assert len(texts) == len(funcs)

    root = Tkinter.Tk()
    root.geometry('{}x{}'.format(WIDTH_PIXELS, HEIGHT_PIXELS))
    root.title(title)
    choose_option(title, texts, funcs)
    root.mainloop()
