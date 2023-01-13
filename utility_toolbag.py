from asyncio.windows_events import NULL
import os
from tkinter import *



##########################################################################################

root = Tk()
frameList = []

path = StringVar()
path.set("C:/Users/lrdef/Desktop/Projects/Coding/Python/")

filename_filter = StringVar()
filename_filter.set('.py')
filename_replace = StringVar()
def callback():
    print("Traced variable: ", filename_replace.get())
filename_replace.trace_add("write", callback)

##########################################################################################

def createTable():

    if(len(frameList) != 0):
        for frame in frameList:
            frame.destroy()
    frame_tableHeader = Frame(root)
    frame_table = Frame(root)

    frameList.append(frame_tableHeader)
    frameList.append(frame_table)

    frame_tableHeader.pack()
    frame_table.pack()

#-------------------------------------------------

    replace_button = Button(frame_tableHeader, text="Replace")
    replace_entry = Entry(frame_tableHeader, textvariable=filename_replace)

    replace_button.grid(row=0,column=0)
    replace_entry.grid(row=0,column=1, ipadx=100)

#-------------------------------------------------
    directory = os.listdir(path.get())
    for filename in directory:
        i = directory.index(filename)

        if(filename.__contains__(filename_filter.get())):
            element_label = Label(frame_table, text="Result: " + str(directory.index(filename)+1))
            
            filename_original = StringVar()
            filename_original.set(filename)

            element_original = Entry(frame_table, text=filename_original)
            element_rename = Entry(frame_table, text=filename_replace)
        
            element_label.grid(row=i, column=0)
            element_original.grid(row=i, column=1, ipadx=100)
            element_rename.grid(row=i, column=2, ipadx=100)

##########################################################################################

def main():

    frame_header = Frame(root)
    frame_header.pack()

    path_label = Label(frame_header,text="Path")
    path_entry = Entry(frame_header, textvariable=path)

    filter_label = Label(frame_header,text="Filter")
    filter_entry = Entry(frame_header, textvariable=filename_filter)

    search_button = Button(frame_header, text="Search", command=createTable)

    path_label.grid(row=0, column=0)
    path_entry.grid(row=0, column=1, ipadx=300)
   
    filter_label.grid(row=1, column=0)
    filter_entry.grid(row=1, column=1, ipadx=300)

    search_button.grid(row=0, column=2, rowspan=2)

    root.mainloop()

main()


"""
path = "C:/Users/lrdef/Desktop/Projects/Coding/Python/"

prefix = "blueprint"
edit = prefix + " -"

for filename in os.listdir(path):
    if(filename.__contains__(prefix)):
        print("Old File Name: " + filename)

        if(filename.__contains__(edit)):
            print("File Name: Up to Date")
        else:
            new_filename = filename.replace(prefix,edit)
            print("New File Name: " + new_filename)
            
            os.rename(path + filename,path + new_filename)
        
        print("-----------------------------------------------------")

    
"""