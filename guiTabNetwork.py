from tkinter import *
from module_network import *

class guiTabNetwork:
    def __init__( self, root ):
        #############################################################
        #############################################################
        # Initiate Explorer Module
        #############################################################
        #############################################################
        self.module_network = networkManager()
        self.networkAdapter = StringVar()
        self.hostname = StringVar()
        self.ipv4 = StringVar()
        self.ipv6 = StringVar()
        self.subnet = StringVar()
        self.gateway = StringVar()

        self.networkAdapter.set( self.module_network.returnIPConfiguration()[0])
        self.hostname.set( self.module_network.returnIPConfiguration()[1] )
        self.ipv4.set( self.module_network.returnIPConfiguration()[2] )
        self.ipv6.set( self.module_network.returnIPConfiguration()[3] )
        self.subnet.set( self.module_network.returnIPConfiguration()[4] )
        self.gateway.set( self.module_network.returnIPConfiguration()[5] )

        self.networkAdapters = self.module_network.returnNetworkAdapters()
        #############################################################
        #############################################################
        # GUI Widgets
        #############################################################
        #############################################################
        self.root = root
        self.NETWORKCONFIG_ENTRY_WIDTH = 30
        #############################################################
        #############################################################
        # Render Widgets
        #############################################################
        #############################################################
        
        self.displayTab()
        self.displayNetworkConfiguration()
    
    def displayTab( self ):
        self.frame_tabNetworkManager = Frame(self.root)
        self.frame_tabNetworkManager.pack()

    def displayNetworkConfiguration( self ):
        self.frame_networkConfiguration = Frame( self.frame_tabNetworkManager )
        self.frame_networkConfiguration.pack()

        # Display Network Configuration
        self.label_networkAdapter = Label( self.frame_networkConfiguration, text="Network Adapter")
        self.entry_networkAdapter = Entry( self.frame_networkConfiguration, textvariable=self.networkAdapter, width=self.NETWORKCONFIG_ENTRY_WIDTH)
        self.label_ipv4 = Label( self.frame_networkConfiguration, text="IPv4")
        self.entry_ipv4 = Entry( self.frame_networkConfiguration, textvariable=self.ipv4, width=self.NETWORKCONFIG_ENTRY_WIDTH)
        self.label_ipv6 = Label( self.frame_networkConfiguration, text="IPv6")
        self.entry_ipv6 = Entry( self.frame_networkConfiguration, textvariable=self.ipv6, width=self.NETWORKCONFIG_ENTRY_WIDTH)
        self.label_subnet = Label( self.frame_networkConfiguration, text="Subnet")
        self.entry_subnet = Entry( self.frame_networkConfiguration, textvariable=self.subnet, width=self.NETWORKCONFIG_ENTRY_WIDTH)
        self.label_gateway = Label( self.frame_networkConfiguration, text="Gateway")
        self.entry_gateway = Entry( self.frame_networkConfiguration, textvariable=self.gateway, width=self.NETWORKCONFIG_ENTRY_WIDTH)

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