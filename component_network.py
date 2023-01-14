import socket
from tkinter import *

class tab_network:
    def __init__(self, root):
        self.root = root
        
        self.container = Frame(self.root)
        self.container.pack()

        self.createNetworkHeader()
        self.createPortScanner()

    def createNetworkHeader(self):
        # Variables
        hostname = StringVar()
        hostname.set(socket.gethostname())

        ip_address = StringVar()
        ip_address.set(socket.gethostbyname(hostname.get()))

        # Widget Root
        frame_header = Frame(self.container)
        frame_header.pack()
        # Widgets
        title = Label(frame_header, text="Computer Network Configuration")

        hostname_label = Label(frame_header, text="Hostname")
        hostname_entry = Entry(frame_header, textvariable=hostname)
        
        ip_label = Label(frame_header, text="IPv4")
        ip_entry = Entry(frame_header, textvariable=ip_address)

        # Render
        title.grid(row=0 , columnspan=2)

        hostname_label.grid(row=1, column=0)
        hostname_entry.grid(row=1, column=1)

        ip_label.grid(row=2, column=0)
        ip_entry.grid(row=2, column=1)





    def createPortScanner(self):
        # Widget Root
        frame_scanner = Frame(self.container)
        frame_scanner.pack()
        # Widgets
        title = Label(frame_scanner, text="Port Scanner")

        ip_label = Label(frame_scanner, text="IP Address")
        ip_entry = Entry(frame_scanner)

        portMin_label = Label(frame_scanner, text="Port Min")
        portMin_entry = Entry(frame_scanner)

        portMax_label = Label(frame_scanner, text="Port Max")
        portMax_entry = Entry(frame_scanner)

        search_button = Button(frame_scanner, text="Search")

        # Render
        title.grid(row=0, columnspan=3)

        ip_label.grid(row=1, column=0)
        ip_entry.grid(row=1, column=1, ipadx=100)
    
        portMin_label.grid(row=2, column=0)
        portMin_entry.grid(row=2, column=1, ipadx=100)
        portMax_label.grid(row=3, column=0)
        portMax_entry.grid(row=3, column=1, ipadx=100)

        search_button.grid(row=2, column=2)