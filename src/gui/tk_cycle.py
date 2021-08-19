import logging
import tkinter as tk
from tkinter import ttk


class CycleScreen(ttk.LabelFrame):
    """
    Frame with cycle viev
    """

    CANVAS = ['width', 'height', 'bg']

    def __init__(self, master, config, data, *args, **kwargs):
        self.data = data
        self.config = config
        super().__init__(master,text=data.get_name(), *args, **kwargs)
        self.display = None
        self.update()

    def update(self, config=None):
        logging.info('card update')
        if config is not None:
            logging.debug('New configuration')
            self.config=config
        self.blank()
        self.draw_data()
        self.display.pack()

    def blank(self):
        """
        Draws blank cycle card based on configuration
        """
        if self.display is not None:
            self.display.pack_forget()
        self.display = tk.Canvas(self, **self.canvas_config)
        self._draw_table()

    def _draw_table(self):

        # get data from config
        config = self.config
        total_width = config['width']
        total_heigth = config['height']
        padding = config['padding']
        label_width = config['label width']
        days = config['days displayed']
        temp_range = config['temperature range']
        table_top = padding + config['info height']
        table_left = 2*(padding + label_width)
        field_width = (total_width-padding-label_width-table_left)//days
        field_height = (total_heigth - 2*table_top - config['symptom height'])//temp_range
        table_right = table_left + days*field_width
        symp_padding = table_top + temp_range*field_height
        symp_bottom = symp_padding + config['symptom height']

        # create interface outline
        self.display.create_text((padding+table_left)//2, table_top, text='Data', anchor=tk.NE)
        self.display.create_line(padding, padding, table_right, padding, width=2)
        self.display.create_line(padding, table_top + field_height, table_right, table_top+field_height, width=2)
        self.display.create_line(table_left, table_top, table_right, table_top, width=2)
        self.display.create_line(padding, symp_bottom, table_right, symp_bottom, width=2)
        self.display.create_line(padding, symp_padding, table_right, symp_padding, width=2)
        self.display.create_line(padding, symp_padding - field_height, table_right, symp_padding - field_height, width=2)

        # table outline
        # self.display.create_rectangle(table_left,table_top, table_right, symp_padding, fill='red')
        self.display.create_line(table_left, padding, table_left, symp_bottom)
        self.display.create_line(table_right, padding, table_right, symp_bottom)
        # table vertical
        for day,column in enumerate(range(table_left, table_right, field_width)):
            self.display.create_line(column, table_top, column, symp_bottom)
            #TODO: days
        # table horizontal
        for row in range(table_top,symp_padding, field_height):
            self.display.create_line(table_left, row, table_right, row)

    @property
    def canvas_config(self):
        return {key: val for key,val in self.config.items() if key in self.CANVAS}

    def set_rgb(self, r, g, b):
        self._str = None
        self.R, self.G, self.B = r, g, b
        self.update()

    def draw_data(self):
        pass

    def __str__(self):
        return f"Frame containing cycle viev"


