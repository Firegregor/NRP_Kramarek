import logging
import tkinter as tk
from tkinter import ttk


test_temp_values = [366, 368, 358,365, 365,366]
test_symp_values = ['','k5','k4','k3','s','mo']


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
        self.cell=None
        self.data_displayed = {
            'temperature':test_temp_values+[0]*config['days displayed'],
            'symptoms':test_symp_values+['']*config['days displayed']
            }
        self.big_font = ' '.join([
            self.config['font type'],
            str(self.config['interface size'])])
        self.text_font = ' '.join([
            self.config['font type'],
            str(self.config['text size'])])
        self.update()

    def update(self, config=None, data=None):
        logging.info('card update')
        if config is not None:
            logging.debug('New configuration')
            self.config=config
        if data is not None:
            self.data_displayed=data
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
        self.draw_empty_card()

    def draw_empty_card(self):
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
        field_height = (total_heigth - 2*table_top
                        - config['symptom height'])//temp_range
        table_right = table_left + days*field_width
        table_heigth = temp_range*field_height
        symp_padding = table_top + table_heigth
        symp_bottom = symp_padding + config['symptom height']
        fg = config['text color']
        self.cell = (field_width, field_height)

        # create interface outline
        self.display.create_text(
            (padding+table_left)//2,
            (padding + table_top + field_height) // 2,
            text='Data',
            font=self.big_font,
            fill=fg,
            anchor=tk.E)
        self.display.create_line( # all the way to the top
            padding,
            padding,
            table_right,
            padding,
            width=2)
        self.display.create_line( # under data
            padding,
            table_top + field_height,
            table_right,
            table_top+field_height,
            width=2)
        self.display.create_line( # between month and day
            table_left,
            table_top,
            table_right,
            table_top,
            width=2)
        self.display.create_line( # all the way to the bottom
            padding,
            symp_bottom,
            table_right,
            symp_bottom,
            width=2)
        self.display.create_line( # under cycle day
            padding,
            symp_padding,
            table_right,
            symp_padding,
            width=2)
        self.display.create_line( # over cycle day
            padding,
            symp_padding - field_height,
            table_right,
            symp_padding - field_height,
            width=2)

        # table outline
        # self.display.create_rectangle(table_left,table_top, table_right, symp_padding, fill='red')
        self.display.create_line( # table left
            table_left,
            padding,
            table_left,
            symp_bottom,
            width=2)
        self.display.create_line( # table right
            table_right,
            padding,
            table_right,
            symp_bottom,
            width=2)
        # table vertical
        for day,column in enumerate(range(table_left, table_right,
                 field_width),1+config['days offset']):
            self.display.create_line( # all vertical
                column,
                table_top,
                column,
                symp_bottom)
            self.display.create_text(
                column+field_width//2,
                symp_padding-field_height//2,
                font=self.text_font,
                fill=fg,
                text=day)
        # table horizontal
        for temp,row in enumerate(range(symp_padding, table_top,
             -field_height),int(config['min temperature']*10-1)):
            self.display.create_line(table_left, row, table_right, row)
            if (row > table_top + field_height
               and row < symp_padding - field_height):
                if not temp % 5:
                    self.display.create_text(
                        table_left-field_width,
                        row,
                        font=self.text_font,
                        fill=fg,
                        text=temp/10)
                else:
                    self.display.create_text(
                        table_left-field_width,
                        row,
                        font=self.text_font,
                        fill=fg,
                        text=f'.{temp%10}', anchor=tk.W)

        # ovals
        self._draw_oval(padding+label_width//2,
                        table_top+table_heigth//4,
                        'Godzina')
        self._draw_oval(padding+label_width//2,
                        table_top+table_heigth//2,
                        'Miejsce')
        self._draw_oval(table_right+label_width,
                        table_top+self.config['oval message'],
                        'Nr cyklu')
        self._draw_oval(table_right+label_width,
                        table_top+table_heigth*3//4,
                        'Faza niższa')
        self._draw_oval(table_right+label_width,
                        symp_padding,
                        'Długość cyklu')

        # Symptoms
        self.display.create_text(
            table_left - padding // 2,
            symp_padding + padding // 5,
            text='Śluz\nszyjkowy:\nodczucie\nwygląd\nilość',
            font=self.text_font,
            anchor=tk.NE)

    def _draw_oval(self, x, y, msg=''):
        size = self.config["oval size"]
        orect = [x-size, y-size, x+size, y+size]
        self.display.create_oval(*orect, width=2)
        self.display.create_text(x, y - self.config['oval message'],
            font=self.text_font,
            text=msg)

    @property
    def canvas_config(self):
        return {key: val for key,val in self.config.items()
                     if key in self.CANVAS}

    def draw_data(self):
        self.draw_temperature()
        self.draw_symtoms()
        self.draw_comments()
        self.draw_symbols()

    def draw_temperature(self):
        field_width, field_height = self.cell
        size = self.config["dot size"]
        day1 = 2*(self.config['padding']+self.config['label width']
                ) + field_width//2
        temp0 = (self.config['padding']
                +self.config['info height']
                +field_height*(
                    self.config['temperature range']
                    +10*self.config['min temperature']
                    -1)
                )
        previous=0
        for day, temp in enumerate(self.data_displayed['temperature'],
            -self.config['days offset']):
            x = day1 + field_width * day
            y = temp0 - field_height * temp
            orect = [x-size, y-size, x+size, y+size]
            if (temp > 10*self.config['min temperature'] 
                and 0 <= day < self.config['days displayed']):
                self.display.create_oval(*orect, fill=self.config['text color'])
                if previous > 0 and 10*self.config['min temperature']:
                    self.display.create_line(
                        x, y, x-field_width, previous,
                        width=self.config['dot size']
                        )
                previous = y
            else:
                previous = 0

    def draw_symtoms(self):
        for day, symp in enumerate(self.data_displayed['symptoms'],
            -self.config['days offset']):
            if 0 <= day < self.config['days displayed']:
                #self.display.create_text(100, 100, text=symp)
                pass

    def draw_comments(self):
        pass

    def draw_symbols(self):
        pass

    def __str__(self):
        return f"Frame containing cycle viev"


