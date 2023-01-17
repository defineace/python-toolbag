from tkinter import *
from component_tab_explorer import *
from component_tab_network import *

root = Tk()

root.minsize(1100, 600)

tabList = []

def clearTab():
    for tab in tabList:
        tab.destroy()

def tabExplorer():
    clearTab()
    tab = Frame(root)
    tabList.append(tab)
    tab.pack()
    tab_explorer(tab)


def tabNetwork():
    clearTab()
    tab = Frame(root)
    tabList.append(tab)
    tab.pack()
    tab_network(tab)

def main():

    navbar = Frame(root)
    navbar.pack()

    explorer_button = Button(navbar, text="Directory Explorer", command=tabExplorer)
    explorer_button.grid(row=0, column=0)

    network_button = Button(navbar, text="Network Tools", command=tabNetwork)
    network_button.grid(row=0, column=2)

    root.mainloop()


if __name__ == '__main__':   
    main()