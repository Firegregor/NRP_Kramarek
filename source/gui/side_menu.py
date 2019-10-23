import config
import tkinter as tk
import tkinter.ttk as ttk


class SideMenu(ttk.Frame):
    def __init__(self, master):
        self.master = master
        super(Main_Menu, self).__init__(master.mainFrame)
