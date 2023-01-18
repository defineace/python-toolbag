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
        
        self.path.set("C:/Users/lrdef/Desktop/Projects/Coding/Python/python-toolbag-gui")
        self.filter.set("")

        self.search.set("utility_")
        self.replace.set("utility_category_")

        # Frames
        self.frame_navbar_header = Frame(self.root)
        self.frame_navbar_searchReplace = Frame(self.root)
        
        self.frame_navbar_header.pack(padx=10, pady=10)
        self.frame_navbar_searchReplace.pack()
        
        self.frame_table_body = Frame(self.root, borderwidth=1, relief="solid", padx=10, pady=10)
        self.frame_table_body.pack(padx=20, pady=20)

        # Create OS Directory Explorer
        self.directoryExplorer = augment_directoryExplorer(self.path.get())
        self.table_data = self.directoryExplorer.getDirectory_filtered(self.filter.get())

        # Create Explorer Navbar Header
        self.navbar_header = directoryExplorer_navbar_header(self.frame_navbar_header, self.updateTable_goto)
        
        # Config navbar header
        self.config_navbarHeader()

        # Create Explorer Navbar Search and Replace
        self.navbar_searchReplace = directoryExplorer_navbar_searchReplace(self.frame_navbar_searchReplace, self.search, self.replace)
        
        self.createTable()


        
    def config_navbarHeader(self):
        self.navbar_header.path.set(self.path.get())
        self.navbar_header.filter.set(self.filter.get())

    def createTable(self):
        # Clear table frame
        self.frame_table_body.destroy()

        # Frames
        self.frame_table_body = Frame(self.root, borderwidth=1, relief="solid", padx=10, pady=10)
        self.frame_table_body.pack(padx=20, pady=20)      

        # Create Explorer Table Body
        directoryExplorer_table_body(self.frame_table_body, self.table_data)

    def updateTable_goto(self, path, filter):
        # Function for goto button in navbar header
        
        #Update vaiables
        self.path = path
        self.filter = filter

        # Update OS Directory Explorer
        self.directoryExplorer.updatePath(self.path)
        self.table_data = self.directoryExplorer.getDirectory_filtered(self.filter)

        # Refresh Table
        self.createTable()


