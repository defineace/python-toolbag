from tkinter import *

class component_explorer_navbar_searchReplace:
    def __init__(self, root, search, replace):
        # Variables
        self.root = root
        self.search = search
        self.replace = replace

        self.search.set(self.search.get())
        self.replace.set(self.replace.get())

        # Widgets
        title_label = Label(self.root, text="Search and Replace")

        search_label = Label(self.root, text="Search")
        search_entry = Entry(self.root, textvariable=self.search)
        search_button = Button(self.root, text="Search")

        replace_label = Label(self.root, text="Replace")
        replace_entry = Entry(self.root, textvariable=self.replace)
        replace_button = Button(self.root, text="Replace")

        # Render
        title_label.grid(row=0, columnspan=3)

        search_label.grid(row=1, column=0)
        search_entry.grid(row=1, column=1, ipadx=200)
        search_button.grid(row=1, column=3)

        replace_label.grid(row=2, column=0)
        replace_entry.grid(row=2, column=1, ipadx=200)
        replace_button.grid(row=2, column=3)