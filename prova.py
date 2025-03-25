import os
import csv
from survey_item import survey_item

# Definizione della cartella di input
cartella_input = r"C:\Development\Tesi\input"
output_file = "output_survey.txt"

# Funzione per generare domande da testi e immagini
def genera_questionario(cartella):
    items = []

    # Scansiona la cartella per sezioni
    for sezione in sorted(os.listdir(cartella)):
        sezione_path = os.path.join(cartella, sezione)
        if os.path.isdir(sezione_path):  # Controlla che sia una cartella

            # Legge file di testo e immagini nella sezione
            for file in sorted(os.listdir(sezione_path)):
                file_path = os.path.join(sezione_path, file)

                if file.endswith(".txt"):
                    with open(file_path, "r", encoding="utf-8") as f:
                        testo = f.read().strip()
                    
                    # Creazione dell'oggetto survey_item per la domanda
                    item = survey_item(
                        id=None, 
                        class_="Q",  # Domanda
                        type_and_scale="L",  # Tipo di domanda (Lista)
                        name=file.replace(".txt", ""),  # Nome derivato dal file
                        text=testo,
                        language="it",
                        mandatory="Y"
                    )
                    items.append(item)

                elif file.endswith((".jpg", ".png", ".jpeg")):
                    # Inserisce l'immagine come HTML
                    immagine_html = f'<img src="files/images/{file}" width="200px">'
                    
                    item = survey_item(
                        id=None,
                        class_="Q",
                        type_and_scale="L",
                        name=file.replace(".", "_"),  # Nome derivato dal file
                        text=immagine_html,
                        language="it",
                        mandatory="N"
                    )
                    items.append(item)

    return items

# Genera le domande dal dataset
items = genera_questionario(cartella_input)

# Scrive il file TXT con struttura compatibile LimeSurvey
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    
    # Scrive l'intestazione del file TXT
    header = [
        "id", "related_id", "class", "type/scale", "name", "relevance", 
        "text", "help", "language", "validation", "mandatory", "encrypted", "other"
    ]
    writer.writerow(header)

    # Scrive le domande generate
    for item in items:
        writer.writerow([
            item.id, item.related_id, item.class_, item.type_and_scale, 
            item.name, item.relevance, item.text, item.help, item.language, 
            item.validation, item.mandatory, item.encrypted, item.other
        ])

print(f"File {output_file} generato con successo!")
