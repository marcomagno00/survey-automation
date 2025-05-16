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
    
    # dir path input
    file_path_input = r"input/"
    file_path_presentazione_caso = r"input/Presentazione Caso"
    file_path_advice = r"input/Advice"
    file_path_confidenza_iniziale = r"input/Confidenza Iniziale"
    file_path_confidenza_finale = r"input/Confidenza Finale"
    file_path_decisioni_iniziali = r"input/Decisioni Iniziali"
    file_path_decisioni_finali = r"input/Decisioni Finali"
    file_path_opzioni_finali = r"input/Opzioni Finali"
    file_path_presentazione_supporto = r"input/Presentazione Supporto"

    # path immagini per l'upload su Limesurvey
    images_path = r"{SURVEYRESOURCESURL}/images"

    # testi di input
    text_advice_1 = read_first_line_from_txt("input/Advice/testoadvice1.txt")
    text_advice_2 = read_first_line_from_txt("input/Advice/testoadvice2.txt")
    text_spiegazione_advice_1 = read_first_line_from_txt("input/Advice/spiegazioneadvice1.txt")
    text_spiegazione_advice_2 = read_first_line_from_txt("input/Advice/spiegazioneadvice2.txt")
    
    text_confidenza_finale = read_first_line_from_txt(give_first_txt_from_folder(file_path_confidenza_finale))
    text_confidenza_iniziale = read_first_line_from_txt(give_first_txt_from_folder(file_path_confidenza_iniziale))
    text_presentazione_caso = read_first_line_from_txt(give_first_txt_from_folder(file_path_presentazione_caso))
    text_presentazione_supporto = read_first_line_from_txt(give_first_txt_from_folder(file_path_presentazione_supporto))

    list_decisioni_iniziali = read_all_lines_from_txt(give_first_txt_from_folder(file_path_decisioni_iniziali))
    list_decisioni_finali = read_all_lines_from_txt(give_first_txt_from_folder(file_path_decisioni_finali))
    list_opzioni_finali = read_all_lines_from_txt(give_first_txt_from_folder(file_path_opzioni_finali))



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

    # NUMERO DI CASI

    # conto le immagini nella cartella di Presentazione Caso (e le rinomino)
    # chiedo quanti casi voglio generare
    # li confronto con il numero di immagini presenti nella cartella di Presentazione Caso
    # se:
    # num_immagini_presentazione_caso <= max_index_case -> prendo in ordine tutte le immagini disponibili e i casi rimanenti non avranno l'immagine
    # num_immagini_presentazione_caso > max_index_case -> prendo le immagini in ordine
    
    print()
    print(r"** NUMERO DI CASI **")
    
    # chiedo quanti casi voglio generare
    while True:
        try:
            max_index_case = int(input("Inserisci il numero di casi che vuoi generare (un gruppo): "))
            break  # Uscita dal ciclo se l'input è valido
        except ValueError:
            print("Devi inserire un numero intero di casi")


    # IMMAGINI PRESENTAZIONE CASO

    num_immagini_presentazione_caso = count_images_in_folder(file_path_presentazione_caso)
    list_immagini_presentazione_caso = get_images_from_folder(file_path_presentazione_caso)
    print(list_immagini_presentazione_caso)
    
    print()
    print(r"** IMMAGINI PRESENTAZIONE CASO **")
    
    if num_immagini_presentazione_caso == 0:
        # se non ci sono immagini nella cartella di presentazione caso
        print("Nessuna immagine trovata nella cartella di presentazione caso.")
        
    else:
        # rinomino le immagini presenti nella cartella di presentazione caso
        print(f"Rinomino le {num_immagini_presentazione_caso} immagini presenti nella cartella di presentazione caso:")
        rename_images_in_folder(file_path_presentazione_caso, "presentazione_caso_")
    


    
    # SURVEY

    index_case = 1 # indice per contare e visualizzare i casi (1, 2, 3...)
    max_index_case = max_index_case # numero di casi richiesti
    survey_cases = [] # lista di "survey_item" che contiene i casi A e B
    
    
    while (index_case <= max_index_case):

        
        # indici specifici per tracciare i gruppi (per la parte di logica)
        a_index = index_case * 2 - 1
        b_index = index_case * 2

        # path immagine da inserire (se presente)
        if index_case <= num_immagini_presentazione_caso:
            image_path = f'<img src="{images_path}/{list_immagini_presentazione_caso[index_case - 1]}"/>'
        else:
            image_path = ""

        ## CASE A
        case = []

        # group
        case.append(group(type_and_scale = a_index, name = f"Case{index_case}a", text = text_presentazione_caso))
        
        # question
        text =  f'<p>{text_presentazione_caso}</p>'
        text += image_path 
        case.append(question(type_and_scale = "L", name = f"HD{a_index}", text = text, mandatory = "Y"))
        
        # first answer (correct)
        first_answer = list_decisioni_iniziali[0]
        case.append(answer(name = "1", text = first_answer))

        # remaining answers (wrong)
        remaining_answers = list_decisioni_iniziali[1:]
        for option in remaining_answers:
            case.append(answer(name = "0", text = option)) 

        # question confidenza iniziale 1 "Quanto sei confidente della risposta?"
        case.append(question(type_and_scale = "F", name = f"CONF{a_index}", text = text_confidenza_iniziale, mandatory = "Y"))
        
        # subquestion confidenza iniziale
        case.append(sub_question(type_and_scale = "", name = "CONFI", text = "Confidenza", mandatory="N"))
        
        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "(Per nulla confidente)"))
        # answer 2
        case.append(answer(name = "2", text = "(Poco confidente)"))
        # answer 3
        case.append(answer(name = "3", text = "(Abbastanza confidente)"))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "(Totalemente confidente)"))
        
        survey_cases.append(case)

        ## CASE B
        case = []

        # group
        case.append(group(type_and_scale = b_index, name = f"Case{index_case}b", text = text_presentazione_caso))

        # question
        text =  f'<p>{text_presentazione_supporto}</p>'
        text += f'<p>{text_presentazione_caso}</p>'
        text += image_path 
        text += f'<p>{text_advice_1}</p>'
        text += f'<img src="{images_path}/immagineadvice1.png"/>'
        text += f'<p>{text_spiegazione_advice_1}</p>'
        text += f'<img src="{images_path}/immaginespiegazioneadvice1.png"/>'
        text += f'<p>{text_advice_2}</p>'
        text += f'<img src="{images_path}/immagineadvice2.png"/>'
        text += f'<p>{text_spiegazione_advice_2}</p>'
        text += f'<img src="{images_path}/immaginespiegazioneadvice2.png"/>'
        case.append(question(type_and_scale = "L", name = f"FHD{b_index}", text = text, mandatory = "Y"))
        
        # prima risposta (corretta)
        first_answer = list_decisioni_iniziali[0]
        case.append(answer(name = "1", text = first_answer))

        # risposte rimanenti (sbagliate) (in questo caso ci sono 2 riposte iniziali, una giusta e una sbagliata)
        remaining_answers = list_decisioni_iniziali[1:]
        for option in remaining_answers:
            case.append(answer(name = "0", text = option)) 

        # question confidenza iniziale 1 "Quanto sei confidente della risposta?"
        case.append(question(type_and_scale = "F", name = f"CONF{b_index}", text = text_confidenza_iniziale, mandatory = "Y"))
        
        # subquestion confidenza iniziale
        case.append(sub_question(type_and_scale = "",name = "CONFI", text = "Confidenza", mandatory="N"))
        
        # answer 1 "per nulla confidente"
        case.append(answer(name = "1", text = "(Per nulla confidente)"))
        # answer 2
        case.append(answer(name = "2", text = "(Poco confidente)"))
        # answer 3
        case.append(answer(name = "3", text = "(Abbastanza confidente)"))
        # answer 4 "totalemente confidente"
        case.append(answer(name = "4", text = "(Totalemente confidente)"))

        # question opzione finale
        text = ""
        for option in list_opzioni_finali:
            text += f"<p>{option}</p>"
        case.append(question(name = f"Q{b_index:03}", type_and_scale = "F", text = text, mandatory = "N"))

        # subquestion opzione finale
        for i, option in enumerate(list_opzioni_finali, 1):
            case.append(sub_question(type_and_scale="", name = f"OPTF{i}", text = option, mandatory = "N"))

        # answer
        case.append(answer(name = f'AO01',text = "Per niente"))
        case.append(answer(name = f'AO02',text = "Poco"))
        case.append(answer(name = f'AO03',text = "Abbastanza"))
        case.append(answer(name = f'AO04',text = "Totalmente"))

        survey_cases.append(case)
        index_case += 1



    # OUTPUT 
    
    print()
    
    # print dei testi letti
    print(r"** TESTI DI INPUT **")
    print(r"Testo presentazione caso:", text_presentazione_caso)
    print(r"Testo presentazione supporto:", text_presentazione_supporto)
    print(r"Testo confidenza iniziale:", text_confidenza_iniziale)
    print(r"Testo confidenza finale:", text_confidenza_finale)
    print(r"Testo advice 1:", text_advice_1)
    print(r"Testo advice 2:", text_advice_2)
    print(r"Testo spiegazione advice 1:", text_spiegazione_advice_1)
    print(r"Testo spiegazione advice 2:", text_spiegazione_advice_2)

    print()

    # print delle risposte
    print(r"** RISPOSTE DI INPUT **")
    print(r"Risposte iniziali:", list_decisioni_iniziali)
    print(r"Risposte finali:", list_decisioni_finali)

    print()

    # print dei dati letti
    print(r"** DATI DI INPUT **")
    print(r"Numero di casi richiesti:", max_index_case)
    print(r"Numero di immagini in Presentazione Caso:", num_immagini_presentazione_caso)
    print(r"Numeri di casi totali generati (A e B):", len(survey_cases))
    if max_index_case >= num_immagini_presentazione_caso:
        print(r"Numero di casi senza immagine:", max_index_case - num_immagini_presentazione_caso)
    if max_index_case < num_immagini_presentazione_caso:
        print(r"Numero di immagini non utilizzate:", num_immagini_presentazione_caso - max_index_case)
    
    print()
    print(r"** FILE DI OUTPUT **")
    
    
    # copio tutte le immagini nella cartella "images" in output, per poter uploadarle su Limesurvey più comodamente
    copy_images_to_folder(file_path_input, images_path_dir)
    print(r"Immagini copiate nella cartella:", images_path_dir)


    # svuoto output.tsv se esiste già
    with open(file_path_output, "w", encoding="utf-8") as f:
        pass
    
    # creo il file di output output.tsv
    create_survey(survey_settings, survey_cases, file_path_output)
    # creo il file di output output.txt
    convert_tsv_to_txt(file_path_output, file_path_output.replace(".tsv", ".txt"), delimiter="\t")

    print()




    











    
