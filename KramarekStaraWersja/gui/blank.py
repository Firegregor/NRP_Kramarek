import tkinter as tk
import tkinter.ttk as ttk
import datetime as dt
from res.storage import Person
from res import config

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


class BlankCard(ttk.Labelframe):
    def __init__(self, master, person=Person("Kasia")):
        self.person = person
        super(BlankCard, self).__init__(master, text=self.person.name)
        self.pack()
        self.display = None
        self.update_canvas()

    @property
    def temp(self):
        return self.person.cycle['temperature']

    @property
    def obs(self):
        return self.person.cycle['observation']

    @property
    def msg(self):
        return self.person.cycle['comments']

    @property
    def start(self):
        return self.person.date

    def mouse_1(self, event):
        if config["verbose"]:
            print('mysza na pozycji: {} x {}'.format(event.x, event.y))
        if off_x + 40 * field_width < event.x:
            pass
        elif event.x < off_x:
            self.person.change_place()
        else:
            day = (event.x - off_x) // field_width
            if event.y < off_y + field_height:
                self.person.act(day, 'akty')
            elif event.y > bottom:
                self.person.act(day, 'bo')
            else:
                temp = 375 - (event.y - off_y + field_height // 3) // field_height
                if self.person.active:
                    if config["verbose"]:
                        print('dostępny - Dzień:{}, temperatura:{}'.format(day, temp))
                    self.add_param(temp=temp, day=day)
                else:
                    if config["verbose"]:
                        print('niedostępny - Dzień:{}, temperatura:{}'.format(day, temp))
        self.update_canvas()


    def blank(self):
        """
        Odświeżanie karty
        """
        if self.display is not None:
            self.display.pack_forget()
        self.display = tk.Canvas(self, width=1000, height=600, bg='white')
        self.display.bind('<ButtonPress-1>', self.mouse_1)
        self.display.bind('<Key>', self.keyboard_handler)
        self._draw_tab()
        self.display.pack()

    def _draw_tab(self):
        """
        Rysowanie pustej karty
        """
        # tekst data
        self.display.create_text(off_x-10, off_y-10, text='Data', anchor=tk.NE)
        # Linie daty
        self.display.create_line(top, top, off_x + 40 * field_width, top, width=2)
        self.display.create_line(top, off_y + field_height, off_x + 40 * field_width, off_y + field_height, width=2)
        self.display.create_line(off_x, off_y, off_x + 40 * field_width, off_y, width=2)
        self.display.create_text(off_x + 0.5 * field_width, top + 0.3 * field_height, text=month[self.start.month], anchor=tk.W)
        # Tabela pion + numeracja dni
        for x in range(1, 41):
            if self.master.menu:
                if x == self.master.menu.day.get() - 1:
                    self.display.create_rectangle(off_x + x * field_width, bottom + field_height,
                                                  off_x + (x + 1) * field_width, bottom + 2 * field_height, fill='green')
            self.display.create_line(off_x + x * field_width, off_y,
                                     off_x + x * field_width, 580)
            self.display.create_text(off_x + (x-0.5) * field_width,
                                     bottom + 1.5 * field_height, text=x)
            day = self.start + dt.timedelta(days=x - 1)
            if x % 2:
                self.display.create_text(off_x + (x - 0.5) * field_width,
                                         top + 1.1 * field_height, text=str(day.day))
            if 5 <= day.weekday() <= 6:
                self.display.create_line(off_x + x * field_width, off_y, off_x + x * field_width,
                                         off_y + field_height, width=2)
        self.display.create_line(off_x, 20, off_x, 580, width=2)
        # Tabela poziom + oznaczenie temperatury
        for x, s in enumerate([2, 3, 4, '36,5', 6, 7, 8, 9, '37,0', 1, 2, 3]):
            self.display.create_line(off_x, bottom - x*field_height,
                                     off_x + 40 * field_width, bottom - x * field_height)
            self.display.create_text(off_x-5, bottom - x*field_height, anchor=tk.E, text=s)
        # Dni Cyklu
        self.display.create_line(top, bottom + field_height, off_x + 40 * field_width,
                                 bottom + field_height, width=2)
        self.display.create_text(top + 10, bottom + 1.5 * field_height, text='DNI CYKLU', anchor=tk.W)
        # Śluz szyjkowy
        self.display.create_line(top, bottom + 2 * field_height, off_x + 40 * field_width,
                                 bottom + 2 * field_height, width=2)
        self.display.create_text(top + 10, bottom + 2.2 * field_height,
                                 text='Śluz\nszyjkowy:\nodczucie\nwygląd\nilość', anchor=tk.NW)
        # Owale
        self._draw_oval(50, 400, 'Godzina', 'Miejsce')
        self.display.create_text(50,310, text=self.person.place)
        self._draw_oval(950, 500, 'Długość cyklu', 'Długość fazy\nniższej temp.')
        self._draw_oval(950, 50, 'Nr cyklu')
        # nr cyklu
        self.display.create_text(950, 50, text=self.person.cycle_nr)

    def interpret(self):
        """
        Rysowanie końca cyklu i interpretacji objawów
        """
        # długość cyklu
        x = self.person.cycle["len"]
        plo = ['jb', 'p', 'mo', 'w', 'śl', 'ol', 'r']
        if config['interpret']:
            szczyt = 0
            temp_h = 0
            finish_ov = 0
        self.display.create_text(950, 500, text='{}'.format(x))
        # oznaczenie końca na karcie
        self.display.create_line(off_x + x * field_width, off_y, off_x + x * field_width, 580, width=2)
        self.display.create_line(off_x + x * field_width, bottom + 1.5 * field_height,
                                 off_x + 40 * field_width, bottom + 1.5 * field_height)
        self.display.create_rectangle(off_x + x * field_width, off_y + field_height,
                                      off_x + (x + 1) * field_width, off_y + 2 * field_height, fill='red')
        level = self.person.cycle['special']['interpret']
        x = self.master.menu.day.get()
        for i in range(x):
            orect = [off_x + (i + 0.5) * field_width - 4, bottom + 0.6 * field_height - 4,
                     off_x + (i + 0.5) * field_width + 4, bottom + 0.6 * field_height + 4]
            color = None
            if self.obs[i] == 's':
                self.display.create_text(off_x + (i + 0.5) * field_width, bottom + 0.6 * field_height - 4, text='-')
                color = 'black'
            elif self.obs[i] and 'k' not in self.obs[i]:
                if [x for x in plo if x in self.obs[i].split()]:
                    color = 'white'
                else:
                    color = 'black'
                self.display.create_oval(*orect, width=1, fill=color)

            if config['interpret'] > 0:
                if color == 'white':
                    if szczyt >= -1:
                        szczyt = i
                elif color is not None:
                    if szczyt > 0 :
                        szczyt = -4
                        field = (i - 0.5) * field_width
                        self.display.create_line(off_x + field - 6,
                                                 bottom + 0.6 * field_height - 6,
                                                 off_x + field + 6,
                                                 bottom + 0.6 * field_height + 6)
                        self.display.create_line(off_x + field - 6,
                                                 bottom + 0.6 * field_height + 6,
                                                 off_x + field + 6,
                                                 bottom + 0.6 * field_height - 6)
                if szczyt < -1:
                    self.display.create_text((orect[0] + orect[2]) / 2, orect[1], text='{}'.format(5 + szczyt), anchor='s')
                    szczyt += 1
            if config['interpret'] > 1:
                if 0 > szczyt:
                    skipped = 0
                    if not temp_h:
                        if self.temp[i] > max(self.temp[i-7:i-1]):
                            skipped = 0
                            temp_h = i-1
                    else:
                        if self.temp[i] > max(self.temp[temp_h-6:temp_h]):
                            if i - temp_h - skipped == 4:
                                self.display.create_line(off_x + i * field_width, off_y, off_x + i * field_width, 580, width=2)
                                self.person.cycle['special']['interpret'] = temp_h + 2
                                temp_h = 0
                                szczyt = 0
                                skipped = 0
                        elif not skipped:
                            skipped = 1
                        else:
                            temp_h = 0
                            skipped = 0

                    if 0 < temp_h < i:
                        self.display.create_text(off_x + (i + 0.5) * field_width - 2,
                                                 bottom - (self.temp[i] - 362) * field_height - 2,
                                                 text='{}'.format(i - temp_h - skipped),
                                                 anchor='s')
        if self.person.cycle['special']['interpret'] > 1:
            self.display.create_text(950, 410, text='{}'.format(self.person.cycle['special']['interpret']))



    def finish(self, day):
        """
        Zakończ cykl w danym dniu

        :param day: dzień krwawienia
        :return:
        """
        self.person.finish_cycle(day)
        self.update_canvas()

    def keyboard_handler(self, event):
        keymap = {'Left': lambda: self.master.menu.day.set(self.master.menu.day.get()-1), 'Right': lambda: self.master.menu.day.set(self.master.menu.day.get()+1)}
        if event.keysym in keymap:
            keymap[event.keysym]()

    def add_param(self, day, temp=None, obs=None, msg=None):
        """
        Dodawanie wpisu z dnia:

        :param temp: temperatura
        :param obs: obserwacje śluzu
        :param day: dzień cyklu
        :param msg: komentarz
        """
        if temp is not None:
            if temp == self.temp[day]:
                self.temp[day] = 0
            else:
                self.temp[day] = temp
        if obs is not None:
            self.obs[day] = obs
        if msg is not None:
            self.msg[day] = msg
        self.update_canvas()

    def _draw_oval(self, x, y, msg1='', msg2=''):
        orect = [x-20, y-20, x+20, y+20]
        orect2 = [x - 20, y - 110, x + 20, y - 70]
        self.display.create_oval(*orect, width=2)
        self.display.create_oval(*orect2, width=2)
        self.display.create_text(x, y - 35, text=msg1)
        self.display.create_text(x, y - 130, text=msg2)

    def update_canvas(self):
        self.blank()
        self.display.pack_forget()

        for i, t, o, m in zip(range(40), self.temp, self.obs, self.msg):
            x = t - 362
            s = ''
            if i in self.person.cycle['special']['bo']:
                self.display.create_text(off_x + (i+0.5) * field_width, bottom + field_height / 2, text=chr(0x2666), anchor=tk.S)
            if i in self.person.cycle['special']['akty']:
                self.display.create_text(off_x + (i+0.5) * field_width, off_y + field_height, text=chr(0x2193), anchor=tk.N, font='25')
            for obs in o.split():
                if obs.isnumeric():
                    self.display.create_rectangle(off_x + i * field_width, bottom + field_height,
                                                  off_x + (i + 1) * field_width, bottom + (1 - 0.2*int(obs)) * field_height, fill='red')
                else:
                    s += obs + '\n'
            self.display.create_text(off_x + (i+0.5) * field_width, bottom + 2.2 * field_height,
                                     text=s, anchor=tk.N)
            
            if x < 6:
                self.display.create_text(off_x + (i+0.5) * field_width, off_y + 2 * field_height + 5, text=m,
                                         angle=90, anchor=tk.E)

            else:
                self.display.create_text(off_x + (i+0.5) * field_width, bottom - field_height-5, text=m,
                                         angle=90, anchor=tk.W)
    
            self.display.create_oval(off_x + (i+0.5) * field_width - 2, bottom - x*field_height - 2,
                                     off_x + (i+0.5) * field_width + 2, bottom - x*field_height + 2, width=3)
            if i and t and self.temp[i - 1]:
                x2 = self.temp[i - 1] - 362
                self.display.create_line(off_x + (i - 0.5) * field_width, bottom - x2 * field_height,
                                         off_x + (i + 0.5) * field_width, bottom - x * field_height, width=2)
            if not self.person.cycle['active']:
                self.interpret()
        self.display.pack()
