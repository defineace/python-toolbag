from tkinter import *
import os

class tab_explorer:
    def __init__(self, root):
        self.root = root
        self.frameList = []

        self.path = StringVar()
        self.filename_filter = StringVar()

        self.path.set("C:/Users/lrdef/Desktop/Projects/Coding/Python/python-practice")
        self.filename_filter.set("utility")

        self.createExplorerHeader()


    def createExplorerHeader(self):
        # Widget Root
        frame_header = Frame(self.root)
        frame_header.pack()

        # Widgets
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


    def createTableHeader(self):
        # Variables
        prefix = StringVar()


        # Widget Root
        frame_tableHeader = Frame(self.root)
        self.frameList.append(frame_tableHeader)
        frame_tableHeader.pack()

        # Widgets
        filename_prefix_label = Label(frame_tableHeader, text="File Name Prefix")
        filename_prefix_entry = Entry(frame_tableHeader)

        filename_root_label = Label(frame_tableHeader, text="File Name Root")
        filename_root_entry = Entry(frame_tableHeader)

        filename_suffix_label = Label(frame_tableHeader, text="File Name Suffix")
        filename_suffix_entry = Entry(frame_tableHeader)

        filename_delimiter_label = Label(frame_tableHeader, text="File Name Delimiter")
        filename_delimiter_entry = Entry(frame_tableHeader)

        filename_index_label = Label(frame_tableHeader, text="File Name Indexing")
        filename_index_entry = Entry(frame_tableHeader)

        # Render
        filename_prefix_label.grid(row=0, column=0)
        filename_prefix_entry.grid(row=1, column=0)

        filename_root_label.grid(row=0, column=1)
        filename_root_entry.grid(row=1, column=1)

        filename_suffix_label.grid(row=0, column=2)
        filename_suffix_entry.grid(row=1, column=2)

        filename_delimiter_label.grid(row=0, column=3)
        filename_delimiter_entry.grid(row=1, column=3)

        filename_index_label.grid(row=0, column=4)
        filename_index_entry.grid(row=1, column=4)

    def createTable(self):
        # Clear Table
        if(len(self.frameList) != 0):
            for frame in self.frameList:
                frame.destroy()

        self.createTableHeader()

        # Widget Root
        frame_table = Frame(self.root)
        self.frameList.append(frame_table)
        frame_table.pack()

        directory = os.listdir(self.path.get())
        for filename in directory:
            i = directory.index(filename)

            if(filename.__contains__(self.filename_filter.get())):
                # Variables
                index_label = StringVar()
                index_label.set("Result: " + str(directory.index(filename)+1))

                filename_original = StringVar()
                filename_original.set(filename)

                """
                if(filename.__contains__('.')):
                    index_label.set("File: " + str(index_file))
                    index_file += 1
                else:
                    index_label.set("Directory: " + str(index_dir))
                    index_dir += 1

                filename_original = StringVar()
                filename_original.set(filename)
                """


                # Widgets
                index_entry = Entry(frame_table, textvariable=index_label)
                
                filename_original_entry = Entry(frame_table, text=filename_original)
                filename_rename_entry = Entry(frame_table, text='')
                
                # Render
                index_entry.grid(row=i, column=0)
                filename_original_entry.grid(row=i, column=1, ipadx=100)
                filename_rename_entry.grid(row=i, column=2, ipadx=100)