from tkinter import *

class directoryExplorer_navbar_header:

    def __init__(self, root, function_goto):
        #Variables
        self.gotoTable = function_goto
        self.root = root
        self.path = StringVar()
        self.filter = StringVar()

        # Widgets
        path_label = Label(self.root,text="Path")
        path_entry = Entry(self.root, textvariable=self.path)

        filter_label = Label(self.root,text="Filter")
        filter_entry = Entry(self.root, textvariable=self.filter)

        goto_button = Button(self.root, text="Go To", command= lambda: self.gotoTable(self.path.get(), self.filter.get()))

        # Render
        path_label.grid(row=0, column=0)
        path_entry.grid(row=0, column=1, ipadx=300)

        filter_label.grid(row=1, column=0)
        filter_entry.grid(row=1, column=1, ipadx=300)

        goto_button.grid(row=0, column=2, rowspan=2)