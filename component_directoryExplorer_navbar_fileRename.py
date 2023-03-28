from tkinter import *

class directoryExplorer_navbar_fileRename:
    def __init__(self, root, buttonClicked_search, buttonClicked_replace):
        # Variables
        self.root = root
        self.buttonClicked_search = buttonClicked_search
        self.buttonClicked_replace = buttonClicked_replace

        self.search = StringVar()
        self.replace = StringVar()

        # Widgets
        self.title_label = Label(self.root, text="Rename Files")

        self.search_label = Label(self.root, text="Search")
        self.search_entry = Entry(self.root, textvariable=self.search)
        self.search_button = Button(self.root, text="Search", command= lambda: self.buttonClicked_search(self.search.get(), self.replace.get()))

        self.replace_label = Label(self.root, text="Rename")
        self.replace_entry = Entry(self.root, textvariable=self.replace)
        self.replace_button = Button(self.root, text="Replace", command= lambda: self.buttonClicked_replace(self.search.get(), self.replace.get()))

        # Render
        self.title_label.grid(row=0, columnspan=3)

        self.search_label.grid(row=1, column=0)
        self.search_entry.grid(row=1, column=1, ipadx=200)
        self.search_button.grid(row=1, column=3)

        self.replace_label.grid(row=2, column=0)
        self.replace_entry.grid(row=2, column=1, ipadx=200)
        self.replace_button.grid(row=2, column=3)