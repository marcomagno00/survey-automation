import os
import csv
import codecs
# import openpyxl

from dataclasses import dataclass, fields
# from openpyxl import Workbook

from survey_item import *
from utility import *



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

    
    file_path_settings = r"template/settings_survey.tsv"
    survey_settings = []
    
    with open(file_path_settings, "r") as file:
        reader = csv.reader(file, delimiter="\t")

        next(reader, None) # skippa la prima riga

        for row in reader:
            
            item = survey_item()

            item.class_ = row[0]
            item.name = row[2]
            item.text = row[4]
            item.language = row[6]

            survey_settings.append(item)


    # leggo dalle cartelle di input e scrivo e scrivo i dati

    
    ended = False
    index = 1

    # creo una lista di "survey_item" che contiene i casi del gruppo A
    survey_cases_A = []

    # casoA

    while (not ended): # finchè ci sono immagini per la presentazione caso
        
        case = []
        # gruppo
        case.append(group(type_and_scale = "1", name = f"Case{index}a"))

        # question
        case.append(question(type_and_scale = "L", name = f"HD{index}", text = "E' FRESCO O NO? e IMMAGINE PESCE", mandatory = "Y"))
        
        # answer decisioneiniziale1
        case.append(answer(name = "1", text = "FRESCO"))
        # answer decisioneiniziale2
        case.append(answer(name = "0", text = "NON FRESCO"))

        # question "Quanto sei confidente della risposta?"
        case.append(question(type_and_scale = "F", name = f"CONF{index}", text = "Quanto sei confidente della risposta?", mandatory = "Y"))

        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "per nulla confidente"))
        # answer 2
        case.append(answer(name = "2", text = ""))
        # answer 3
        case.append(answer(name = "3", text = ""))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "totalemente confidente"))

        ended = True

    survey_cases_A.append(case)
    
    
    for item in survey_settings:
        add_row_to_tsv(item, "output6.tsv")

    for case in survey_cases_A:
       for group_ in case:
            add_row_to_tsv(group_, "output6.tsv")










        
    



    











    
