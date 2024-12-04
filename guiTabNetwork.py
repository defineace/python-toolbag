from tkinter import *

class guiTabNetwork:
    def __init__( self, root ):
        self.root = root
        self.displayNetworkConfiguration()

    def displayNetworkConfiguration( self ):
        # Display Network Configuration
        self.label_networkAdapter = Label( self.root, text="Network Adapter")
        self.entry_networkAdapter = Entry( self.root )
        self.label_ipv4 = Label(self.root, text="IPv4")
        self.entry_ipv4 = Entry(self.root)
        self.label_ipv6 = Label(self.root, text="IPv6")
        self.entry_ipv6 = Entry(self.root)
        self.label_subnet = Label(self.root, text="Subnet")
        self.entry_subnet = Entry(self.root)
        self.label_gateway = Label(self.root, text="Gateway")
        self.entry_gateway = Entry(self.root)

        self.label_networkAdapter.pack()
        self.entry_networkAdapter.pack()
        self.label_ipv4.pack()
        self.entry_ipv4.pack()
        self.label_ipv6.pack()
        self.entry_ipv6.pack()
        self.label_subnet.pack()
        self.entry_subnet.pack()
        self.label_gateway.pack()
        self.entry_gateway.pack()