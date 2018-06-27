import Tkinter, tkFileDialog
import tkMessageBox
from functools import partial
import os, sys
import splitpdf
# from DragDropListBox import * 
import DragDropListBox as dbox
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
            answer = raw_input("Remove temp file {} (y/n)?".format(splitpdf.TMP_PATH))
            if answer.lower() == 'y' or answer.lower() == 'yes': 
                os.remove(splitpdf.TMP_PATH)
            else:
                print ("ok, we won't remove it.")
        elif ask == False:
            os.remove(splitpdf.TMP_PATH)

def ask_remove_tmp_file(msg=None):
    title = "\"Wait! Don't go!\""
    question = "Remove temp file {}?".format(splitpdf.TMP_PATH)
    if msg != None:
        question += "\n"+msg
    ans = tkMessageBox.askyesno(title, question, parent=root)
    root.destroy()
    if ans: #user replied 'yes'
        remove_tmp_file()

def get_save_as_directory(original_path):
    '''
        Prompt user to choose where to save split pdf files
    '''
    dir_name = tkFileDialog.askdirectory()
    if dir_name == None:
        dir_name = os.path.dirname(original_path)

    print ("Will save into {}".format(dir_name))
    return dir_name

def start_split():
    '''
        Begin Splitting Functionality
    '''
    original_path, size = get_users_file()
    if original_path != None and size != None:
        save_as_dir = get_save_as_directory(original_path)
        splitpdf.split(name=original_path, dir_name=save_as_dir)

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

def get_save_as_name(): #initial_dir):
    '''
        Prompt user to choose where to save the combined pdf file
    '''
    file_name = tkFileDialog.asksaveasfilename()
    if file_name != None:
        return file_name
        
    else:
        file_name = "combined.pdf"
        print ("will save as default: {}".format(file_name))
        return file_name

def combine_ordered_files(root, listbox, num_files):
    # extract the order specified by user
    ordered_paths=[]
    for i in range(num_files):
        ordered_paths.append(listbox.get(0))
        listbox.delete(0)

    print ("\norder")
    for p in ordered_paths:
        print p

    name = get_save_as_name()#os.path.dirname(ordered_paths[0]))
    splitpdf.combine_files(ordered_paths, name=name)

    listbox.destroy()
    root.destroy()
    print ("done!!")

def start_combine():
    '''
        Collects multiple filenames from user through dialog box
        Calls combine function
    '''
    file_paths = get_users_files()
    num_files = len(file_paths)
    if num_files > 0:
        # add items to list box
        listbox = dbox.DragDropListbox(root)
        for i, path in enumerate(file_paths):
            listbox.insert(Tkinter.END, path)
            listbox.selection_set(i)

        listbox.pack(fill=Tkinter.BOTH, expand=True)
        height = min(dbox.LIST_BOX_HEIGHT + 20*num_files, \
            dbox.MAX_LISTBOX_HEIGHT)
        listbox.setSize(dbox.LIST_BOX_WIDTH, height)

        combine_based_on_listbox = partial(\
            combine_ordered_files, root, listbox, num_files)
        b = Tkinter.Button(root, text="Go", command=combine_based_on_listbox)
        b.place(relx=0.85, rely=0.2) 

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
