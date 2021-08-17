import logging
import tkinter as tk
from tkinter import ttk


class CycleScreen(ttk.LabelFrame):
    """
    Frame with cycle viev
    """

    CANVAS = ['width', 'height', 'bg']

    def __init__(self, master, config, data, *args, **kwargs):
        self.data = data
        self.config = config
        super().__init__(master,text=data.get_name(), *args, **kwargs)
        self.display = None
        self.update()

    def update(self):
        self.blank()
        self.display.pack_forget()
        self.draw_data()
        self.display.pack()

    def blank(self):
        """
        Draws blank cycle card based on configuration
        """
        if self.display is not None:
            self.display.pack_forget()
        self.display = tk.Canvas(self, **self.canvas_config)

    @property
    def canvas_config(self):
        return {key: val for key,val in self.config.items() if key in self.CANVAS}

    def set_rgb(self, r, g, b):
        self._str = None
        self.R, self.G, self.B = r, g, b
        self.update()

    def draw_data(self):
        pass

    def __str__(self):
        return f"Frame containing cycle viev"


