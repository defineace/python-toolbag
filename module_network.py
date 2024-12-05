import socket
import psutil

class networkManager:
    def __init__( self ):
        # Network Configuration
        self.networkAdapter = 'N/A'
        self.hostname = socket.gethostname()
        self.ipv4 = socket.getaddrinfo( self.hostname, 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][4][0]
        self.ipv6 = socket.getaddrinfo( self.hostname, 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0] 
        self.subnet = 'N/A'
        self.gateway = 'N/A'

        # Network Adapters
        self.networkAdapters = psutil.net_if_addrs()
    
    def returnIPConfiguration( self ):
        # Return list of network adapter configuration
        return [
            self.networkAdapter,
            self.hostname,
            self.ipv4,
            self.ipv6,
            self.subnet,
            self.gateway
        ]

    def returnNetworkAdapters( self ):
        # Return a list of Network Adapters
        return self.networkAdapters