# -*- coding: utf-8 -*-
import logging
import tkinter as tk
from tkinter import ttk
from src.gui.interface import NrpViev
from src.gui.tk_config import ConfigScreen
from src.gui.tk_cycle import CycleScreen


class TkViev(NrpViev):
    """
    Viev for NRP using tkinter
    """

    config = {}
    initialized = False
    cycle = None

    @classmethod
    def welcome(cls, model_load):
        logging.info("welcome method called")
        if not cls.config:
            logging.debug("set default configuration")
            cls.config_apply()
        window = tk.Tk()
        window.title("Witamy w NRP")
        PADDING = int(cls.config['General']['padding'])
        BG = cls.config['Colors']['background']
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

    @classmethod
    def default_config(cls):
        return ConfigScreen.get_defaults()

    @classmethod
    def config_screen(cls, *_, cycle=None):
        logging.info("Config screen start - cycle={cycle}")
        window = tk.Tk()
        window.title("Config")
        ConfigScreen(window, cls.config, cls.config_apply, cycle)
        window.mainloop()

    @classmethod
    def config_apply(self, config=None):
        logging.info(f'Config apply')
        logging.debug(f'config={config}')
        logging.debug(f'cycle={self.cycle}')
        if config is None:
            self.config = self.default_config()
        else:
            self.config = config
        if self.initialized:
            self.root.configure(background=self.config['Colors']['background'])
            self.root.geometry(self.config['General']['geometry'])

    def __init__(self, set_config):
        self.root = tk.Tk()
        #self.root.geometry('1000x1000')
        self.initialized = True
        self.set_config = set_config

    def mainloop(self):
        logging.debug('TkViev mainloop starts')
        self.root.mainloop()

    def draw_card(self, data, name):
        self.root.title(name)
        self.cycle = CycleScreen(self.root, self.config['Cycle'], data)
        self.cycle.pack(side=tk.LEFT)
        ttk.Button(text='Config', command=lambda: self.config_screen(cycle=self.cycle)).pack(side=tk.LEFT)



