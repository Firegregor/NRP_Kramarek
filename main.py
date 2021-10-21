# -*- coding: utf-8 -*-
import argparse
import logging
import unittest
from src import TkViev, JsonModel ,NRP
from test.model.cycle_test import TestCycle

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = NRP(JsonModel, TkViev)

if __name__ == "__main__":
    unittest.main()
    print('Tests are ok')
    if 0:
        main()
