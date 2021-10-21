# -*- coding: utf-8 -*-
import datetime as dt
from dataclasses import dataclass, field
from typing import List, Dict, NewType

@dataclass
class Cycle:
    """
    Cycle class for NRP data storage
    """
    ID: NewType('CycleID', int)
    START: dt.date = field(default=dt.date.today())
    temperature: Dict[int, int] = field(default_factory=dict,repr=False)
    symptom: Dict[int, int] = field(default_factory=dict,repr=False)
    comment: Dict[int, str] = field(default_factory=dict,repr=False)
    extra: Dict[int, List[str]] = field(default_factory=dict,repr=False)

    def add_temperature(self, day:int, value:int) -> None:
        self.temperature[day] = value

    def get_temperature_list(self, length:int=40, offset:int=0) -> List[int]:
        tmp = [0 for _ in range(length)]
        for day,val in self.temperature.items():
            tmp[day - offset] = val
        return tmp

    def get_temperature(self, day:int) -> int:
        if day in self.temperature.keys():
            return self.temperature[day]
        return 0

    def add_symptom(self, day:int, value:str) -> None:
        self.symptom[day] = value

    def get_symptom_list(self, length:int=40, offset:int=0) -> List[str]:
        tmp = [0 for _ in range(length)]
        for day,val in self.symptom.items():
            tmp[day - offset] = val
        return tmp

    def get_symptom(self, day:int) -> int:
        if day in self.symptom.keys():
            return self.symptom[day]
        return 0

    def add_comment(self, day:int, value:str) -> None:
        self.comment[day] = value

    def get_comment_list(self, length:int=40, offset:int=0) -> List[str]:
        tmp = [0 for _ in range(length)]
        for day,val in self.comment.items():
            tmp[day - offset] = val
        return tmp

    def get_comment(self, day:int) -> int:
        if day in self.comment.keys():
            return self.comment[day]
        return 0

    def get_day(self, day:int) -> dict:
        day = {
                'temperature': self.temperature[day],
                'symptom': self.symptom[day],
                'comment': self.comment[day],
                'extra': self.extra[day]
               }
        return day

if __name__ == "__main__":
    test = Cycle(1)
    print(test)
    print(test.__repr__())
