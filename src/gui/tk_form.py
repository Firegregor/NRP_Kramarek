# -*- coding: utf-8 -*-
import logging
import tkinter as tk
from tkinter import ttk



class FormScreen(tk.Frame):
    """
    Form fot inserting data like comments and symptoms
    """

    def __init__(self, master, config, data, *args, **kwargs):
        self.data = data
        super().__init__(master,text=data.get_name(), *args, **kwargs)
        self.display = None
        self.update(config=config)

    def draw_burttons():
        pass


