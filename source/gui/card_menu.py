import tkinter as tk
import tkinter.ttk as ttk

sqr = 15
temp_x = 5
temp_y = 5


class CardMenu(ttk.Labelframe):

    def __init__(self, master):
        super(CardMenu, self).__init__(master, text='Menu')
        self.master = master

        self.current_cycle = tk.StringVar()
        self.current_cycle.set('Cykl {}'.format(self.master.card.person.cycle_nr))
        tk.Label(self, textvariable=self.current_cycle).grid(column=1)
        ttk.Button(self, text='<<', command=self.previous, width=5).grid(row=0, column=0)
        ttk.Button(self, text='>>', command=self.next, width=5).grid(row=0, column=2)
        self.current_temp = tk.IntVar()
        self.day = tk.IntVar()
        self.day.set(1)
        maxtemp = 375
        for x in range(361, maxtemp):
            ttk.Radiobutton(self, text='{:.1f}'.format(x / 10), variable=self.current_temp,
                            value=x).grid(row=maxtemp - x, column=0)
        ttk.Label(self, text='Dzień').grid(row=1, column=1, columnspan=2)
        tk.Spinbox(self, textvariable=self.day, from_=1, to=40, increment=1,
                   width=5).grid(row=2, column=1, columnspan=2)
        ttk.Label(self, text='Objaw').grid(row=3, column=1)
        self.objaw = self.objaw_create()
        self._objaw_draw()
        self.objaw.bind('<Button-1>', self.objaw_handler)
        ttk.Label(self, text='Komentarz').grid(row=10, column=1)
        self.msg = ttk.Entry(self)
        self.msg.bind('<Key>', lambda event, entry=self.add_msg: self.keyboard_handler(event, entry))
        self.msg.grid(row=11, column=1, columnspan=2)
        ttk.Button(self, text='+', command=self.add_msg, width=5).grid(row=10, column=2)
        ttk.Label(self, text='Temperatura').grid(row=12, column=1, columnspan=1)
        ttk.Button(self, text='+', command=self.add_temp, width=5).grid(row=12, column=2, columnspan=1)
        ttk.Button(self, text='Zakończ cykl', command=self.master.finish_cycle).grid(row=14, column=1, columnspan=2)
        ttk.Button(self, text='zapisz', command=self.master.save).grid(row=15, column=2, columnspan=2)

    def previous(self):
        self.master.previous()

    def next(self):
        self.master.next()

    def add_msg(self):
        self.master.card.add_param(day=self.day.get() - 1, msg=self.msg.get())
        self.day.set(self.day.get() + 1)

    def add_obj(self, obj):
        self.master.card.add_param(day=self.day.get() - 1, obs=obj)
        self.day.set(self.day.get() + 1)

    def add_temp(self, button=False):
        self.master.card.add_param(day=self.day.get() - 1, temp=self.current_temp.get())
        if button:
            self.day.set(self.day.get() + 1)

    def objaw_create(self):
        canvas = tk.Canvas(self, width=140, height=150, bg='white')
        ilosc = ['', 'm', 'd']
        odc_l = ['', 'l', 'w', 'mo', 'śl', 'ol']
        wgl_l = ['', 'g', 'mę', 'gr', 'b', 'ż', 'r', 'p', 'jb']
        canvas.odc_l, canvas.wgl_l, canvas.ilosc = odc_l, wgl_l, ilosc
        canvas.state = {'ilosc': 0, 'odc': 0, 'wgl': 0, 'k':1, 'str': 's'}
        return canvas

    def _objaw_draw(self):
        self.objaw.grid_forget()
        self.objaw.create_rectangle(0, 0, 500, 500, fill='white')
        # print('state: {}'.format(self.objaw.state))
        y = temp_y + self.objaw.state['wgl'] * sqr + sqr
        x = temp_x + self.objaw.state['odc'] * sqr + sqr
        self.objaw.create_rectangle(temp_x, y - sqr, len(self.objaw.odc_l) * sqr + temp_x, y, fill='gray')
        self.objaw.create_rectangle(x - sqr, temp_y, x, len(self.objaw.wgl_l) * sqr + temp_y, fill='gray')
        self.objaw.create_text(temp_x + sqr / 2, temp_y, text='s/-', anchor=tk.N)

        for dist, odc in enumerate(self.objaw.wgl_l):
            y = temp_y + dist * sqr + sqr
            self.objaw.create_line(temp_x, y, len(self.objaw.odc_l) * sqr + temp_x, y)
            self.objaw.create_text(temp_x + sqr / 2.5, y - sqr, text=odc, anchor=tk.N)
        for dist, wgl in enumerate(self.objaw.odc_l):
            x = temp_x + dist * sqr + sqr
            self.objaw.create_line(x, temp_y, x, len(self.objaw.wgl_l) * sqr + temp_y)
            self.objaw.create_text(x - sqr / 2, temp_y, text=wgl, anchor=tk.N)

        for i, text in enumerate(self.objaw.ilosc):
            x, y = temp_x + 7 * sqr, temp_y + i * sqr
            if i == self.objaw.state['ilosc']:
                self.objaw.create_rectangle(x, y, x + sqr, y + sqr, fill='gray')
            self.objaw.create_rectangle(x, y, x+sqr, y+sqr)
            self.objaw.create_text(x + sqr / 2, y + sqr / 2, text=text)

        self.objaw.create_rectangle(temp_x + 7 * sqr, temp_y + 9 * sqr, temp_x + 8 * sqr,
                                     temp_y + (9 - self.objaw.state['k']) * sqr, fill='red')

        self.objaw.create_rectangle(temp_x + 7 * sqr, temp_y + 9 * sqr,
                                    temp_x + 8 * sqr, temp_y + 4 * sqr)

        self.objaw.grid(row=4, column=1, rowspan=6, columnspan=2)

    def keyboard_handler(self, event, entry):
        keymap = {'Return': entry, 'Up': lambda: self.day.set(self.day.get()+1), 'Down': lambda: self.day.set(self.day.get()-1)}
        if event.keysym in keymap:
            keymap[event.keysym]()
            self.master.card.update_canvas()

    def objaw_handler(self, event):
        if temp_x < event.x < temp_x + sqr * len(self.objaw.odc_l) and temp_y < event.y < temp_y + sqr * len(self.objaw.wgl_l):
            wgl, odc = (event.y - temp_y) // sqr, (event.x - temp_x) // sqr
            if self.objaw.state['odc'] != odc or self.objaw.state['wgl'] != wgl:
                self._update_state(odc=odc, wgl=wgl)
            else:
                self.add_obj(self.objaw.state['str'])
        # ilosc
        if temp_x + 7 * sqr < event.x < temp_x + 8 * sqr and temp_y < event.y < temp_y + sqr * len(self.objaw.ilosc):
            ilosc = (event.y - temp_y) // sqr
            if self.objaw.state['ilosc'] != ilosc:
                self._update_state(ilosc=ilosc)
            else:
                self.add_obj(self.objaw.state['str'])
        # krwawienie
        if temp_x + 7 * sqr < event.x < temp_x + 8 * sqr and temp_y + 4 * sqr < event.y < temp_y + 9 * sqr:
            ilosc_k = (temp_y + 10 * sqr - event.y) // sqr
            if self.objaw.state['k'] != ilosc_k:
                self._update_state(k=ilosc_k)
            else:
                self.add_obj('k {}'.format(ilosc_k))
        self._objaw_draw()

    def _update_state(self, odc=None, wgl=None, ilosc=None, k=None):
        if odc is not None:
            self.objaw.state['odc'] = odc
        if wgl is not None:
            self.objaw.state['wgl'] = wgl
        if ilosc is not None:
            self.objaw.state['ilosc'] = ilosc
        if k is not None:
            self.objaw.state['k'] = k
        s = ' '.join([self.objaw.odc_l[self.objaw.state['odc']], self.objaw.wgl_l[self.objaw.state['wgl']], self.objaw.ilosc[self.objaw.state['ilosc']]]
                     ).strip()
        if not s:
            s = 's'
        self.objaw.state['str'] = s

