# -*- coding: utf-8 -*-
import logging
import tkinter as tk
from tkinter import ttk
from src.gui.interface import NrpViev


class TkViev(NrpViev):
    """
    Viev for NRP using tkinter
    """

    config = {"General": {
                'resolurion': "600x800",
                'scale': '1',
                'padding': '10',
                'background color': 'lightgrey'},
              'Model': {
                'min temperature':'35.6',
                'days offset': '0'}}

    def __init__(self, set_config):
        self.root = tk.Tk()
        self.apply_config()
        self.set_config = set_config

    @classmethod
    def welcome(cls, model_load):
        logging.info("welcome method called")
        window = tk.Tk()
        window.title("Witamy w NRP")
        PADDING = int(cls.config['General']['padding'])
        BG = cls.config['General']['background color']
        window.configure(background=BG);
        tk.Label(window,
            text="Witamy, Z kim mamy dzisiaj przyjemność?",
            bg=BG
            ).grid(row=0, columnspan=4, padx=PADDING, pady=PADDING)
        tk.Label(window,
            text = "Imię:",
            bg=BG
            ).grid(row=1, column=1)
        name_entry = tk.Entry(window)
        name_entry.grid(row=1, column=2)
        def clicked(*_):
            logging.info(f'function called with args: {_}')
            name = name_entry.get()
            logging.debug( "Welcome " + name)
            window.destroy()
            logging.debug('window quit')
            model_load(name)
        window.bind('<Return>', clicked)
        ttk.Button(window,
            text="Ustawienia",
            command=cls.config_screen,
            ).grid(row=2, column=1, padx=PADDING, pady=PADDING)
        ttk.Button(window,
            text="Zaczynamy",
            command=clicked,
            ).grid(row=2, column=2, padx=PADDING, pady=PADDING)
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
        PADDING = int(cls.config['General']['padding'])/2
        BG = cls.config['General']['background color']
        window.title("Config")
        window.configure(background=BG);
        params = {}
        for name in cls.config:
            logging.debug(f"loading {name}")
            frame = ttk.LabelFrame(window, text=name)
            params[name] = {key: ttk.Entry(frame) for key in cls.config[name]}
            logging.debug('params cleated')
            for i, (key, val) in enumerate(params[name].items()):
                tk.Label(frame, text=key, bg=BG).grid(row=i, column=0, padx=PADDING, pady=PADDING)
                val.insert(0,cls.config[name][key])
                val.grid(row=i, column=1,padx=PADDING, pady=PADDING)
            logging.debug("params displayed")
            frame.pack(fill=tk.BOTH)
        def default(*args):
            logging.info(f"default reload")
            cls.default_config()
            for key,val in cls.config.items():
                params[key].delete(0,tk.END)
                params[key].insert(0,val)
        def done(*args):
            logging.info(f"close config window")
            window.destroy()
        def save(*_):
            logging.info(f"saving configuration")
            cls.config = {name:{k:val.get() for k,val in part.items()} for name,part in params.items()}
            done()
        ttk.Button(window ,text="Default", command=default).pack()
        ttk.Button(window ,text="Ok", command=save).pack(side=tk.LEFT)
        ttk.Button(window ,text="Cancel", command=done).pack(side=tk.RIGHT)
        window.mainloop()

    def config_apply(self, config=None):
        if config is not None:
            self.config = config

    def draw_card(self, config):
        pass

