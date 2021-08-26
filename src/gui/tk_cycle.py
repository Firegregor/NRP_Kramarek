import logging
import tkinter as tk
from tkinter import ttk
from itertools import zip_longest


test_temp_values = [366, 368, 358,365, 365,366]
test_symp_values = ['','k5','k4','k3','s','mo']
test_coments_values = ['sda', 'nieprzespana noc', 'Stres', 'alkohol', '', 'cos']


class CycleScreen(ttk.LabelFrame):
    """
    Frame with cycle viev
    """

    CANVAS = ['width', 'height', 'bg']

    def __init__(self, master, config, data, *args, **kwargs):
        self.data = data
        super().__init__(master,text=data.get_name(), *args, **kwargs)
        self.display = None
        self.data_displayed = {
            'temperature':test_temp_values+[0]*config['days displayed'],
            'comments':test_coments_values+['']*config['days displayed'],
            'symptoms':test_symp_values+['']*config['days displayed']
            }
        self.update(config=config)

    def update(self, config=None, data=None):
        logging.info('card update')
        if config is not None:
            logging.debug('New configuration')
            self.config=config
            self._update_config()
        self.blank()
        if data is not None:
            self.data_displayed=data
        self.draw_data()
        self.display.pack()

    def blank(self):
        """
        Draws blank cycle card based on configuration
        """
        if self.display is not None:
            self.display.pack_forget()
        canvas_params = {key: self.config[key] for key in self.CANVAS}
        self.display = tk.Canvas(self, **canvas_params)
        self._create_interface_outline()
        self._table()

    def draw_data(self):
        self._drawtemperature()
        self._drawsymtoms()
        self._drawcomments()
        self._drawsymbols()

    def _update_config(self):
        # get data from config
        config = self.config
        self.total_width = config['width']
        self.total_heigth = config['height']
        self.padding = config['padding']
        self.label_width = config['label width']
        self.days = config['days displayed']
        self.delay = config['days offset']
        self.temp_range = config['temperature range']
        self.temp_min = config['min temperature']*10
        self.table_top = self.padding + config['info height']
        self.table_left = 2*(self.padding + self.label_width)
        self.field_width = (self.total_width-self.padding-self.label_width-self.table_left)//self.days
        self.field_height = (self.total_heigth - 2*self.table_top
                        - config['symptom height'])//self.temp_range
        self.table_right = self.table_left + self.days*self.field_width
        self.table_heigth = self.temp_range*self.field_height
        self.symp_padding = self.table_top + self.table_heigth
        self.symp_bottom = self.symp_padding + config['symptom height']
        self.fg = config['text color']
        self.big_font = ' '.join([
            config['font type'],
            str(config['interface size'])])
        self.text_font = ' '.join([
            config['font type'],
            str(config['text size'])])

    def _create_interface_outline(self):
        self.display.create_text(
            (self.padding+self.table_left)//2,
            (self.padding + self.table_top + self.field_height) // 2,
            text='Data',
            font=self.big_font,
            fill=self.fg,
            anchor=tk.E)
        self.display.create_line( # all the way to the top
            self.padding,
            self.padding,
            self.table_right,
            self.padding,
            width=2)
        self.display.create_line( # under data
            self.padding,
            self.table_top + self.field_height,
            self.table_right,
            self.table_top+self.field_height,
            width=2)
        self.display.create_line( # between month and day
            self.table_left,
            self.table_top,
            self.table_right,
            self.table_top,
            width=2)
        self.display.create_line( # all the way to the bottom
            self.padding,
            self.symp_bottom,
            self.table_right,
            self.symp_bottom,
            width=2)
        self.display.create_line( # under cycle day
            self.padding,
            self.symp_padding,
            self.table_right,
            self.symp_padding,
            width=2)
        self.display.create_line( # over cycle day
            self.padding,
            self.symp_padding - self.field_height,
            self.table_right,
            self.symp_padding - self.field_height,
            width=2)
        self.display.create_text(
            self.table_left - self.padding // 2,
            self.symp_padding + self.padding // 5,
            text='Śluz\nszyjkowy:\nodczucie\nwygląd\nilość',
            font=self.text_font,
            anchor=tk.NE)
        # ovals
        self._draw_oval(self.padding+self.label_width//2,
                        self.table_top+self.table_heigth//4,
                        'Godzina')
        self._draw_oval(self.padding+self.label_width//2,
                        self.table_top+self.table_heigth//2,
                        'Miejsce')
        self._draw_oval(self.table_right+self.label_width,
                        self.table_top+self.config['oval message'],
                        'Nr cyklu')
        self._draw_oval(self.table_right+self.label_width,
                        self.table_top+self.table_heigth*3//4,
                        'Faza niższa')
        self._draw_oval(self.table_right+self.label_width,
                        self.symp_padding,
                        'Długość cyklu')

    def _table(self):
        # Outline
        # self.display.create_rectangle(self.table_left,self.table_top, self.table_right, self.symp_padding, fill='red')
        self.display.create_line( # table left
            self.table_left,
            self.padding,
            self.table_left,
            self.symp_bottom,
            width=2)
        self.display.create_line( # table right
            self.table_right,
            self.padding,
            self.table_right,
            self.symp_bottom,
            width=2)
        # table vertical
        for day,column in enumerate(
            range(self.table_left, self.table_right, self.field_width),
            1+self.delay
            ):
            self.display.create_line( # all vertical
                column,
                self.table_top,
                column,
                self.symp_bottom)
            self.display.create_text(
                column+self.field_width//2,
                self.symp_padding-self.field_height//2,
                font=self.text_font,
                fill=self.fg,
                text=day)
        # table horizontal
        for temp,row in enumerate(range(self.symp_padding, self.table_top,
             -self.field_height),int(self.temp_min - 1)):
            self.display.create_line(self.table_left, row, self.table_right, row)
            if (row > self.table_top + self.field_height
               and row < self.symp_padding - self.field_height):
                if not temp % 5:
                    self.display.create_text(
                        self.table_left-self.field_width,
                        row,
                        font=self.text_font,
                        fill=self.fg,
                        text=temp/10)
                else:
                    self.display.create_text(
                        self.table_left-self.field_width,
                        row,
                        font=self.text_font,
                        fill=self.fg,
                        text=f'.{temp%10}', anchor=tk.W)

    def _draw_oval(self, x, y, msg=''):
        size = self.config["oval size"]
        orect = [x-size, y-size, x+size, y+size]
        self.display.create_oval(*orect, width=2)
        self.display.create_text(x, y - self.config['oval message'],
            font=self.text_font,
            text=msg)

    def _drawtemperature(self):
        size = self.config["dot size"]
        day1 = 2*(self.config['padding']+self.config['label width']
                ) + self.field_width//2
        temp0 = (self.config['padding']
                +self.config['info height']
                +self.field_height*(
                    self.config['temperature range']
                    +10*self.config['min temperature']
                    -1)
                )
        previous=0
        for day, temp in enumerate(self.data_displayed['temperature'],
            -self.delay):
            x = day1 + self.field_width * day
            y = temp0 - self.field_height * temp
            orect = [x-size, y-size, x+size, y+size]
            if (temp > 10*self.config['min temperature'] 
                and 0 <= day < self.config['days displayed']):
                self.display.create_oval(*orect, fill=self.config['text color'])
                if previous > 0 and 10*self.config['min temperature']:
                    self.display.create_line(
                        x, y, x-self.field_width, previous,
                        width=self.config['dot size']
                        )
                previous = y
            else:
                previous = 0

    def _drawsymtoms(self):
        day1 = 2*(self.padding+self.label_width) -self.field_width//2
        for day, symp in enumerate(self.data_displayed['symptoms'],
            -self.delay):
            if 0 < day < self.config['days displayed']:
                self.display.create_text(
                    day1+day*self.field_width,
                    self.symp_bottom-(self.config['symptom height']*2)//3,
                    text=symp,
                    font=self.text_font,
                    )

    def _drawcomments(self):
        day1 = 2*(self.padding+self.label_width) + self.field_width//2
        temp0 = (self.table_top + self.field_height
             * (self.temp_range+self.temp_min-1))
        for day, (temp, msg) in enumerate(
            zip(
                self.data_displayed['temperature'],
                self.data_displayed['comments']
                ),
            -self.delay
            ):
            x = day1 + self.field_width * day
            if temp < self.temp_min:
                y = temp0 - int(self.field_height * (self.temp_min +0.5))
            else:
                y = temp0 - self.field_height * (temp +1)
            if 0 <= day < self.config['days displayed']:
                anchor = tk.E
                if self.temp_min < temp < self.temp_min+self.temp_range//2:
                    anchor=tk.W
                    y += self.field_height*2
                # logging.debug(f'Symptom x={x},y={y} - msg={msg} ')
                self.display.create_text(
                    x, y, text=msg,
                    angle=-90,
                    font=self.text_font,
                    anchor=anchor,
                    fill=self.config['text color'])

    def _drawsymbols(self):
        pass

    def __str__(self):
        return f"Frame containing cycle viev"



