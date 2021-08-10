# -*- coding: utf-8 -*-
import tkinter as tk
from src.gui.interface import NrpViev


class TkViev(NrpViev):
    """
    Viev for NRP using tkinter
    """

    config = {}

    def __init__(self):
        self.root = tk.Tk()
        self.default_config()
        self.root.mainloop()

    def default_config(self):
        pass

    def welcome_screen(self, config_callback, user_callback):
        pass

    def config_screen(self):
        pass

    def draw_card(self, config):
        pass

