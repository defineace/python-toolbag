from tkinter import *
from guiTabExplorer import *
from guiTabNetwork import *

class guiWindow:
    def __init__( self, root, window_width, window_height ):
        # Init tkinter gui window
        self.root = root    
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        self.guiTabExplorer = guiTabExplorer( self.root )
        # self.guiTabNetwork = guiTabNetwork( self.root )

        self.root.mainloop()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
windowRoot = Tk()
windowRoot.minsize(WINDOW_WIDTH,WINDOW_HEIGHT)

if __name__ == '__main__':
    guiWindow( windowRoot, WINDOW_WIDTH, WINDOW_HEIGHT )