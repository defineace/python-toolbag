from tkinter import *

class network_portScanner:
    def __init__(self, root):
        self.root = root

        # Widgets
        title = Label(self.root, text="Port Scanner")

        ip_label = Label(self.root, text="IP Address")
        ip_entry = Entry(self.root)

        portMin_label = Label(self.root, text="Port Min")
        portMin_entry = Entry(self.root)

        portMax_label = Label(self.root, text="Port Max")
        portMax_entry = Entry(self.root)

        search_button = Button(self.root, text="Search")

        # Render
        title.grid(row=0, columnspan=3)

        ip_label.grid(row=1, column=0)
        ip_entry.grid(row=1, column=1, ipadx=100)
    
        portMin_label.grid(row=2, column=0)
        portMin_entry.grid(row=2, column=1, ipadx=100)
        portMax_label.grid(row=3, column=0)
        portMax_entry.grid(row=3, column=1, ipadx=100)

        search_button.grid(row=2, column=2)
