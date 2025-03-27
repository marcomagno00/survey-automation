import os
import csv
import codecs
import openpyxl

from dataclasses import dataclass, fields
from openpyxl import Workbook

from survey_item import survey_item, group, question, sub_question, answer

from utility import write_dataclass_to_csv, add_row_to_csv
import template

### leggo gli input dalle cartelle e li inserisco nelle variabili

# path della cartella di input
#input_folder = r"C:\Development\Tesi\input"

## Presentazione Caso
#specific_folder = r"\Presentazione Caso"

# testo
#with open(input_folder + specific_folder + r"\testopresentazionecaso.txt", "r", encoding="utf-8") as file:
#    testopresentazionecaso = file.read()

# immagine
#immagine_html = f'<img src="{input_folder + specific_folder + r"\immaginepresentazionecaso.png"}">'









## MAIN

if __name__ == "__main__":

    # creo una lista di survey_item per definire i settings
    # leggo dal file settings_survey.csv e scrivo e scrivo i dati

    survey_settings = []
    file_path = r"/Users/marcogrande/Development/Tesi/survey-automation/template/settings_survey.csv"

    with open(file_path, "r") as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            
            item = survey_item()

            item.class_ = row[0]
            item.name = row[2]
            item.text = row[4]
            item.language = row[6]

            survey_settings.append(item)


    # creo una lista di survey_item per definire i casi
    # leggo dalle cartelle di input e scrivo e scrivo i dati
    survey_cases = []
    











    # Create an instance of our dataclass
    item = answer(id = "3", name= "si", text= "sicuramente si")
    item2 = group(id = "1", type_and_scale= "1", name= "gruppo1")
    # Write it to a csv file
    add_row_to_csv(item2, "output.csv")
