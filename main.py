# -*- coding: utf-8 -*-
import tkinter as tk
import os.path as op
import json
import config
from source.gui.gui import Gui


def load_config():
    path = op.split(op.abspath(__file__))[0]
    with open(op.join(path, 'config', 'config.json')) as file:
        temp_config = json.loads(file.read())
        for param, value in temp_config.items():
            config.config[param] = value


if __name__ == '__main__':
    try:
        load_config()
        Gui()
    except Exception as e:
        print(e)
        input()
