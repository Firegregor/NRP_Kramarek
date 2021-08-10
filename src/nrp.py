# -*- coding: utf-8 -*-
from src.model import NrpModel
from src.gui import NrpViev


class NRP:
    """
    Nrp Controller class
    """
    def __init__(self, model: NrpModel, gui: NrpViev):
        self.model = model
        self.model.load()
        self.gui = gui
        self.welcome()

    def welcome(self):
        """
        Show welcome screen with callbacks to configuration and start
        """
        self.gui.welcome_screen(self.set_config, self.draw_user)

    def set_config(self):
        gui.config_screen()

    def draw_user(self):
        pass