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
    images_path_dir = r"output/images/"
    
    # path input
    file_path_input = r"input/"
    file_path_presentazione_caso = r"input/Presentazione Caso"
    file_path_advice = r"input/Advice"
    file_path_confidenza_iniziale = r"input/Confidenza Iniziale"
    file_path_confidenza_finale = r"input/Confidenza Finale"
    file_path_opzioni_iniziali = r"input/Opzioni Iniziali"
    file_path_opzioni_finali = r"input/Opzioni Finali"
    file_path_presentazione_supporto = r"input/Presentazione Supporto"
    images_path = r"{SURVEYRESOURCESURL}/images"

    # testi (sempre uguali)
    text_advice_1 = read_first_line_from_txt("input/Advice/testoadvice1.txt")
    text_advice_2 = read_first_line_from_txt("input/Advice/testoadvice2.txt")
    text_spiegazione_advice_1 = read_first_line_from_txt("input/Advice/spiegazioneadvice1.txt")
    text_spiegazione_advice_2 = read_first_line_from_txt("input/Advice/spiegazioneadvice2.txt")
    
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
    

    # SETTINGS 
    
    survey_settings = [] # lista di survey_item per definire i settings
    
    # leggo dal file settings.tsv e scrivo i dati nella lista survey_settings
    with open(file_path_settings, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        next(reader, None) # salta la prima riga
        for row in reader:
            item = survey_item()
            item.class_ = row[0]
            item.name = row[2]
            item.text = row[4]
            item.language = row[6]
            survey_settings.append(item)

    # SURVEY

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
        
        # GRUPPO A
        case = [] # singolo caso

        # gruppo
        case.append(group(type_and_scale = "1", name = f"Case{index_case}a"))

        # question
        text =  f'<p>{text_presentazione_caso}</p>'
        text += f'<img src="{images_path}/presentazione_caso_{index_case}.png"/>'
        #text = f'<p>{text_presentazione_caso}</p><p>img src="presentazione_caso_{index_case}.png"</p><p><testopresentazionecaso></testopresentazionecaso></p><p><immaginepresentazionecaso></immaginepresentazionecaso></p>'
        case.append(question(type_and_scale = "L", name = f"HD{index_case}", text = text, mandatory = "Y")) # testo e immagine
        
        # answer decisione iniziale 1 (giusta)
        case.append(answer(name = "1", text = "<decisioneiniziale1>"))
        # answer decisione iniziale 0 (sbagliata)
        case.append(answer(name = "0", text = "<decisioneiniziale0>"))

        # question confidenza iniziale 1 "Quanto sei confidente della risposta?"
        case.append(question(type_and_scale = "F", name = f"CONF{index_case}", text = text_confidenza_iniziale, mandatory = "Y"))
        
        # subquestion confidenza iniziale
        case.append(sub_question(type_and_scale = "",name = "CONFI", text = "<confidenza>", mandatory="N"))
        
        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "(Per nulla confidente)"))
        # answer 2
        case.append(answer(name = "2", text = ""))
        # answer 3
        case.append(answer(name = "3", text = ""))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "(Totalemente confidente)"))

        # opzione iniziale 1
        text = f'<p>{list_opzioni_iniziali[0]}</p><p>{list_opzioni_iniziali[1]}</p><p>{list_opzioni_iniziali[2]}</p>'
        case.append(question(type_and_scale = "F", name = f"option{index_case}", text = text, mandatory = "Y"))

        # subquestion opzione iniziale
        case.append(sub_question(type_and_scale = "", name = "OPTI1", text = "option1", mandatory="N"))
        case.append(sub_question(type_and_scale = "", name = "OPTI3", text = "option2", mandatory="N"))
        case.append(sub_question(type_and_scale = "", name = "OPTI3", text = "option3", mandatory="N"))

        # answer
        case.append(answer(name = f'AO01', text = "Per niente"))
        case.append(answer(name = f'AO02', text = ""))
        case.append(answer(name = f'AO03', text = ""))
        case.append(answer(name = f'AO04', text = "Totalmente"))

        survey_cases_A.append(case)

        #######################################################################################################
        
        # GRUPPO B (con AI)
        case = []

        # gruppo
        case.append(group(type_and_scale = "2", name = f"Case{index_case}b"))

        # question
        text =  f'<p>{text_presentazione_supporto}</p>'
        text += f'<p>{text_presentazione_caso}</p>'
        text += f'<img src="{images_path}/presentazione_caso_{index_case}.png"/>'
        text += f'<p>{text_advice_1}</p>'
        text += f'<img src="{images_path}/immagineadvice1.png"/>'
        text += f'<p>{text_spiegazione_advice_1}</p>'
        text += f'<img src="{images_path}/immaginespiegazioneadvice1.png"/>'
        text += f'<p>{text_advice_2}</p>'
        text += f'<img src="{images_path}/immagineadvice2.png"/>'
        text += f'<p>{text_spiegazione_advice_2}</p>'
        text += f'<img src="{images_path}/immaginespiegazioneadvice2.png"/>'

        case.append(question(type_and_scale = "L", name = f"FHD{index_case}", text = text, mandatory = "Y")) # testo e immagine
        

        # answer decisione iniziale 1 (giusta)
        case.append(answer(name = "1", text = "<decisionefinale1>"))
        # answer decisione iniziale 0 (sbagliata)
        case.append(answer(name = "0", text = "<decisionefinale0>"))

        # question confidenza finale
        case.append(question(name = f"FCONF{index_case}", type_and_scale="F", text=f"{text_confidenza_finale}<testo valutazioni=""></testo>", mandatory="Y"))
        
        # sub_question confidenza finale
        case.append(sub_question(type_and_scale="", name="CONFF", text="<confidenza>", mandatory = "N"))
        
        
        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "per nulla confidente"))
        # answer 2
        case.append(answer(name = "2", text = ""))
        # answer 3
        case.append(answer(name = "3", text = ""))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "totalemente confidente"))

        # question opzione finale
        text = f"<p>[optionfinale1]</p><p>[optionfinale2]</p><p>[optionfinale3]</p><p><testo advice="" presentazione=""></testo></p>"
        case.append(question(name = f"Q{index_case:03}", type_and_scale = "F", text = text, mandatory = "N"))

        # subquestion opzione finale
        case.append(sub_question(type_and_scale="", name="OPTF1", text="option1", mandatory = "N"))
        case.append(sub_question(type_and_scale="", name="OPTF2", text="option2", mandatory = "N"))
        case.append(sub_question(type_and_scale="", name="OPTF3", text="option3", mandatory = "N"))

        # answer
        case.append(answer(name = f'AO01',text = "Per niente"))
        case.append(answer(name = f'AO02',text = ""))
        case.append(answer(name = f'AO03',text = ""))
        case.append(answer(name = f'AO04',text = "Totalmente"))


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
    print(list_opzioni_iniziali)
    print(list_opzioni_finali)
    print()
    

    # copio tutte le immagini nella cartella "images" in output
    copy_images_to_folder(file_path_input, images_path_dir)

    # svuoto output.tsv se esiste già
    with open(file_path_output, "w", encoding="utf-8") as f:
        pass
    
    # creo il file di output output.tsv
    create_survey(survey_settings, survey_cases_A, survey_cases_B, file_path_output)
    # creo il file di output output.txt
    convert_tsv_to_txt(file_path_output, file_path_output.replace(".tsv", ".txt"), delimiter="\t")




    











    
