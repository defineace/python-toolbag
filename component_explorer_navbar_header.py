from tkinter import *
class component_explorer_navbar_header:
    def __init__(self, tab_explorer, root, path, filter):
        #Variables
        self.tab_explorer = tab_explorer
        
        print(self.tab_explorer)

        self.root = root
        self.path = path
        self.filter = filter

        self.path.set(self.path.get())
        self.filter.set(self.filter.get())

        # Widgets
        path_label = Label(self.root,text="Path")
        path_entry = Entry(self.root, textvariable=self.path)

        filter_label = Label(self.root,text="Filter")
        filter_entry = Entry(self.root, textvariable=self.filter)

        search_button = Button(self.root, text="Go To", command= lambda: self.tab_explorer.createTable(self))
        
        # Render
        path_label.grid(row=0, column=0)
        path_entry.grid(row=0, column=1, ipadx=300)

        filter_label.grid(row=1, column=0)
        filter_entry.grid(row=1, column=1, ipadx=300)

        search_button.grid(row=0, column=2, rowspan=2)