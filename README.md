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
    - establish dict structure for model
    - helper function for accessing data
- Gui:
  - Tkinter viev:
    V welcome screen:
        + renders properly
        - updates according to configuration
        - provide list of known users
    - main window
        + empty table
        + surrounding interface
        - draw temperature
        - draw symptoms
        - draw comments
        - draw special characters
    V config window
        + as a separate window
        + splited to categories
        + render properly
        + update configuration properly
- Controller:
  Nrp:
    + initializing seqience
    - config handling
    - cycle navigation
