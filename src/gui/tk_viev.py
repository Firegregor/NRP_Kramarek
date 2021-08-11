# -*- coding: utf-8 -*-
import logging
import tkinter as tk
from tkinter import ttk
from src.gui.interface import NrpViev


class TkViev(NrpViev):
    """
    Viev for NRP using tkinter
    """

    config = {"test": "testvalue", 'test2': 'testva;ue2'}

    def __init__(self):
        self.root = tk.Tk()
        self.default_config()

    @classmethod
    def welcome(cls, model_load):
        logging.info("welcome method called")
        window = tk.Tk()
        window.title("Witamy w NRP")
        window.configure(background = "lightgrey");
        tk.Label(window ,text = "Name").grid(row = 0,column = 0)
        name_entry = tk.Entry(window)
        name_entry.grid(row = 0,column = 1)
        def clicked(*_):
            logging.info(f'function called with args: {_}')
            name = name_entry.get()
            logging.debug( "Welcome " + name)
            window.destroy()
            logging.debug('window quit')
            model_load(name)
        window.bind('<Return>', clicked)
        ttk.Button(window ,text="Config", command=cls.config_screen).grid(row=1,columnspan=2)
        ttk.Button(window ,text="Submit", command=clicked).grid(row=2,columnspan=2)
        window.mainloop()


    def mainloop(self):
        logging.debug('TkViev mainloop starts')
        self.root.mainloop()

    @classmethod
    def default_config(cls):
        pass

    def welcome_screen(self, config_callback, user_callback):
        pass

    @classmethod
    def config_screen(cls):
        logging.info("Config screen start")
        window = tk.Tk()
        window.title("Config")
        window.configure(background = "lightgrey");
        frame = ttk.LabelFrame(window, text='Config')
        params = {key: ttk.Entry(frame) for key in cls.config}
        logging.debug('params cleated')
        def default(*args):
            cls.default_config()
            for key,val in cls.config.items():
                params[key].delete(0,tk.END)
                params[key].insert(0,val)
        def done(*args):
            window.destroy()
        def save(*_):
            cls.config = {k:val.get() for k,val in params.items()}
            done()
        for i, (key, val) in enumerate(params.items()):
            tk.Label(frame, text=key).grid(row=i, column=0)
            val.insert(0,cls.config[key])
            val.grid(row=i, column=1)
        logging.debug("params displayed")
        frame.pack(fill=tk.BOTH)
        ttk.Button(window ,text="Default", command=default).pack()
        ttk.Button(window ,text="Ok", command=save).pack(side=tk.LEFT)
        ttk.Button(window ,text="Cancel", command=done).pack(side=tk.RIGHT)
        window.mainloop()

    def config_apply(self, config=None):
        if config is not None:
            self.config = config

    def draw_card(self, config):
        pass

