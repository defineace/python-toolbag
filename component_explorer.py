from tkinter import *
from fragment_explorer_table import *

class tab_explorer:
    def __init__(self, root):
        # Variables
        self.root = root
        self.frameList = []

        self.path = StringVar()
        self.filter = StringVar()

        self.search = StringVar()
        self.replace = StringVar()

        self.path.set("C:/Users/lrdef/Desktop/Projects/Coding/Python/python-practice")
        self.filter.set("")

        self.search.set("utility_")
        self.replace.set("utility_category_")

        # Render Frames
        self.frameExplorerHeader()
        self.frameSearchReplace()

    def frameExplorerHeader(self):
        # Widget Root
        frame_header = Frame(self.root, borderwidth=10)
        frame_header.pack()

        # Widgets
        path_label = Label(frame_header,text="Path")
        path_entry = Entry(frame_header, textvariable=self.path)

        filter_label = Label(frame_header,text="Filter")
        filter_entry = Entry(frame_header, textvariable=self.filter)

        search_button = Button(frame_header, text="Go To", command=self.createTable)
        
        
        # Render
        path_label.grid(row=0, column=0)
        path_entry.grid(row=0, column=1, ipadx=300)
    
        filter_label.grid(row=1, column=0)
        filter_entry.grid(row=1, column=1, ipadx=300)

        search_button.grid(row=0, column=2, rowspan=2)

    def frameSearchReplace(self):
        # Widget Root
        frame_SearchReplace = Frame(self.root, borderwidth=10)
        frame_SearchReplace.pack()
        # Widgets
        search_label = Label(frame_SearchReplace, text="Search")
        search_entry = Entry(frame_SearchReplace, textvariable=self.search)

        replace_label = Label(frame_SearchReplace, text="Replace")
        replace_entry = Entry(frame_SearchReplace, textvariable=self.replace)
        # Render
        search_label.grid(row=0, column=0)
        search_entry.grid(row=0, column=1, ipadx=200)

        replace_label.grid(row=1, column=0)
        replace_entry.grid(row=1, column=1, ipadx=200)

    def createTable(self):
            for frame in self.frameList:
                frame.destroy()

            table = Frame(self.root, borderwidth=.5, relief="solid")
            self.frameList.append(table)
            table.pack(padx=10, pady=10)

            fragment_table(table, self.path, self.filter, self.search, self.replace)