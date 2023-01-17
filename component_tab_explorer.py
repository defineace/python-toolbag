from tkinter import *
from component_explorer_navbar_header import *
from component_explorer_navbar_searchReplace import *
from component_explorer_table_body import *
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
        
        self.path.set("C:/")
        self.filter.set("")

        self.search.set("utility_")
        self.replace.set("utility_category_")

        self.explorer = fragment_directory_explorer(self.path.get())
        self.table_data = self.explorer.getDirectory_filtered(self.filter.get())

        # Frames
        self.frame_navbar_header = Frame(self.root)
        self.frame_navbar_searchReplace = Frame(self.root)
        
        self.frame_navbar_header.pack()
        self.frame_navbar_searchReplace.pack()
        
        self.createTable()

        # Create Explorer Navbar Header
        component_explorer_navbar_header(tab_explorer, self.frame_navbar_header, self.path, self.filter)
        
        # Create Explorer Navbar Search and Replace
        component_explorer_navbar_searchReplace(self.frame_navbar_searchReplace, self.search, self.replace)
        
        # Create Explorer Table Body
        component_explorer_table_body(self.frameList[0], self.table_data)


    def createTable(self):
        for frame in self.frameList:
            frame.destroy()

        # Frames
        frame_table_body = Frame(self.root)
        frame_table_body.pack()        
        self.frameList.append(frame_table_body)
        
        print("Frame Created")