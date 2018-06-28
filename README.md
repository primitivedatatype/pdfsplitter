# pdf splitter
Separate a multi-page pdf into 1-page pdfs.

Combine several pdf files into one pdf.

Written in Python 2.7.

## Run with:
`python view.py`

## Install Dependencies:
`pip install PyPDF2`

## Needed to make the executable:
`pip install pyinstaller` 

## Future Plans:
* Add a button on the listbox dialog to allow user to select additional files to combine. 
* Create a visual cue to remind the user whether in combine or split mode.
* Have a default filename/path shown in the dialog box in case the user forgets to write it in the 'save as' box.
* The executable in the dist folder bugs out on the combine function, even though it works when running with `python view.py`.
