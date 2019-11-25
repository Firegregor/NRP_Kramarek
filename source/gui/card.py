import config
import datetime as dt
import tkinter as tk
import tkinter.ttk as ttk

# TODO: From res import cycle
top = 20
monthspace = 20
off_x = 100
field_width = 20
field_height = 30
off_y = top + monthspace
bottom = 580
month = {x+1: y for x, y in enumerate(['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec',
                                       'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień'])}
config.params["visible day"] = 5
config.params["selected day"] = 15
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

        # widoczne dni
        for x in range(40):
            self.display.create_line(off_x + x * field_width, off_y,
                                     off_x + x * field_width, 580)
        self.display.create_line(off_x, top, off_x, bottom, width=2)
        self.display.create_line(off_x + 40 * field_width, top, off_x + 40 * field_width, bottom, width=2)

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
            # index pomocniczy
            x= cycle_day - config.params["visible day"] + 1

            # zaznaczenie obecnie wybranego dnia
            if cycle_day == config.params["selected day"]+1:
                self.display.create_rectangle(off_x + x * field_width, off_y,
                                              off_x + (x + 1) * field_width, bottom, fill='gray80')
                # naprawa zasłoniętych lini
                for y in range(16):
                    if y==1 or y>13:
                        self.display.create_line(off_x + x * field_width, off_y+y*field_height,
                            off_x + (x + 1) * field_width, off_y+y*field_height, width=2)
                    else:
                        self.display.create_line(off_x + x * field_width, off_y+y*field_height,
                            off_x + (x + 1) * field_width, off_y+y*field_height, width=1)

            # Wyświetl dzień cyklu na dolnej osi
            self.display.create_text(off_x + (x-0.5) * field_width,
                                     bottom - 3.5 * field_height, text=cycle_day)
            # Dni miesiąca
            day = config.params["cycle start"] + dt.timedelta(days=cycle_day - 1)
            if x % 2:
                self.display.create_text(off_x + (x - 0.5) * field_width,
                                         top + 1.1 * field_height, text=str(day.day))
            # Niedziele
            if 5 <= day.weekday() <= 6:
                self.display.create_line(off_x + x * field_width, off_y, off_x + x * field_width,
                                         off_y + field_height, width=2)
            if (1 == day.day and 4 <= x and x <= 38) or 1 == x:
                self.display.create_text(off_x + (x-0.5) * field_width, top + 0.3 * field_height, text=month[day.month], anchor=tk.W) 

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

