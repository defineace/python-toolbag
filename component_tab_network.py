from tkinter import *
from component_network_header import *

class tab_network:
    def __init__(self, root):
        self.root = root

        # Frames
        frame_network_header = Frame(self.root)
        frame_network_header.pack(padx=10, pady=10)


        self.network_header = network_header(frame_network_header)