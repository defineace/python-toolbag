from tkinter import *
from module_explorer import *

class guiTabExplorer:
    def __init__( self, root ):
        # Init tkinter gui explorer
        self.root = root

        self.path = StringVar()
        self.path.set("C:/")
        self.module_explorer = directoryExplorer(self.path.get())
        self.data = self.module_explorer.getDirectory()
        
        self.displayToolbar()
        self.displayTable()

    def displayToolbar( self ):
        # Search Bar
        self.label_path = Label( self.root, text="Path")
        self.entry_path = Entry( self.root, textvariable=self.path )
        self.button_path_goto = Button( self.root, text="Goto")
        self.label_path.pack()
        self.entry_path.pack()
        self.button_path_goto.pack()

        # Rename Search
        self.label_renameSearch = Label( self.root, text="Rename Search" )
        self.entry_renameSearch = Entry( self.root, text="" )
        self.button_renameSearch = Button( self.root, text="Rename Search")
        self.label_renameSearch.pack()
        self.entry_renameSearch.pack()
        self.button_renameSearch.pack()

        # Rename Replace
        self.label_renameReplace = Label( self.root, text="Rename Replace")
        self.entry_renameReplace = Entry( self.root, text="")
        self.button_renameReplace = Button( self.root, text="Rename Replace")
        self.label_renameReplace.pack()
        self.entry_renameReplace.pack()
        self.button_renameReplace.pack()

    def displayTable( self ):
        #############################################################
        #############################################################
        # Table Container
        #############################################################
        #############################################################
        self.table_canvas = Canvas( self.root )
        self.table_frame = Frame(self.table_canvas)
        #############################################################
        #############################################################
        # Table Scrollbar
        #############################################################
        #############################################################
        self.table_scrollbar = Scrollbar(self.root, orient="vertical", command=self.table_canvas.yview)
        self.table_canvas.configure(yscrollcommand=Scrollbar.set)
        
        self.table_scrollbar.pack(side=RIGHT, fill=Y)
        self.table_canvas.pack(side=LEFT)

        self.table_canvas.create_window((0,0), window=self.table_frame, anchor='nw')
        self.table_canvas.bind("<Configure>", self.bind_callback)
        #############################################################
        #############################################################
        # Table Header
        #############################################################
        #############################################################
        # Column Header Data
        header_index = StringVar()
        header_index.set("Index")
        header_dateCreated = StringVar()
        header_dateCreated.set("Date Created")
        header_dateModified = StringVar()
        header_dateModified.set("Date Last Modified")
        header_type = StringVar()
        header_type.set("Type")
        header_name = StringVar()
        header_name.set("Name")
        header_nameEdited = StringVar()
        header_nameEdited.set("Name Edited")
        
        # Column Header Widgets
        entry_header_index = Entry(self.table_frame, textvariable=header_index, font='Helvetica 8 bold')
        entry_header_dateCreated = Entry(self.table_frame, textvariable=header_dateCreated, font='Helvetica 8 bold')
        entry_header_dateModified = Entry(self.table_frame, textvariable=header_dateModified, font='Helvetica 8 bold')
        entry_header_type = Entry(self.table_frame, textvariable=header_type, font='Helvetica 8 bold')
        entry_header_name = Entry(self.table_frame, textvariable=header_name, font='Helvetica 8 bold')
        entry_header_nameEdited = Entry(self.table_frame, textvariable=header_nameEdited, font='Helvetica 8 bold')

        # Column Header Render
        entry_header_index.grid(row=0, column=0, ipadx=10)
        entry_header_dateCreated.grid(row=0, column=1, ipadx=10)
        entry_header_dateModified.grid(row=0, column=2, ipadx=10)
        entry_header_type.grid(row=0, column=3, ipadx=10)
        entry_header_name.grid(row=0, column=4, ipadx=10)
        entry_header_nameEdited.grid(row=0, column=5, ipadx=10)
        #############################################################
        #############################################################
        # Table Body
        #############################################################
        #############################################################
        for x, result in enumerate( self.data ):
            i = x + 1

            # Row Data
            data_index = StringVar()
            data_index.set( str(i) )
            data_dateCreated = StringVar()
            data_dateCreated.set( "N/A" )
            data_dateModified = StringVar()
            data_dateModified.set( "N/A" )
            data_type = StringVar()
            data_type.set( "N/A" )
            data_name = StringVar()
            data_name.set( result )
            data_nameEdited = StringVar()
            data_nameEdited.set("")

            # Row Widgets
            entry_col_index = Entry(self.table_frame, textvariable=data_index)
            entry_col_dateCreated = Entry(self.table_frame, textvariable=data_dateCreated)
            entry_col_dateModified = Entry(self.table_frame, textvariable=data_dateModified)
            entry_col_type = Entry(self.table_frame, textvariable=data_type)
            entry_col_name = Entry(self.table_frame, text=data_name)
            entry_col_nameEdited = Entry(self.table_frame, text=data_nameEdited)

            # Row Render
            entry_col_index.grid(row=i, column=0, ipadx=10)
            entry_col_dateCreated.grid(row=i, column=1, ipadx=10)
            entry_col_dateModified.grid(row=i, column=2, ipadx=10)
            entry_col_type.grid(row=i, column=3, ipadx=10)
            entry_col_name.grid(row=i, column=4, ipadx=10)
            entry_col_nameEdited.grid(row=i, column=5, ipadx=10)
        
    def bind_callback(self, event):
        self.table_canvas.configure(scrollregion=self.table_canvas.bbox("all"), width=900, height=300)