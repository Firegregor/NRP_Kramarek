# -*- coding: utf-8 -*-
import os
import json
import datetime as dt
from os.path import join as path_join
from os.path import split as path_split
from src.model.interface import NrpModel


class JsonModel(NrpModel):
    """
    Json Model for NRP data storage
    """

    __path = path_split(os.path.abspath(__file__))[0]


    def __init__(self, name, cycles):
        """
        initialize model with None values
        """
        self.name = name
        self.path = path_join(self.__path, f'{name}.json')
        self._cycles = cycles
        self._current_cycle = int(sorted(self._cycles.keys())[-1])

    @classmethod
    def load(cls, name):
        """
        Loads from file or default values in case of non existing and return model.
        """
        name = name
        path = path_join(cls.__path, f'{name}.json')
        if os.path.exists(path):
            with open(path) as model_dump:
                cycles = json.loads(model_dump.read())
        else:
            cycles = {'1': "Default"}
        return cls(name, cycles)

    def export(self, path):
        pass

    def get_cycle(self, nr):
        pass

    def get_temperature(self, nr):
        pass

    def get_symptom(self, nr):
        pass

    def get_comment(self, nr):
        pass

