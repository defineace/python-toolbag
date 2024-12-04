import socket
import psutil

class networkManager:
    def __init__( self ):
        # Network Configuration
        self.hostname = socket.gethostname()
        self.ipv4 = socket.getaddrinfo( self.hostname, 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][4][0]
        self.ipv6 = socket.getaddrinfo( self.hostname, 80, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0] 
        self.subnet = ''
        self.gateway = ''

        # Network Adapters
        self.networkAdapters = psutil.net_if_addrs()
    
    def returnIPconfiguration( self ):
        # Return list of network adapter configuration
        return [
            self.hostname,
            self.ipv4,
            self.ipv6,
            self.subnet,
            self.gateway
        ]

    def returnNetworkAdapter( self ):
        # Return a list of Network Adapters
        return self.networkAdapters