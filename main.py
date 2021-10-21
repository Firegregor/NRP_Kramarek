# -*- coding: utf-8 -*-
import sys
import logging
import unittest
from src import TkViev, JsonModel ,NRP
from test import model_tests

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = NRP(JsonModel, TkViev)

if __name__ == "__main__":
    if len(sys.argv) > 0:
        unittest.main()
    else:
        main()
