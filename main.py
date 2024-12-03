from tkinter import *
from guiTabExplorer import *

class guiWindow:
    def __init__( self, root ):
        # Init tkinter gui window
        self.root = root
        self.guiTabExplorer = guiTabExplorer( self.root )
        self.root.mainloop()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
windowRoot = Tk()
windowRoot.minsize(WINDOW_WIDTH,WINDOW_HEIGHT)

if __name__ == '__main__':
    guiWindow( windowRoot )