import os


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


def read_flags_from_input():

    # presentazione caso
    testopresentazionecaso = input_folder + "/PresentazioneCaso/"
    immaginepresentazionecaso

    # confidenza iniziale
    testoconfidenzainiziale

    # opzioni iniziali
    optioninziale1
    optioniniziale2 
    optioniniziale3

    # presentazione supporto
    testopresentazionesupporto

    # advice
    testoadvice1
    immagineadvice1
    spiegazioneadvice1
    testoadvice2
    immagineadvice2
    spiegazioneadvice2

    # confidenza finale
    testoconfidenzafinale

    # opzioni finali
    optionfinale1
    optionfinale2
    optionfinale3

# creo Case A (caso privo di supporto AI)



# creo Case B (caso che implementa supporto AI)