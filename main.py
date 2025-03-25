
import os
import csv
import codecs
import openpyxl

from dataclasses import dataclass, fields
from openpyxl import Workbook

from survey_item import survey_item

from utility import write_dataclass_to_csv



### leggo gli input dalle cartelle e li inserisco nelle variabili

# path della cartella di input
input_folder = r"C:\Development\Tesi\input"

## Presentazione Caso
specific_folder = r"\Presentazione Caso"

# testo
with open(input_folder + specific_folder + r"\testopresentazionecaso.txt", "r", encoding="utf-8") as file:
    testopresentazionecaso = file.read()

# immagine
immagine_html = f'<img src="{input_folder + specific_folder + r"\immaginepresentazionecaso.png"}">'









## MAIN

# Example usage
if __name__ == "__main__":
    # Create an instance of our dataclass
    item = survey_item()
    item.id = "1"
    item.related_id = "2"
    item.class_ = "class"
    item.type_and_scale = "type/scale"
    item.help = "ciaooo"

    # Write it to an Excel file
    write_dataclass_to_csv(item, "prova.csv")
