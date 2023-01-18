from tkinter import *
from component_tab_directoryExplorer import *
from component_tab_network import *

mainRoot = Tk()
mainRoot.minsize(1100, 600)

class AppMainLoop:
    def __init__(self, root):
        # Variables
        self.root = root
        
        # Widget Root
        self.frame_tab = Frame(self.root)
        self.frame_tab.pack()

        self.navbar = Frame(self.root)
        self.navbar.pack()
        
        # Widgets
        explorer_button = Button(self.navbar, text="Directory Explorer", command=self.tab_DirectoryExplorer)
        explorer_button.grid(row=0, column=0)

        network_button = Button(self.navbar, text="Network Tools", command=self.tab_Network)
        network_button.grid(row=0, column=2)

        self.tab_DirectoryExplorer()

        # Render
        root.mainloop()

    def tab_DirectoryExplorer(self):
        # Widget Root
        self.frame_tab.destroy()
        self.frame_tab = Frame(self.root)
        self.frame_tab.pack()

        # Render Directory Explorer Tab
        tab_directoryExplorer(self.frame_tab)

    def tab_Network(self):
        # Widget Root
        self.frame_tab.destroy()
        self.frame_tab = Frame(self.root)
        self.frame_tab.pack()
        
        # Render Network tab
        tab_network(self.frame_tab)

if __name__ == '__main__':   
    AppMainLoop(mainRoot)