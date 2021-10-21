# -*- coding: utf-8 -*-
import unittest
import random as rd
import datetime as dt
import dataclasses as dc
from src.model.data_cycle import Cycle



class TestCycle(unittest.TestCase):

    def test_to_dict(self):
        self.assertEqual(
                dc.asdict(Cycle(0)),
                {
                    'ID': 0,
                    'START': dt.date.today(),
                    'temperature': {},
                    'symptom': {},
                    'comment': {},
                    'extra': {},
                }
                )

    def test_temperature(self):
        tc = Cycle(0)
        self.assertEqual(tc.get_temperature(0), 0)
        day = rd.randint(0,40)
        tc.add_temperature(day,360)
        self.assertEqual(tc.temperature[day], 360)
        self.assertEqual(tc.get_temperature(day), 360)
        temp_list = [0 for _ in range(40)]
        temp_list[day] = 360
        self.assertEqual(tc.get_temperature_list(), temp_list)

    def test_symptom(self):
        tc = Cycle(0)
        self.assertEqual(tc.get_symptom(0), 0)
        day = rd.randint(0,40)
        tc.add_symptom(day,360)
        self.assertEqual(tc.symptom[day], 360)
        self.assertEqual(tc.get_symptom(day), 360)
        temp_list = [0 for _ in range(40)]
        temp_list[day] = 360
        self.assertEqual(tc.get_symptom_list(), temp_list)

    def test_comment(self):
        tc = Cycle(0)
        self.assertEqual(tc.get_comment(0), 0)
        day = rd.randint(0,40)
        tc.add_comment(day,360)
        self.assertEqual(tc.comment[day], 360)
        self.assertEqual(tc.get_comment(day), 360)
        temp_list = [0 for _ in range(40)]
        temp_list[day] = 360
        self.assertEqual(tc.get_comment_list(), temp_list)

