from tkinter import *
from tkinter import ttk


import HomePage

if __name__ == '__main__':
    # Getting the screensize in list.
    ls = list([1336, 714])
    print(ls)
    # Creating a fixed window.
    root = Tk()

    # Creating a bit icon.
    '''
    root.iconbitmap('icon.ico')
'''
    # Title and Screen Setting.
    root.title("Vehicle Sales and service")  # Sets-up the title of the window.
    root.geometry(f"{ls[0]}x{ls[1]}+0+0")  # Width Height Left-padding Top-padding.
    root.minsize(ls[0], ls[1])  # Locking min-sized window.
    root.maxsize(ls[0], ls[1])  # Locking max-sized window.
    root.configure(bg='#163148')  # Setting the background.

    # Starting the first window.
    firster = HomePage.Main_Page(root, ls)

    # Starting a main window.
    root.mainloop()
