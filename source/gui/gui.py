# -*- coding: utf-8 -*-
import tkinter as tk
import config
from source.gui.main_menu import Main_Menu
from source.gui.side_menu import Side_Menu
from source.gui.card import Card


"""
Klasa odpowiedzialna za rysowanie calosci programu
"""
class Gui:
    def __init__(self, verbose=False):
        print("init Gui")
        root = tk.Tk()
        self._rooot = root
        root.geometry(config.config['geometry'])
        self.mainFrame = tk.Frame(root)
        self.mainFrame.pack()

        self.main = Main_Menu(self)
        self.main.grid()

        self.card = Card(self)
        self.side_menu = SideMenu(self)
        root.mainloop()

    def CardInit(self):
        self.main.grid_forget()
        self.card.grid(row=0, column=0)
        self.side_menu.grid(row=0, column=1)

    def update(self):
        self.card.update()
        self.side_menu.update()

    def card_update(self):
        self.blank()
        self.draw_numbers()
        self.draw_data()
        self.draw_interpretation()

    def blank(self):
        """
        Rysowanie pustej karty
        """
        pass

    def draw_numbers(self):
        """
        Rysowanie zakresu temperatur
        """
        pass

    def draw_data(self):
        """
        Rysowanie temperatury, objawow, dat, numeru cyklu, numerow dni
        """
        pass

    def draw_interpretation(self):
        """
        Rysowanie naniesionej interpretacji
        """
        pass

