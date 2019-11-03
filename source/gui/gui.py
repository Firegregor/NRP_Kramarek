# -*- coding: utf-8 -*-
import tkinter as tk
import config
from source.gui.main_menu import MainMenu
from source.gui.side_menu import SideMenu
from source.gui.card import Card


"""
Klasa odpowiedzialna za rysowanie calosci programu
"""
class Gui:
    def __init__(self, verbose=False):
        self._verbose = verbose
        root = tk.Tk()
        self._rooot = root
        root.geometry(config.params['geometry'])
        self.mainFrame = tk.Frame(root)
        self.mainFrame.pack()

        self.Log("init Gui")
        self.main = MainMenu(self)
        self.Log("MainMenu init done")
        self.main.grid()
        self.Log("MainMenu on board")

        self.card = Card(self)
        self.side_menu = SideMenu(self)
        root.mainloop()

    def CardInit(self):
        self.main.grid_forget()
        self.card.grid(row=0, column=0)
        self.side_menu.grid(row=0, column=1)
        self.update()

    def update(self):
        self.card.update()
        self.side_menu.update()

    @property
    def verbose(self):
        return self._verbose

    def Log(self, msg):
        if self._verbose:
            print(type(self), msg)
