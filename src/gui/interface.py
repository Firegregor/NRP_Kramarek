# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class NrpViev(ABC):
    """
    Abstract viev for NRP
    """

    config = {}

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def welcome_screen(self, config_callback, user_callback):
        pass

    @abstractmethod
    def config_screen(self):
        pass

    @abstractmethod
    def draw_card(self, config):
        pass

