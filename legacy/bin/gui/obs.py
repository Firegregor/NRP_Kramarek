import tkinter as tk
import tkinter.ttk as ttk
import datetime as dt
import res
from contextlib import contextmanager
from gui.blank import BlankCard
from gui.main_menu import MainMenu
from gui.card_menu import CardMenu
from res.storage import Person


class Obs(tk.Frame):
    """Wyświetlanie kart obserwacji cykli wg metody dr Kramarek"""
    def __init__(self, master):
        self.__master = master
        self.displayed = []
        self.card = None
        self.menu = None
        self.day = [tk.IntVar() for _ in range(3)]

        super(Obs, self).__init__(master, width=1200, height=600, bg='white')
        self.display_menu()
        self.pack()

    def display_menu(self):  #TODO: osobna klasa na menu i manager
        self.displayed.append(MainMenu(self))
        self.displayed[-1].grid()

    @contextmanager
    def blanked(self):
        person = Person(self.displayed[0].get(), dt.date(*[x.get() for x in self.day]))
        for widget in self.displayed:
            widget.grid_forget()
        self.card = BlankCard(self, person)
        self.card.grid()
        self.menu = CardMenu(self)
        yield
        self.displayed = [self.card, self.menu]
        self.menu.grid(row=0, column=1)


    def observation(self):
        with self.blanked():
            pass

    def add_day(self):
        temp = self.menu.current_temp.get()
        day = self.menu.day.get() - 1
        obj = self.menu.objaw.get()
        msg = self.menu.msg.get()
        self.menu.day.set(day + 2)
        self.card.add_param(temp=temp, obj=obj, day=day, msg=msg)

    def add_temp(self):
        temp = self.menu.current_temp.get()
        day = self.menu.day.get() - 1
        self.menu.day.set(day + 2)
        self.card.add_param(temp=temp, day=day)

    def add_obj(self):
        day = self.menu.day.get() - 1
        obj = self.menu.objaw.get()
        self.menu.day.set(day + 2)
        self.card.add_param(obj=obj, day=day)

    def add_msg(self):
        day = self.menu.day.get() - 1
        msg = self.menu.msg.get()
        self.menu.day.set(day + 2)
        self.card.add_param(msg=msg, day=day)

    def finish_cycle(self):
        day = self.menu.day.get() - 1
        self.card.finish(day)
        self.menu.current_cycle.set('Cykl {}'.format(self.card.person.cycle_nr))

    def previous(self):
        self.card.person.previous()
        self.menu.current_cycle.set('Cykl {}'.format(self.card.person.cycle_nr))
        self.card.update_canvas()

    def next(self):
        self.card.person.next()
        self.menu.current_cycle.set('Cykl {}'.format(self.card.person.cycle_nr))
        self.card.update_canvas()

    def save(self):
        self.card.person.save()

    def cwiczenia(self):
        with self.blanked():
            self.menu = tk.Label(self, text='Wybrałeś cwiczenia')
            ttk.Button(self.menu, text='rysuj', command=self.card.add_param).grid()
            ttk.Button(self.menu, text='wyczyść', command=self.card.blank).grid()
