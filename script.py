import numpy as np
import pandas as pd
import sys
import os
import tkinter as tk
from tkinter import filedialog

from operation import getAverageMarks

def browseFiles():
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename(title="Select excel Data", initialdir="/", filetypes=[("Excel files", "*.xlsx")])
    print(f"File browsed '{filePath}'")
    return filePath


# 1. Get file 
excelPath = ""
if (len(sys.argv)) > 1:
    excelPath = sys.argv[1]
else:
    excelPath = browseFiles()


# 2. Check file conditions
if not os.path.exists(excelPath):
    print(f"excel Path '{excelPath}' not exist")
    sys.exit()


# 3. Transform excel into dataframe
#       Avoid generating index in rows
print(f"Reading excel from '{excelPath}'")
df = pd.read_excel(excelPath, index_col=0) 
print(f"Data loaded:\n{df}")

print("\n")


# 4. Do operations
newDf = getAverageMarks(df)
print(f"With Average Marks:\n{newDf}")


# 5. Generate file in /data
dirName = "data"
fileName = "result"
os.makedirs(dirName, exist_ok=True) # ensure dir exist

outputFilePath = os.path.join(dirName, f"{fileName}.xlsx")
newDf.to_excel(outputFilePath)
print(f"Result created in {outputFilePath}")



