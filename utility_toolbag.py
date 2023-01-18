from tkinter import *
from component_tab_directoryExplorer import *
from component_tab_network import *

mainRoot = Tk()
mainRoot.minsize(1100, 600)

class AppMainLoop:
    def __init__(self, root):
        # Variables
        self.root = root
        self.tabs_frameList = []
        
        # Widget Root
        navbar = Frame(self.root)
        navbar.pack()
        # Widgets
        explorer_button = Button(navbar, text="Directory Explorer", command=self.tab_DirectoryExplorer)
        explorer_button.grid(row=0, column=0)

        network_button = Button(navbar, text="Network Tools", command=self.tab_Network)
        network_button.grid(row=0, column=2)

        self.tab_DirectoryExplorer()

        # Render
        root.mainloop()

    def clearTab(self):
        for frame in self.tabs_frameList:
            frame.destroy()

    def tab_DirectoryExplorer(self):
        self.clearTab()
        
        # Widget Root
        frame_tab = Frame(self.root)
        frame_tab.pack()
        self.tabs_frameList.append(frame_tab)

        # Render Directory Explorer Tab
        tab_directoryExplorer(frame_tab)

    def tab_Network(self):
        self.clearTab()

        # Widget Root
        frame_tab = Frame(self.root)
        frame_tab.pack()
        self.tabs_frameList.append(frame_tab)
        
        # Render Network tab
        tab_network(frame_tab)



if __name__ == '__main__':   
    AppMainLoop(mainRoot)