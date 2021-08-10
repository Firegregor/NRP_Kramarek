# -*- coding: utf-8 -*-
from src import TkViev, JsonModel ,NRP

def main():
    app = NRP(JsonModel, TkViev())

if __name__ == "__main__":
    main()
