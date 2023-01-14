from tkinter import *
import os

class tab_explorer:
    def __init__(self, root):
        self.root = root
        
        self.container = Frame(self.root)
        self.container.pack()

        self.path = StringVar()
        self.filename_filter = StringVar()

        self.createExplorerHeader()


    def createExplorerHeader(self):
        # Widgets
        frame_header = Frame(self.container)
        frame_header.pack()

        path_label = Label(frame_header,text="Path")
        path_entry = Entry(frame_header, textvariable=self.path)

        filter_label = Label(frame_header,text="Filter")
        filter_entry = Entry(frame_header, textvariable=self.filename_filter)

        search_button = Button(frame_header, text="Search", command=self.createTable)
        
        # Render
        path_label.grid(row=0, column=0)
        path_entry.grid(row=0, column=1, ipadx=300)
    
        filter_label.grid(row=1, column=0)
        filter_entry.grid(row=1, column=1, ipadx=300)

        search_button.grid(row=0, column=2, rowspan=2)


    def createTable(self):
        frame_table = Frame(self.container)
        frame_table.pack()

        directory = os.listdir(self.path.get())
        for filename in directory:
            i = directory.index(filename)

            if(filename.__contains__(self.filename_filter.get())):
                # Variables
                filename_original = StringVar()
                filename_original.set(filename)

                # Widgets
                index_entry = Entry(frame_table, text="Result: " + str(directory.index(filename)+1))
                
                filename_original_entry = Entry(frame_table, text=filename_original)
                filename_rename_entry = Entry(frame_table, text='')
                
                # Render
                index_entry.grid(row=i, column=0)
                filename_original_entry.grid(row=i, column=1, ipadx=100)
                filename_rename_entry.grid(row=i, column=2, ipadx=100)

