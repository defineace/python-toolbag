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
        title_label = Label(self.root, text="Rename Files")

        search_label = Label(self.root, text="Search")
        search_entry = Entry(self.root, textvariable=self.search)
        search_button = Button(self.root, text="Search", command= lambda: self.buttonClicked_search(self.search.get(), self.replace.get()))

        replace_label = Label(self.root, text="Replace")
        replace_entry = Entry(self.root, textvariable=self.replace)
        replace_button = Button(self.root, text="Replace", command= lambda: self.buttonClicked_replace())

        # Render
        title_label.grid(row=0, columnspan=3)

        search_label.grid(row=1, column=0)
        search_entry.grid(row=1, column=1, ipadx=200)
        search_button.grid(row=1, column=3)

        replace_label.grid(row=2, column=0)
        replace_entry.grid(row=2, column=1, ipadx=200)
        replace_button.grid(row=2, column=3)