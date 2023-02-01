import csv
import string
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from IPython.display import HTML

def readCSV(csvfile):
    rows = []
    with open(csvfile, 'r') as file:
        csvReader = csv.reader(file)
        header = next(csvReader)
        for row in csvReader:
            rows.append(row)

    file.close()
    return rows

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

def is_csv(file):
    try:
        with open(file, newline='') as csvfile:
            start = csvfile.read(4096)

            if not all([c in string.printable or c.isprintable() for c in start]):
                return False
            check = csv.Sniffer().sniff(start)
            return True
    except csv.Error:
        return False

def csv_to_html(df):
    # https://www.geeksforgeeks.org/how-to-render-pandas-dataframe-as-html-table/
    dataframe = pd.read_csv(file_path)

    html = dataframe.to_html()

    text_file = open("index.html", "w")
    text_file.write(html)
    text_file.close()

if (is_csv(file_path)):
    csv_to_html(file_path)
else:
    print("Please select CSV file")

