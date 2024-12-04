from tkinter import *
from module_explorer import *

class guiTabExplorer:
    def __init__( self, root ):
        #############################################################
        #############################################################
        # Initiate Explorer Module
        #############################################################
        #############################################################
        self.path = StringVar()
        self.path.set("C:/")
        self.module_explorer = directoryExplorer(self.path.get())
        self.module_explorer_dir = self.module_explorer.returnDirectory()
        #############################################################
        #############################################################
        # GUI Widgets
        #############################################################
        #############################################################
        self.root = root
        self.TOOLBAR_ENTRY_WIDTH = 100
        self.TOOLBAR_BUTTON_WIDTH = 15
        self.TABLE_WIDTH = 900
        self.TABLE_HEIGHT = 400
        self.TABLE_COL_WIDTH = 15
        #############################################################
        #############################################################
        # Render Widgets
        #############################################################
        #############################################################

        self.displayExplorerTab()
        self.displayToolbar()
        self.displayTable()

    def displayExplorerTab( self ):
        self.frame_tabExplorer = Frame(self.root)
        self.frame_tabExplorer.pack()

    def displayToolbar( self ):
        #############################################################
        #############################################################
        # GUI Widgets
        #############################################################
        #############################################################
        self.frame_toolbar = Frame( self.frame_tabExplorer)

        self.label_path = Label( self.frame_toolbar, text="Path")
        self.entry_path = Entry( self.frame_toolbar, textvariable=self.path)
        self.button_path_goto = Button( self.frame_toolbar, text="Goto", width=self.TOOLBAR_BUTTON_WIDTH)
        self.label_renameSearch = Label( self.frame_toolbar, text="Name Search" )
        self.entry_renameSearch = Entry( self.frame_toolbar, text="" )
        self.button_renameSearch = Button( self.frame_toolbar, text="Name Search", width=self.TOOLBAR_BUTTON_WIDTH) 
        self.label_renameReplace = Label( self.frame_toolbar, text="Name Replace")
        self.entry_renameReplace = Entry( self.frame_toolbar, text="")
        self.button_renameReplace = Button( self.frame_toolbar, text="Name Replace", width=self.TOOLBAR_BUTTON_WIDTH)
        
        #############################################################
        #############################################################
        # Render
        #############################################################
        #############################################################
        self.frame_toolbar.pack()

        self.label_path.grid(row = 0, column = 0)
        self.entry_path.grid(row = 0, column = 1, ipadx=self.TOOLBAR_ENTRY_WIDTH)
        self.button_path_goto.grid(row = 0, column = 2)
        self.label_renameSearch.grid(row = 1, column = 0)
        self.entry_renameSearch.grid(row = 1, column = 1, ipadx=self.TOOLBAR_ENTRY_WIDTH)
        self.button_renameSearch.grid(row = 1, column = 2)
        self.label_renameReplace.grid(row = 2, column = 0)
        self.entry_renameReplace.grid(row = 2, column = 1, ipadx=self.TOOLBAR_ENTRY_WIDTH)
        self.button_renameReplace.grid(row = 2, column = 2)

    def displayTable( self ):
        #############################################################
        #############################################################
        # Table Container
        #############################################################
        #############################################################
        self.table_canvas = Canvas( self.frame_tabExplorer , width=self.TABLE_WIDTH, height=self.TABLE_HEIGHT)
        self.frame_table = Frame(self.table_canvas)
        #############################################################
        #############################################################
        # Table Scrollbar
        #############################################################
        #############################################################
        self.table_scrollbar = Scrollbar(self.frame_tabExplorer, orient="vertical", command=self.table_canvas.yview)
        self.table_canvas.configure(yscrollcommand=Scrollbar.set)
        
        self.table_scrollbar.pack(side=RIGHT, fill=Y)
        self.table_canvas.pack(side=LEFT)

        self.table_canvas.create_window((0,0), window=self.frame_table, anchor='nw')
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
        header_nameEdited.set("Name Replace")
        
        # Column Header Widgets
        entry_header_index = Entry(self.frame_table, textvariable=header_index, font='Helvetica 8 bold')
        entry_header_dateCreated = Entry(self.frame_table, textvariable=header_dateCreated, font='Helvetica 8 bold')
        entry_header_dateModified = Entry(self.frame_table, textvariable=header_dateModified, font='Helvetica 8 bold')
        entry_header_type = Entry(self.frame_table, textvariable=header_type, font='Helvetica 8 bold')
        entry_header_name = Entry(self.frame_table, textvariable=header_name, font='Helvetica 8 bold')
        entry_header_nameEdited = Entry(self.frame_table, textvariable=header_nameEdited, font='Helvetica 8 bold')

        # Column Header Render
        entry_header_index.grid(row=0, column=0, ipadx=.05)
        entry_header_dateCreated.grid(row=0, column=1, ipadx=self.TABLE_COL_WIDTH)
        entry_header_dateModified.grid(row=0, column=2, ipadx=self.TABLE_COL_WIDTH)
        entry_header_type.grid(row=0, column=3, ipadx=self.TABLE_COL_WIDTH)
        entry_header_name.grid(row=0, column=4, ipadx=self.TABLE_COL_WIDTH)
        entry_header_nameEdited.grid(row=0, column=5, ipadx=self.TABLE_COL_WIDTH)
        #############################################################
        #############################################################
        # Table Body
        #############################################################
        #############################################################
        for x, result in enumerate( self.module_explorer_dir ):
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
            entry_col_index = Entry(self.frame_table, textvariable=data_index)
            entry_col_dateCreated = Entry(self.frame_table, textvariable=data_dateCreated)
            entry_col_dateModified = Entry(self.frame_table, textvariable=data_dateModified)
            entry_col_type = Entry(self.frame_table, textvariable=data_type)
            entry_col_name = Entry(self.frame_table, text=data_name)
            entry_col_nameEdited = Entry(self.frame_table, text=data_nameEdited)

            # Row Render
            entry_col_index.grid(row=i, column=0, ipadx=.05)
            entry_col_dateCreated.grid(row=i, column=1, ipadx=self.TABLE_COL_WIDTH)
            entry_col_dateModified.grid(row=i, column=2, ipadx=self.TABLE_COL_WIDTH)
            entry_col_type.grid(row=i, column=3, ipadx=self.TABLE_COL_WIDTH)
            entry_col_name.grid(row=i, column=4, ipadx=self.TABLE_COL_WIDTH)
            entry_col_nameEdited.grid(row=i, column=5, ipadx=self.TABLE_COL_WIDTH)

    def bind_callback(self, event):
        self.table_canvas.configure(scrollregion=self.table_canvas.bbox("all"), ipadx=self.TABLE_WIDTH, height=self.TABLE_HEIGHT)6

