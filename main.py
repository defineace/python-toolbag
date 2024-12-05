from tkinter import *
from guiTabExplorer import *
from guiTabNetwork import *

class guiWindow:
    def __init__( self, root, window_width, window_height ):
        # Init tkinter gui window
        self.root = root    
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        self.frame_window = Frame( self.root )
        self.frame_window.pack()

        self.displayNavbar()
        guiTabExplorer( self.frame_window )

        self.root.mainloop()

    def displayNavbar( self ):
        self.frame_navbar = Frame( self.frame_window )
        self.frame_navbar.pack()

        self.button_tabExplorer = Button( self.frame_navbar, text="Explorer", width=20, command= lambda: self.actionNavbarButton(0))
        self.button_tabNetwork = Button( self.frame_navbar, text="Network Manager", width=20, command= lambda: self.actionNavbarButton(1))

        self.button_tabExplorer.grid( row=0, column=0 )
        self.button_tabNetwork.grid( row=0, column=1 )

    def actionNavbarButton( self, action ):
        self.frame_window.destroy()
        self.frame_window = Frame( self.root )
        self.frame_window.pack()
        self.displayNavbar()
        
        if action == 0:
            guiTabExplorer( self.frame_window )
            
        elif action == 1:
            guiTabNetwork( self.frame_window )
        


####################################################################
####################################################################
# Main
####################################################################
####################################################################

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
windowRoot = Tk()
windowRoot.minsize(WINDOW_WIDTH,WINDOW_HEIGHT)

if __name__ == '__main__':
    guiWindow( windowRoot, WINDOW_WIDTH, WINDOW_HEIGHT )