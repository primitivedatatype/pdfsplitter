# pdf splitter
Separate a multi-page pdf into 1-page pdfs.

Combine several pdf files into one pdf.

## Run with:
`python view.py`

## Or split pdfs and avoid the GUI:
`python splitpdf.py <file.pdf>`

`python splitpdf.py`

## Install Dependencies
`pip install PyPDF2`

## Notes:
Combining files needs to be tested on Windows. See link:
[Stackoverflow post on Tkinter askopenfiles bug](https://stackoverflow.com/questions/4116249/parsing-the-results-of-askopenfilenames)

## Future Plans:
Currently messages that tell the user what is going on are only displayed in the commandline. It would be helpful to add these to the UI.
