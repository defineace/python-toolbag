from tkinter import *
import socket
import psutil

class network_header:
    def __init__(self, root):
        self.root = root

         # Variables


        self.computer_name = socket.gethostname()
        self.ipv4 = socket.getaddrinfo(self.computer_name, 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][4][0]
        self.ipv6 = socket.getaddrinfo(self.computer_name, 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0]
        self.network_adapters = psutil.net_if_addrs()

        hostname = StringVar()
        hostname.set(self.computer_name)

        ipv4_address = StringVar()
        ipv4_address.set(self.ipv4)

        ipv6_address = StringVar()
        ipv6_address.set(self.ipv6)

        # Widgets
        title = Label(self.root, text="Computer Network Configuration")

        hostname_label = Label(self.root, text="Hostname")
        hostname_entry = Entry(self.root, textvariable=hostname)
        
        ipv4_label = Label(self.root, text="IPv4")
        ipv4_entry = Entry(self.root, textvariable=ipv4_address)

        ipv6_label = Label(self.root, text="IPv6")
        ipv6_entry = Entry(self.root, textvariable=ipv6_address)
        
        # Render
        title.grid(row=0 , columnspan=2)

        hostname_label.grid(row=1, column=0)
        hostname_entry.grid(row=1, column=1, ipadx=50)

        ipv4_label.grid(row=2, column=0)
        ipv4_entry.grid(row=2, column=1, ipadx=50)

        ipv6_label.grid(row=3, column=0)
        ipv6_entry.grid(row=3, column=1, ipadx=50)

        adapter_label = Label(self.root, text="Local Network Adapters")
        adapter_label.grid(row=4, columnspan=3)

        for i,result in enumerate(self.network_adapters):
            adapter = StringVar()
            adapter.set(result)

            adapter_entry = Entry(self.root, textvariable=adapter)
            adapter_entry.grid(row=5+i, columnspan=3, ipadx=50)