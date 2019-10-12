# -*- coding: utf-8 -*-
import tkinter as tk
import os.path as op
import json
import source


def load_config():
    path = op.split(op.abspath(__file__))[0]
    with open(op.join(path, 'res', 'config.json')) as file:
        temp_config = json.loads(file.read())
        for param, value in temp_config.items():
            res.config[param] = value


if __name__ == '__main__':
    load_config()
    Gui()
