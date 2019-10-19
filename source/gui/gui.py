# -*- coding: utf-8 -*-
import tkinter as tk


"""
Klasa odpowiedzialna za rysowanie calosci programu
"""
class Gui:
    def __init__(self, verbose=False):
        print("init Gui")
        root = tk.Tk()
        self._rooot = root
        self.main = Main_Menu(root,self)
        self.card = Card(root,self)
        self.side_menu = SideMenu(root,self)
        root.geometry(res.config['geometry'])
        root.mainloop()

    def CardInit(self):
        self.main.hide()
        self.card.show()
        self.side_menu.show()

    def update(self):
        self.main.update()
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

