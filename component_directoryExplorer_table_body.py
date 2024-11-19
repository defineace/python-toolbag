from tkinter import *

class directoryExplorer_table_body:
    # data takes in 2 list [[original directory results],[edited directory results]]
    def __init__(self, root, data_1, data_2, data_dateCreated, data_dateModified, data_type):
        # Variables
        self.root = root
        self.data_1 = data_1
        self.data_2 = data_2
        self.data_dateCreated = data_dateCreated
        self.data_dateModified = data_dateModified
        self.data_type = data_type

        # Main Widget Root
        self.canvas_container = Canvas(self.root)
        
        # Main Widgets+
        
        self.frame_container = Frame(self.canvas_container)
        scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas_container.yview)
        self.canvas_container.configure(yscrollcommand=scrollbar.set)

        # Scrollbar Configuration
        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas_container.pack(side=LEFT)

        self.canvas_container.create_window((0,0), window=self.frame_container, anchor='nw')
        self.frame_container.bind("<Configure>", self.bind_callback) 



        # Render - Column Header
        # Column Header Variables
        columnHeader_index = StringVar()
        columnHeader_index.set("Index")

        columnHeader_dateCreated = StringVar()
        columnHeader_dateCreated.set("Date Created")

        columnHeader_dateModified = StringVar()
        columnHeader_dateModified.set("Date Last Modified")

        columnHeader_type = StringVar()
        columnHeader_type.set("Type")

        columnHeader_fileName_old = StringVar()
        columnHeader_fileName_old.set("Name")

        columnHeader_fileName_new = StringVar()
        columnHeader_fileName_new.set("Search and Replace")

        # Column Header Widgets
        columnHeader_index_entry = Entry(self.frame_container, textvariable=columnHeader_index, font='Helvetica 8 bold')

        columnHeader_dateCreated_entry = Entry(self.frame_container, textvariable=columnHeader_dateCreated, font='Helvetica 8 bold')
        columnHeader_dateModified_entry = Entry(self.frame_container, textvariable=columnHeader_dateModified, font='Helvetica 8 bold')

        columnHeader_type_entry = Entry(self.frame_container, textvariable=columnHeader_type, font='Helvetica 8 bold')

        columnHeader_fileName_old_entry = Entry(self.frame_container, text=columnHeader_fileName_old, font='Helvetica 8 bold')
        columnHeader_fileName_new_entry = Entry(self.frame_container, text=columnHeader_fileName_new, font='Helvetica 8 bold')

        # Column Header Render
        columnHeader_index_entry.grid(row=0, column=0)

        columnHeader_dateCreated_entry.grid(row=0, column=1, ipadx=30)
        columnHeader_dateModified_entry.grid(row=0, column=2, ipadx=30)

        columnHeader_type_entry.grid(row=0, column=3)

        columnHeader_fileName_old_entry.grid(row=0, column=4, ipadx=157)
        columnHeader_fileName_new_entry.grid(row=0, column=5, ipadx=157)



        # Render - Directory Results
        for x,result in enumerate(self.data_1):
            i = x + 1

            # Column Variables
            column_index = StringVar()
            column_index.set(str(i))

            column_dateCreated = StringVar()
            column_dateCreated.set(self.data_dateCreated[x])

            column_dateModified = StringVar()
            column_dateModified.set(self.data_dateModified[x])

            column_type = StringVar()
            column_type.set(self.data_type[x])

            column_fileName_old = StringVar()
            column_fileName_old.set(result)

            column_filename_new = StringVar()
            column_filename_new.set("")

            # Column Widgets
            column_index_entry = Entry(self.frame_container, textvariable=column_index)

            column_dateCreated_entry = Entry(self.frame_container, textvariable=column_dateCreated)
            column_dateModified_entry = Entry(self.frame_container, textvariable=column_dateModified)

            column_type_entry = Entry(self.frame_container, textvariable=column_type)

            column_fileName_old_entry = Entry(self.frame_container, text=column_fileName_old)
            column_fileName_new_entry = Entry(self.frame_container, text=column_filename_new)

            # Column Render
            column_index_entry.grid(row=i, column=0)

            column_dateCreated_entry.grid(row=i, column=1, ipadx=30)
            column_dateModified_entry.grid(row=i, column=2, ipadx=30)

            column_type_entry.grid(row=i, column=3)

            column_fileName_old_entry.grid(row=i, column=4, ipadx=157)
            column_fileName_new_entry.grid(row=i, column=5, ipadx=157)

        # Render - Search and Replace
        for x,result in enumerate(self.data_2):
            i = x + 1

            # Column Variables
            column_filename_new = StringVar()
            column_filename_new.set(result)

            # Column Widgets
            column_fileName_new = Entry(self.frame_container, text=column_filename_new)

            # Column Render
            column_fileName_new.grid(row=i, column=2, ipadx=157)



    def bind_callback(self, event):
        self.canvas_container.configure(scrollregion=self.canvas_container.bbox("all"), width=1500, height=300)