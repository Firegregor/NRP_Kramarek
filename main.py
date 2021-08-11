# -*- coding: utf-8 -*-
import logging
from src import TkViev, JsonModel ,NRP

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = NRP(JsonModel, TkViev)

if __name__ == "__main__":
    main()
