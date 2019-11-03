import config
import tkinter as tk
import tkinter.ttk as ttk


class SideMenu(ttk.Frame):
    def __init__(self, master):
        self.gui = master
        super(SideMenu, self).__init__(master.mainFrame)
        self.Log("init started")
        self.Log("init done")
        
    def update(self):
        self.Log("update started")
        self.Log("update done")

    def Log(self, msg):
        if self.gui.verbose:
            print(type(self), msg)

