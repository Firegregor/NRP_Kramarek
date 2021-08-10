# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class NrpModel(ABC):
    """
    Abstract Model for NRP data storage
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def export(self, path):
        pass

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

