import logging
import tkinter as tk
from tkinter import ttk


class TextConfig(ttk.Entry):
    def __init__(self, master, default, *args, **kwargs):
        super().__init__(master,*args,**kwargs)
        self.set(default)

    def set(self, value):
        self.delete(0,tk.END)
        self.insert(0,value)


class IntConfig(ttk.Spinbox):
    def __init__(self, master, default, from_, to, *args, **kwargs):
        super().__init__(master,from_=from_,to=to,*args,**kwargs)
        self._default=default

    def get(self):
        return int(super().get())


class TempConfig(ttk.Spinbox):
    def __init__(self, master, default, *args, **kwargs):
        super().__init__(master, *args,**kwargs,values=[str(x/10) for x in range(350,367)])

    def get(self):
        return float(super().get())


class ColorConfig(tk.Frame):
    def __init__(self, master, default, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._str = None
        self.R=ttk.Spinbox(self, from_=0, to=255, width=4)
        self.G=ttk.Spinbox(self, from_=0, to=255, width=4)
        self.B=ttk.Spinbox(self, from_=0, to=255, width=4)
        self.square = tk.Label(self, text=' '*5)
        self.set(default)
        self.square.pack(side=tk.LEFT)
        tk.Label(self, text='R', bg='red').pack(side=tk.LEFT)
        self.R.pack(side=tk.LEFT)
        tk.Label(self, text='G', bg='green').pack(side=tk.LEFT)
        self.G.pack(side=tk.LEFT)
        tk.Label(self, text='B', bg='blue').pack(side=tk.LEFT)
        self.B.pack(side=tk.LEFT)
        self.apply()
        self.square.bind('<ButtonPress-1>', self.update)

    def update(self, *_, rgb=True):
        if rgb:
            self._str = None
        self.apply()

    def apply(self):
        self.square.config(bg=self.get())

    def set(self, value):
        if value.startswith('#'):
            self.R.set(int(value[1:3],16))
            self.G.set(int(value[3:5],16))
            self.B.set(int(value[5:],16))
            self.update()
        else:
            self._str = value
            self.update(rgb=False)

    @property
    def color(self):
        if self._str is not None:
            return self._str
        return (self.R.get(), self.G.get(), self.B.get())

    def set_rgb(self, r, g, b):
        self._str = None
        self.R.set(r)
        self.G.set(g)
        self.B.set(b)
        self.update()

    def get(self):
        return str(self)

    def __str__(self):
        if self._str is not None:
            return self._str
        logging.warning(f'R = {int(self.R.get()):02x} G = {int(self.G.get()):02x} B = {int(self.B.get()):02x}')
        return f"#{int(self.R.get()):02x}{int(self.G.get()):02x}{int(self.B.get()):02x}"


class ConfigScreen(tk.Frame):
    CONFIG_TYPE = {"General": {
                'resolurion': (TextConfig, '1200x800'),
                'padding': (IntConfig, 10, 1, 20)
                },
              "Colors":{
                'background': (ColorConfig, '#cfcfcf'),
                },
              'Cycle': {
                'days offset': (IntConfig, 0, 0, 500),
                'min temperature': (TempConfig, 36.0),
                'temperature range': (IntConfig, 16, 10, 20),
                'days displayed': (IntConfig, 40, 35, 60),
                'width': (IntConfig, 1000, 800, 1500),
                'height': (IntConfig, 600, 500, 800),
                'bg': (ColorConfig, '#ffffff'),
                'scale': (IntConfig, 1, 1, 2),
                'padding': (IntConfig, 20, 5, 50),
                'label width': (IntConfig, 50, 20, 80),
                'info height': (IntConfig, 15, 10, 25),
                'symptom height': (IntConfig, 80, 50, 120),
                'oval size': (IntConfig, 20, 15, 30),
                'oval message': (IntConfig, 35, 20, 50),
                'font type': (TextConfig, 'Times'),
                'text color': (ColorConfig, '#000000'),
                'text size': (IntConfig, 10, 5, 25),
                'interface size': (IntConfig, 15, 7, 30),
                'dot size': (IntConfig, 4, 2, 7),
                }
            }

    def __init__(self, window, config, save, cycle=None, *args, **kwargs):
        logging.info(f'Config window init - cycle={cycle}')
        self.window=window
        self.save = save
        self.cycle = cycle
        super().__init__(window, *args, **kwargs)
        self.params = {}
        PADDING = int(config['General']['padding'])/2
        BG = config['Colors']['background']
        for category in self.CONFIG_TYPE:
            logging.debug(f"loading {category}")
            frame = ttk.LabelFrame(self, text=category)
            self.params[category] = {key:val[0](frame, *val[1:])
                     for key,val in self.CONFIG_TYPE[category].items()}
            logging.debug(f'{category}: params created')
            for i, (key, wid) in enumerate(self.params[category].items()):
                tk.Label(
                    frame,
                    text=key,
                    bg=BG
                    ).grid(row=i, column=0, padx=PADDING, pady=PADDING)
                wid.grid(row=i, column=1,padx=PADDING, pady=PADDING)
            logging.debug(f"{category}: params displayed")
            frame.pack(fill=tk.BOTH)
        self.set_values(config)
        ttk.Button(self ,text="Default",
         command=lambda: self.set_values(self.get_defaults())).pack()
        ttk.Button(self,
            text="Ok",
            command=self.save_current
            ).pack(side=tk.LEFT)
        ttk.Button(self,
            text="Cancel",
            command=self.done
            ).pack(side=tk.RIGHT)
        self.pack()

    @classmethod
    def get_defaults(cls):
        return {category:{key: val[1] for key,val in settings.items()
            } for category,settings in cls.CONFIG_TYPE.items()}

    def set_values(self, config):
        logging.info("Set config values")
        for category, cont in self.params.items():
            for key, val in cont.items():
                val.set(config[category][key])

    def save_current(self, *args):
        logging.info(f"saving config - cycle={self.cycle}")
        config = {category: {key: val.get() for key,val in values.items()}
                     for category, values in self.params.items()}
        self.save(config=config)
        logging.debug('update cycle')
        self.cycle.update(config['Cycle'])
        self.done()

    def done(self, *args):
        logging.info(f"close config window")
        self.window.destroy()



