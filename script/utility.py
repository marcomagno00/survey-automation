from dataclasses import dataclass, fields
from openpyxl import Workbook
import csv
import os


def give_first_txt_from_folder(folder_path):
    # Get the first file from the folder
    for file_name in os.listdir(folder_path):
        # check if file ends with .txt
        if file_name.endswith(".txt"):
            # return the first .txt file found
            return os.path.join(folder_path, file_name)
    return None

def read_first_line_from_txt(file_path):
    if file_path is None:
        return None
    # Open the file and read the first line
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline().strip()
    return first_line

def write_dataclass_to_excel(dataclass_obj, filename):
    
    # Create a new workbook and get the active worksheet
    workbook = Workbook()
    worksheet = workbook.active

    # Write headers (the alias if present, otherwise the field name)
    for col_index, field_info in enumerate(fields(dataclass_obj), start=1):
        alias = field_info.metadata.get("alias", field_info.name)
        worksheet.cell(row=1, column=col_index, value=alias)
        
    # Write the dataclass object's values
    for col_index, field_info in enumerate(fields(dataclass_obj), start=1):
        value = getattr(dataclass_obj, field_info.name)
        worksheet.cell(row=2, column=col_index, value=value)

    # Save the workbook
    workbook.save(filename)

def write_dataclass_to_tsv(dataclass_obj, filename):
    # Extract aliases (or field names if no alias)
    header = []
    row = []
    for field_info in fields(dataclass_obj):
        alias = field_info.metadata.get("alias", field_info.name)
        header.append(alias)
        row.append(getattr(dataclass_obj, field_info.name))
    
    # Write to CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as tsv_file:
        writer = csv.writer(tsv_file, delimiter="\t")
        writer.writerow(header)  # Write header row
        writer.writerow(row)     # Write data row

def add_row_to_tsv(dataclass_obj, filename):
    # Open the TSV file in append mode
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter="\t")

        # If the file is empty, write the headers first
        if file.tell() == 0:
            headers = [field_info.metadata.get("alias", field_info.name) for field_info in fields(dataclass_obj)]
            writer.writerow(headers)

        # Write the values of the dataclass instance as a new row
        row = [getattr(dataclass_obj, field.name) for field in fields(dataclass_obj)]
        writer.writerow(row)