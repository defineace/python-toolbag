from tkinter import *
from augment_directoryExplorer_table import *
from component_directoryExplorer_navbar_header import *
from component_directoryExplorer_navbar_fileRename import *
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
        self.filter.set("tab")

        self.search.set("augment")
        self.replace.set("augments")

        # Frames
        self.frame_navbar_header = Frame(self.root)
        self.frame_navbar_searchReplace = Frame(self.root)
        
        self.frame_navbar_header.pack(padx=10, pady=10)
        self.frame_navbar_searchReplace.pack()
        
        self.frame_table_body = Frame(self.root, borderwidth=1, relief="solid", padx=10, pady=10)
        self.frame_table_body.pack(padx=20, pady=20)

        # Create OS directory explorer
        self.directoryExplorer = augment_directoryExplorer(self.path.get())
        
        self.dataList_1 = self.directoryExplorer.getDirectory_filtered(self.filter.get())
        self.dataList_2 = []

        # Create explorer navbar header
        self.navbar_header = directoryExplorer_navbar_header(self.frame_navbar_header, self.buttonClicked_goto)
        
        # Config navbar header
        self.config_navbarHeader()

        # Create explorer navbar file rename
        self.navbar_fileRename = directoryExplorer_navbar_fileRename(self.frame_navbar_searchReplace, self.buttonClicked_search, self.buttonClicked_replace)
        
        # Config navbar file rename
        self.config_fileRename()

        # Create directory explorer table results
        self.createTable()


        
    def config_navbarHeader(self):
        self.navbar_header.path.set(self.path.get())
        self.navbar_header.filter.set(self.filter.get())

    def config_fileRename(self):
        self.navbar_fileRename.search.set(self.search.get())
        self.navbar_fileRename.replace.set(self.replace.get())
    
    def createTable(self):
        # Clear table frame
        self.frame_table_body.destroy()

        # Frames
        self.frame_table_body = Frame(self.root, borderwidth=1, relief="solid", padx=10, pady=10)
        self.frame_table_body.pack(padx=20, pady=20)      

        # Create Explorer Table Body
        directoryExplorer_table_body(self.frame_table_body, self.dataList_1, self.dataList_2)

    def buttonClicked_goto(self, path, filter):
        # Function for goto button in navbar header
        
        #Update vaiables
        self.path.set(path)
        self.filter.set(filter)

        # Update OS Directory Explorer
        self.directoryExplorer.updatePath(self.path.get())

        self.dataList_1 = self.directoryExplorer.getDirectory_filtered(self.filter.get())
        self.dataList_2 = []

        # Refresh Table
        self.createTable()

    def buttonClicked_search(self, search, replace):
        print("Search Clicked")
        self.search.set(search)
        self.replace.set(replace)

        self.dataList_1 = self.directoryExplorer.getDirectory_filtered(self.filter.get())
        self.dataList_2 = self.directoryExplorer.getDirectory_previewRename_filtered(self.search.get(), self.replace.get(), self.filter.get())

        # Refresh Table
        self.createTable()

    def buttonClicked_replace(self, search, replace):
        print("Replace Clicked")
        self.search.set(search)
        self.replace.set(replace)

        # Change file name
        if(len(self.dataList_2) != 0):
            self.directoryExplorer.editDirectory_fileRename(self.search.get(), self.replace.get())

            self.navbar_fileRename.search_entry.configure( bg="white")
            self.navbar_fileRename.search_button.configure( bg="SystemButtonFace")
        else:
            self.navbar_fileRename.search_entry.configure( bg="#e8baba")
            self.navbar_fileRename.search_button.configure( bg="#e8baba")

        # Update OS Directory Explorer
        self.directoryExplorer.updatePath(self.path.get())

        self.dataList_1 = self.directoryExplorer.getDirectory_filtered(self.filter.get())
        self.dataList_2 = []


        # Refresh Table
        self.createTable()