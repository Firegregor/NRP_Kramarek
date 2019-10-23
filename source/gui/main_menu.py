# -*- coding: utf-8 -*-
import config
import datetime as dt
import tkinter as tk
import tkinter.ttk as ttk


class MainMenu(ttk.Labelframe):

    def __init__(self, master):
        self.master = master
        super(MainMenu, self).__init__(master.mainFrame)

        self.name = ttk.Entry(self)
        self.name.grid(row=4, column=3, sticky='nswe', columnspan=2)
        self.name.insert(0, config.params['name'])

        self.button1 = ttk.Button(self, text='Start', command=master.CardInit)
        self.button1.grid(row=1, column=2, columnspan=3)
        tk.Label(self, text='Wprowadzenie własnych obserwacji', bg='white').grid(row=2, column=2, sticky='nswe', columnspan=3)
        tk.Label(self, text='Imię', bg='white').grid(row=4, column=2, sticky='nswe', )
        tk.Label(self, text='Dzień rozpoczęcia cyklu', bg='white').grid(row=5, column=2, sticky='nswe', columnspan=3)

        self.day = []
        self._day = [tk.IntVar() for _ in range(3)]
        self.day.append(tk.Spinbox(self, textvariable=self._day[2], from_=1, to=31, increment=1, width=5))
        self.day.append(tk.Spinbox(self, textvariable=self._day[1], from_=1, to=12, increment=1, width=5))
        self.day.append(tk.Spinbox(self, textvariable=self._day[0], from_=1990, to=2040, increment=1, width=5))
        self.day[0].grid(row=6, column=2)
        self.day[1].grid(row=6, column=3)
        self.day[2].grid(row=6, column=4)
        [self._day[i].set(y) for i, y in enumerate([dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day])]

    def get_name(self):
        return self.name.get()

    def get_day(self):
        pass
