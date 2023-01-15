from tkinter import *
import os

class fragment_table:
    def __init__(self, root, path, filter, search, replace):
        # Main Variables
        self.root = root
        
        self.path = path
        self.filter = filter
        self.search = search
        self.replace = replace
        
        # Main Widget Root
        self.canvas_container = Canvas(self.root)
        
        # Main Widgets
        self.frame_container = Frame(self.canvas_container)
        scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas_container.yview)
        self.canvas_container.configure(yscrollcommand=scrollbar.set)

        # Scrollbar Configuration
        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas_container.pack(side=LEFT)

        self.canvas_container.create_window((0,0), window=self.frame_container, anchor='nw')
        self.frame_container.bind("<Configure>", self.bind_callback) 

        # Render
        directory = os.listdir(self.path.get())
        for filename in directory:
            i = directory.index(filename)

            if(filename.__contains__(self.filter.get())):
                # Sub Variables
                index_label = StringVar()
                index_label.set("Result: " + str(directory.index(filename)+1))

                filename_original = StringVar()
                filename_original.set(filename)

                filename_new = StringVar()
                filename_new.set(filename.replace(self.search.get(), self.replace.get()))


                # Sub Widgets
                filename_index_entry = Entry(self.frame_container, textvariable=index_label)
                filename_original_entry = Entry(self.frame_container, text=filename_original)
                filename_new_entry = Entry(self.frame_container, text=filename_new)

                    
                # Sub Render
                filename_index_entry.grid(row=i, column=0)
                filename_original_entry.grid(row=i, column=1, ipadx=157)
                filename_new_entry.grid(row=i, column=2, ipadx=157)
            
    def bind_callback(self, event):
        self.canvas_container.configure(scrollregion=self.canvas_container.bbox("all"), width=1000, height=300)