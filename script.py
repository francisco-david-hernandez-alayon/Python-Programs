import numpy as np
import pandas as pd
import sys
import os
import tkinter as tk
from tkinter import filedialog

def browseFiles():
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename(title="Select excel Data", initialdir="/", filetypes=[("Excel files", "*.xlsx")])
    print(f"File browsed '{filePath}'")
    return filePath


# Get file 
excelPath = ""
if (len(sys.argv)) > 1:
    excelPath = sys.argv[1]
else:
    excelPath = browseFiles()

# Check file conditions
if not os.path.exists(excelPath):
    print(f"excel Path '{excelPath}' not exist")
    sys.exit()


# Read excel
print(f"Reading excel from '{excelPath}'")
df = pd.read_excel(excelPath)
print(df)



