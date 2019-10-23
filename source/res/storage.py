import datetime as dt import json
import os
import res


class Person:  # TODO: dodatkowa lista specjalnych (akty, ból owólacyjny)

    __path = os.path.split(os.path.abspath(__file__))[0]

    def __init__(self, name, date=dt.datetime.now().date()):
        self.name = name
        res.config['name'] = name
        self._path = os.path.join(self.__path, '{}.json'.format(name))
        self._cnf_path = os.path.join(self.__path, 'config.json')
        if os.path.exists(self._path):
            with open(self._path) as file:
                self._cycles = json.loads(file.read())
            self._current_cycle = int(sorted(self._cycles.keys())[-1])
        else:
            self._cycles = {'1': NewCycle('U', date)}
            self._current_cycle = 1

    @property
    def cycle(self):
        return self._cycles[str(self._current_cycle)]

    @property
    def cycle_nr(self):
        return self._current_cycle

    @property
    def active(self):
        return self.cycle['active']

    @property
    def place(self):
        return self.cycle['place']

    def act(self, day, type):
        if day in self.cycle['special'][type]:
            self.cycle['special'][type].remove(day)
        else:
            self.cycle['special'][type].append(day)

    def finish_cycle(self, day):
        self.cycle['active'] = False
        self.cycle['len'] = day
        date = self.date + dt.timedelta(days=day)
        self._cycles[str(self.cycle_nr + 1)] = NewCycle(self.place, date)
        self._current_cycle += 1

    def __len__(self):
        return self.cycle['len']

    @property
    def date(self):
        return dt.date(**self.cycle['start_date'])

    def save(self):
        cnf = json.dumps(res.config, indent=2)
        s = json.dumps(self._cycles, indent=2)
        with open(self._cnf_path, 'w') as file:
            file.write(cnf)
        with open(self._path, 'w') as file:
            file.write(s)

    def previous(self):
        if self.cycle_nr > 1:
            self._current_cycle -= 1

    def next(self):
        if self.cycle_nr < len(self._cycles):
            self._current_cycle += 1

    def change_place(self):
        pl = {'P': 'U', 'U': 'O', 'O': 'P'}
        self.cycle['place'] = pl[self.place]


def NewCycle(place, date=dt.datetime.now().date()):
        return {'active': True, 'start_date': {'day': date.day, 'month': date.month, 'year': date.year}, 'len': 1,
                'place': place, 'temperature': [0 for _ in range(40)], 'observation': ['' for _ in range(40)],
                'comments': ['' for _ in range(40)], "special": {'bo': [], 'akty': [], 'interpret': 0}}

