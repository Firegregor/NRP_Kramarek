# NRP _Kramarek_

## Overviev

Program to store and viev cycles

## Parts

Model - Holds and process data

Gui - viev data and provide forms to insert data

Controller - handles user interaction

## Details

- Model:
  - Json Model:
    + load from json file
    + export to json file
    - cycle representation (as class)
    - establish dict structure for model
    - helper function for accessing data
- Gui:
  - Tkinter viev:
    V welcome screen:
        + renders properly
        - separate global configuration to chose model and viev
        - provide list of known users (requires controller callback)
    V main window
        + empty table
        + surrounding interface
        + draw temperature
        + draw symptoms
        + draw comments
        + bind controller functions to mouse click
        - draw special characters
        - menu for adding new data
    + config window
        + as a separate window
        + splited to categories
        + render properly
        + update configuration properly
        - more user friendly way of selecting color
- Controller:
  Nrp:
    + initializing seqience
    - config handling
    - cycle navigation
