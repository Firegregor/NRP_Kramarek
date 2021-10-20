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
    START: dt.date = field(default=dt.datetime.now().date())
    temperature: List[int] = field(default_factory=list,repr=False)
    symptom: List[int] = field(default_factory=list,repr=False)
    comment: List[str] = field(default_factory=list,repr=False)
    extra: Dict[int, List[str]] = field(default_factory=dict,repr=False)

    def add_temperature(self, day:int, value:int) -> None:
        self.temperature[day] = value

    def add_symptom(self, day:int, value:int) -> None:
        self.symptom[day] = value

    def add_comment(self, day:int, value:int) -> None:
        self.comment[day] = value

    def get_temperature(self, day:int) -> int:
        return self.temperature[day]

    def get_symptom(self, day:int) -> int:
        return self.symptom[day]

    def get_comment(self, day:int) -> str:
        return self.comment[day]

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
