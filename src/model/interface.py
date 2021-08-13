# -*- coding: utf-8 -*-
import os
from abc import ABC, abstractmethod
from os.path import join as path_join
from os.path import split as path_split


class NrpModel(ABC):
    """
    Abstract Model for NRP data storage
    """

    _path = path_split(os.path.abspath(__file__))[0]

    def __init__(self, name, cycles, config=None, path=None):
        """
        initialize model with None values
        """
        self.name = name
        self.path = path_join(self._path, f'{name}.json')
        self._cycles = cycles
        self._current_cycle = int(sorted(self._cycles.keys())[-1])

    @classmethod
    @abstractmethod
    def load(cls, name):
        pass

    @abstractmethod
    def export(self, path):
        pass

    def save_gui_config(self, config):
        self.gui_congfig = config
        self.export()

    @abstractmethod
    def get_cycle(self, nr):
        pass

    @abstractmethod
    def get_temperature(self, nr):
        pass

    @abstractmethod
    def get_symptom(self, nr):
        pass

    @abstractmethod
    def get_comment(self, nr):
        pass

