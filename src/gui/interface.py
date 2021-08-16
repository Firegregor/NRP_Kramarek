# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class NrpViev(ABC):
    """
    Abstract viev for NRP
    """

    config = {}

    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def welcome(cls, model_load):
        pass

    @classmethod
    @abstractmethod
    def config_screen(cls):
        pass

    @classmethod
    @abstractmethod
    def config_apply(self, config=None):
        pass

    @abstractmethod
    def draw_card(self, config):
        pass

