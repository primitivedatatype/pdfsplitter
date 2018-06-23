# pdfsplitter
## Separates a multi-page pdf into 1-page pdfs in a folder labeled `pages`
## Combines several pdf files into one labeled `combined.pdf`

## Run with either of:
`python view.py`

## Just split pdfs and avoid the GUI:
`python splitpdf.py <file.pdf>`

`python splitpdf.py`

## Install Dependencies
`pip install PyPDF2`

## Notes:
`Combining files needs to be tested on Windows. See link:`
[Stackoverflow post on Tkinter askopenfiles bug](https://stackoverflow.com/questions/4116249/parsing-the-results-of-askopenfilenames)

## Future Plans:
* Verify the order of files before combining
* Place combined/split file(s) into same directory
	ask original file(s)
* Let user specify the name of the combined file

