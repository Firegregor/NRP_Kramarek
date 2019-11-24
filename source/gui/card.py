import config
import datetime as dt
import tkinter as tk
import tkinter.ttk as ttk

# TODO: From config import params
top = 20
monthspace = 20
off_x = 100
field_width = 20
field_height = 30
off_y = top + monthspace
bottom = off_y + 13 * field_height
month = {x+1: y for x, y in enumerate(['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec',
                                       'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień'])}
config.params["visible day"] = 5
config.params["cycle start"] = dt.datetime.now()
config.params["card"] = {'canvas':(1000, 600)}


class Card(ttk.LabelFrame):
    def __init__(self, gui):
        self.gui = gui
        super(Card, self).__init__(gui.mainFrame)
        self.display = None
        self.Log("init done")

    def update(self):
        self.Log("update started")
        if self.display is not None:
            self.display.pack_forget()
        width, heigth = config.params["card"]['canvas']
        self.display = tk.Canvas(self, width=width, height=heigth, bg='white')
        self.blank()
        self.draw_numbers()
        self.draw_data()
        self.draw_interpretation()
        self.display.pack()
        self.Log("update done")

    def blank(self):
        """
        Rysowanie pustej karty
        """
        self.Log("Blank started")
        # tekst data
        self.display.create_text(off_x-10, off_y-10, text='Data', anchor=tk.NE)
        # Linie daty
        self.display.create_line(top, top, off_x + 40 * field_width, top, width=2)
        self.display.create_line(top, off_y + field_height, off_x + 40 * field_width, off_y + field_height, width=2)
        self.display.create_line(off_x, off_y, off_x + 40 * field_width, off_y, width=2)
        self.display.create_text(off_x + 0.5 * field_width, top + 0.3 * field_height, text=month[5], anchor=tk.W) # TODO: Make months from cycle module
        # widoczne dni
        for x in range(40):
            if 0:#self.master.menu:
                if x == self.master.menu.day.get() - 1:
                    self.display.create_rectangle(off_x + x * field_width, bottom + field_height,
                                                  off_x + (x + 1) * field_width, bottom + 2 * field_height, fill='green')
            self.display.create_line(off_x + x * field_width, off_y,
                                     off_x + x * field_width, 580)
        self.display.create_line(off_x, 20, off_x, 580, width=2)
        self.display.create_line(off_x + 40 * field_width, top, off_x + 40 * field_width, 580, width=2)
        # linie temperatury i dni cyklu
        for level in range(16):
            self.display.create_line(off_x, off_y + level * field_height, off_x + 40 * field_width,
                                     off_y + level * field_height, width = (level//14+1))
        self.Log("Blank done")

    def draw_numbers(self):
        """
        Rysowanie zakresu temperatur i dni miesiąca
        """
        self.Log("Numbers started")
        for cycle_day in range(config.params["visible day"], config.params["visible day"] + 40):
            x= cycle_day - config.params["visible day"] + 1
            self.display.create_text(off_x + (x-0.5) * field_width,
                                     bottom + 1.5 * field_height, text=cycle_day)
            # Dni miesiąca
            day = config.params["cycle start"] + dt.timedelta(days=x - 1)
            if x % 2:
                self.display.create_text(off_x + (x - 0.5) * field_width,
                                         top + 1.1 * field_height, text=str(day.day))
            if 5 <= day.weekday() <= 6:
                self.display.create_line(off_x + x * field_width, off_y, off_x + x * field_width,
                                         off_y + field_height, width=2)

    def draw_data(self):
        """
        Rysowanie temperatury, objawow, dat, numeru cyklu, numerow dni
        """
        self.Log("Data started")

    def draw_interpretation(self):
        """
        Rysowanie naniesionej interpretacji
        """
        self.Log("Interpretation started")

    def Log(self, msg):
        if self.gui.verbose:
            print(type(self), msg)

