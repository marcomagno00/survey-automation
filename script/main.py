import os
import csv
import codecs
import openpyxl

from dataclasses import dataclass, fields
from openpyxl import Workbook

from survey_item import *
from utility import *


## MAIN

if __name__ == "__main__":

    # VARIABILI GLOBALI

    # path settings e path output
    file_path_settings = r"template/settings.tsv"
    file_path_output = r"output/output.tsv"
    
    # path input
    file_path_input = r"input/"
    file_path_presentazione_caso = r"input/Presentazione Caso"
    file_path_advice = r"input/Advice"
    file_path_confidenza_iniziale = r"input/Confidenza Iniziale"
    file_path_confidenza_finale = r"input/Confidenza Finale"
    file_path_opzioni_iniziali = r"input/Opzioni Iniziali"
    file_path_opzioni_finali = r"input/Opzioni Finali"
    file_path_presentazione_supporto = r"input/Presentazione Supporto"

    # testi (sempre uguali)
    text_advice = read_first_line_from_txt(give_first_txt_from_folder(file_path_advice))
    text_confidenza_finale = read_first_line_from_txt(give_first_txt_from_folder(file_path_confidenza_finale))
    text_confidenza_iniziale = read_first_line_from_txt(give_first_txt_from_folder(file_path_confidenza_iniziale))
    text_presentazione_caso = read_first_line_from_txt(give_first_txt_from_folder(file_path_presentazione_caso))
    text_presentazione_supporto = read_first_line_from_txt(give_first_txt_from_folder(file_path_presentazione_supporto))

    # opzioni iniziali
    list_opzioni_iniziali = []
    with open(file_path_opzioni_iniziali + r"/opzioniiniziali.txt", 'r') as file:
        list_opzioni_iniziali = [linea.strip() for linea in file]

    # opzioni finali
    list_opzioni_finali = []
    with open(file_path_opzioni_finali + r"/opzionifinali.txt", 'r') as file:
        list_opzioni_finali = [linea.strip() for linea in file]
    
    
    survey_settings = [] # lista di survey_item per definire i settings
    
    # leggo dal file settings.tsv e scrivo i dati nella lista survey_settings
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

    # se non ci sono immagini, esco
    if count_images_in_folder(file_path_presentazione_caso) == 0:
        print("Nessuna immagine trovata nella cartella di presentazione caso.")
        exit(1)

    # rinomino le immagini presenti nella cartella di presentazione caso
    rename_images_in_folder(file_path_presentazione_caso, "presentazione_caso_")
    
    index_case = 1 # indice per i casi (1, 2, 3...)
    max_index_case = count_images_in_folder(file_path_presentazione_caso) # numero del caso massimo
    survey_cases_A = [] # lista di "survey_item" che contiene i casi del gruppo A
    survey_cases_B = [] # lista di "survey_item" che contiene i casi del gruppo B (casi con AI)

    while (index_case <= max_index_case): # finchè ci sono immagini per la presentazione caso
        
        # casi del gruppo A
        case = []

        # gruppo
        case.append(group(type_and_scale = "0", name = f"Case{index_case}a"))

        # question
        text = f'<p>{text_presentazione_caso}</p><p>img src="presentazione_caso_{index_case}.png"</p><p><testopresentazionecaso></testopresentazionecaso></p><p><immaginepresentazionecaso></immaginepresentazionecaso></p>'
        case.append(question(type_and_scale = "L", name = f"HD{index_case}", text = text, mandatory = "Y")) # testo e immagine
        

        # loop per le opzioni (se presenti)
        for item in list_opzioni_iniziali:
            # aggiungo le opzioni iniziali
            case.append(answer(name = item, text = item))

        # answer decisioneiniziale1
        case.append(answer(name = "1", text = "FRESCO"))
        # answer decisioneiniziale2
        case.append(answer(name = "0", text = "NON FRESCO"))


        # question "Quanto sei confidente della risposta?"
        case.append(question(type_and_scale = "F", name = f"CONF{index_case}", text = text_confidenza_iniziale, mandatory = "Y"))
        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "per nulla confidente"))
        # answer 2
        case.append(answer(name = "2", text = ""))
        # answer 3
        case.append(answer(name = "3", text = ""))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "totalemente confidente"))

        survey_cases_A.append(case)

        #######################################################################################################
        
        # casi del gruppo B
        case = []

        # gruppo
        case.append(group(type_and_scale = "0", name = f"Case{index_case}b"))

        # question
        text = f'<p>{text_presentazione_caso}</p><p>img src="presentazione_caso_{index_case}.png"</p><p><testopresentazionecaso></testopresentazionecaso></p><p><immaginepresentazionecaso></immaginepresentazionecaso></p>'
        case.append(question(type_and_scale = "L", name = f"HD{index_case}", text = text, mandatory = "Y")) # testo e immagine
        
        # answer decisioneiniziale1
        case.append(answer(name = "1", text = "FRESCO"))
        # answer decisioneiniziale2
        case.append(answer(name = "0", text = "NON FRESCO"))

        # question "Quanto sei confidente della risposta?"
        case.append(question(type_and_scale = "F", name = f"CONF{index_case}", text = text_confidenza_iniziale, mandatory = "Y"))

        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "per nulla confidente"))
        # answer 2
        case.append(answer(name = "2", text = ""))
        # answer 3
        case.append(answer(name = "3", text = ""))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "totalemente confidente"))

        survey_cases_B.append(case)









        index_case += 1 # incremento l'indice del caso
       


    # OUTPUT
    
    # print dei dati letti
    print()
    print(r"testo presentazione caso:", text_presentazione_caso)
    print(r"testo presentazione supporto:", text_presentazione_supporto)
    print(r"testo confidenza iniziale:", text_confidenza_iniziale)
    print(r"testo confidenza finale:", text_confidenza_finale)
    print(r"lunghezza di survey_cases_A:", len(survey_cases_A))
    print(r"numero di immagini in Presentazione Caso:", count_images_in_folder(file_path_presentazione_caso))
    print()
    
    rename_images_in_folder(file_path_presentazione_caso, "presentazione_caso_")

    # svuoto output.tsv se esiste già
    with open(file_path_output, "w", encoding="utf-8") as f:
        pass
    
    # creo il file di output output.tsv
    create_survey(survey_settings, survey_cases_A, survey_cases_B, file_path_output)
    convert_tsv_to_txt(file_path_output, file_path_output.replace(".tsv", ".txt"), delimiter="\t")




    











    
