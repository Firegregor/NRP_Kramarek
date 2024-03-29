# -*- coding: utf-8 -*-
import logging
from src.model import NrpModel
from src.gui import NrpViev


class NRP:
    """
    Nrp Controller class
    """
    def __init__(self, model: NrpModel, gui: NrpViev):
        logging.info("NRP Controller init")
        self._model_class = model
        logging.debug("NRP Controller - model saved")
        self._gui_class = gui
        logging.debug("NRP Controller - gui saved")
        gui.welcome(self.model_config)

    def welcome(self):
        """
        Show welcome screen with callbacks to configuration and start
        """
        self.gui.welcome_screen(self.set_config, self.draw_user)

    def model_config(self, name):
        logging.info(f'Loading {name}')
        self.model = self._model_class.load(name)
        self.gui = self._gui_class(self.set_config)
        self.gui.config_apply(self._gui_class.config)
        self.model.save_gui_config(self.gui.config)
        logging.debug("NRP Controller - gui created")
        self.draw_user(name)
        self.gui.mainloop()

    def set_config(self):
        self.gui.config_screen()
        model.save_gui_config(self.gui.config)

    def draw_user(self, name):
        logging.debug(f'drawing user {name}')
        self.gui.draw_card(self, name)

    def get_name(self):
        return self.model.name
