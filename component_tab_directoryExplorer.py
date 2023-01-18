from tkinter import *
from augment_directoryExplorer_table import *
from component_directoryExplorer_navbar_header import *
from component_directoryExplorer_navbar_searchReplace import *
from component_directoryExplorer_table_body import *



class tab_directoryExplorer:

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

        self.directoryExplorer = augment_directoryExplorer(self.path.get())
        self.table_data = self.directoryExplorer.getDirectory_filtered(self.filter.get())

        # Frames
        self.frame_navbar_header = Frame(self.root)
        self.frame_navbar_searchReplace = Frame(self.root)
        
        self.frame_navbar_header.pack(padx=10, pady=10)
        self.frame_navbar_searchReplace.pack()
        
        frame_table_body = Frame(self.root, borderwidth=1, relief="solid", padx=10, pady=10)
        frame_table_body.pack(padx=20, pady=20)        
        self.frameList.append(frame_table_body)

        # Create Explorer Navbar Header
        directoryExplorer_navbar_header(self.frame_navbar_header, self.path, self.filter)
        
        # Create Explorer Navbar Search and Replace
        directoryExplorer_navbar_searchReplace(self.frame_navbar_searchReplace, self.search, self.replace)
        
        # Create Explorer Table Body
        directoryExplorer_table_body(self.frameList[0], self.table_data)


    def createTable(self):
        # Clear table frame
        for frame in self.frameList:
            frame.destroy()

        # Frames
        frame_table_body = Frame(self.root, borderwidth=1, relief="solid", padx=10, pady=10)
        frame_table_body.pack(padx=20, pady=20)        
        self.frameList.append(frame_table_body)
     