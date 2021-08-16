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

    @classmethod
    def load(cls, name):
        """
        Loads from file or default values in case of non existing and return model.
        """
        name = name
        path = path_join(cls._path, f'{name}.json')
        if os.path.exists(path):
            with open(path) as model_dump:
                data = json.loads(model_dump.read())
        else:
            data = {'gui': {}, 'cycles': "Default"}
        return cls(name, data, path)

    def export(self):
        with open(self.path, 'w') as dump:
            content = {'gui':self.gui_config, 'cycles':self.cycles}
            dump.write(json.dumps(content, indent=2))

    def get_cycle(self, nr):
        pass

    def get_temperature(self, nr):
        pass

    def get_symptom(self, nr):
        pass

    def get_comment(self, nr):
        pass

