# -*- coding: utf-8 -*-
from source import NrpModel, NrpViev


class NRP:
    """
    Nrp Controller class
    """
    def __init__(self, model: NrpModlel, gui: NrpViev):
        self.model = model
        self.gui = gui
