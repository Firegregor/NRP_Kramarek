import tkinter as tk
import os.path as op
import json
import res
from gui.card_menu import CardMenu
from res.storage import Person


class Test(tk.LabelFrame):
    def __init__(self, master):
        super(Test, self).__init__(master, text='Test')
        self.card = tk.Frame(self)
        self.card.add_param = self.add_param
        self.card.person = Person('Test')
        self.menu=CardMenu(self)
        self.menu.pack()
        self.pack()

    def finish_cycle(self):
        print('Finish cycle called')

    def save(self):
        print('save called')

    def next(self):
        print('next called')

    def previous(self):
        print('previous called')

    def add_param(self, day, obs='', msg='', temp=''):
        print(f'Obs =  "{obs}", msg = "{msg}", temp = "{temp}" added on day {day}')


def load_config():
    path = op.split(op.abspath(__file__))[0]
    with open(op.join(path,'res', 'config.json')) as file:
        temp_config = json.loads(file.read())
        for param, value in temp_config.items():
            res.config[param] = value


if __name__ == '__main__':
    load_config()
    root = tk.Tk()
    root.geometry('250x600')
    Test(root)
    root.mainloop()
