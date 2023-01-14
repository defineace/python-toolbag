from tkinter import *
from component_explorer import *
from component_network import *

root = Tk()

def main():

    navbar = Frame(root)
    navbar.pack()

    explorer_button = Button(navbar, text="Directory Explorer", command= lambda: tab_explorer(root))
    explorer_button.grid(row=0, column=0)

    network_button = Button(navbar, text="Network Tools", command= lambda: tab_network(root))
    network_button.grid(row=0, column=2)

    root.mainloop()


if __name__ == '__main__':   
    main()