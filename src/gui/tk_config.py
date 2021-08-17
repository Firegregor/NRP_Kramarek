import logging
import tkinter as tk
from tkinter import ttk


class TextConfig(ttk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def set(self, value):
        self.delete(0,tk.END)
        self.insert(0,value)


class TempConfig(ttk.Spinbox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs,values=[str(x/10) for x in range(350,367)])


class ColorConfig(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._str = None
        self.R=125
        self.G=125
        self.B=125
        self.square = tk.Label(self, text=' '*5)
        self.square.pack(fill=tk.BOTH)
        self.update()

    def update(self):
        self.square.config(bg=self.get())

    def set(self, value):
        self._str = value
        #TODO: pattern recognition of rgb values

    @property
    def color(self):
        if self._str is not None:
            return self._str
        return (self.R, self.G, self.B)

    def set_rgb(self, r, g, b):
        self._str = None
        self.R, self.G, self.B = r, g, b
        self.update()

    def get(self):
        return str(self)

    def __str__(self):
        if self._str is not None:
            return self._str
        return f"#{self.R:02x}{self.G:02x}{self.B:02x}"


class ConfigScreen(tk.Frame):
    CONFIG_TYPE = {"General": {
                'resolurion': TextConfig,
                'scale': ttk.Spinbox,
                'padding': ttk.Spinbox,
                },
              "Colors":{
                'background': ColorConfig,
                'forground': ColorConfig,
                },
              'Model': {
                'min temperature': TempConfig,
                'days offset': ttk.Spinbox}}

    def __init__(self, window, config, default, save, *args, **kwargs):
        self.window=window
        self.save = save
        super().__init__(window, *args, **kwargs)
        self.params = {}
        PADDING = int(config['General']['padding'])/2
        BG = config['Colors']['background']
        for category in self.CONFIG_TYPE:
            logging.debug(f"loading {category}")
            frame = ttk.LabelFrame(self, text=category)
            self.params[category] = {key:val(frame)
                     for key,val in self.CONFIG_TYPE[category].items()}
            logging.debug(f'{category}: params created')
            for i, (key, wid) in enumerate(self.params[category].items()):
                tk.Label(frame, text=key, bg=BG
                        ).grid(row=i, column=0, padx=PADDING, pady=PADDING)
                wid.grid(row=i, column=1,padx=PADDING, pady=PADDING)
            logging.debug(f"{category}: params displayed")
            frame.pack(fill=tk.BOTH)
        self.set_values(config)
        ttk.Button(self ,text="Default",
         command=lambda: self.set_values(default())).pack()
        ttk.Button(self ,text="Ok", command=self.save_current).pack(side=tk.LEFT)
        ttk.Button(self ,text="Cancel", command=self.done).pack(side=tk.RIGHT)
        self.pack()

    def set_values(self, config):
        logging.info("Set config values")
        for category, cont in self.params.items():
            for key, val in cont.items():
                val.set(config[category][key])

    def save_current(self, *args):
        logging.info(f"saving config")
        config = {category: {key: val.get() for key,val in values.items()}
                     for category, values in self.params.items()}
        self.save(config)
        self.done()

    def done(self, *args):
        logging.info(f"close config window")
        self.window.destroy()


