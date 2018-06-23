import Tkinter
LIST_BOX_WIDTH = 800
LIST_BOX_HEIGHT = 30
MAX_LISTBOX_HEIGHT=500
#credit: https://stackoverflow.com/questions/14459993/tkinter-listbox-drag-and-drop-with-python
class DragDropListbox(Tkinter.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries. """
    def __init__(self, master, **kw):
        kw['selectmode'] = Tkinter.SINGLE
        # kw['width'] = LIST_BOX_WIDTH
        # kw['height'] = LIST_BOX_HEIGHT
        # master.geometry('{}x{}'.format(LIST_BOX_WIDTH, LIST_BOX_HEIGHT))
        self.master = master
        Tkinter.Listbox.__init__(self, master, kw)#LIST_BOX_WIDTH, LIST_BOX_HEIGHT)#, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None

    def setSize(self, w, h):
        self.master.geometry('{}x{}'.format(w, h))

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i