import pandas as pd

# Axis for pandas
AXIS_COLUMN = 0
AXIS_ROW = 1

# New row's and column's names
NEW_COLUMN_NAME = "Mark Average"
NEW_ROW_NAME = "Asignature Average"

def getAverageMarks(df):
    currentDf = df.copy()  # avoid overwrite df

    # Get Individual Person Average
    # currentDf[NEW_COLUMN_NAME] = currentDf.sum(axis=AXIS_ROW, numeric_only=True) / currentDf.select_dtypes(include="number").count(axis=1) # manual mean
    currentDf[NEW_COLUMN_NAME] = currentDf.mean(axis=AXIS_ROW, numeric_only=True)  
    
    # Get Asignature Average
    # asignatureAverage = currentDf.sum(axis=AXIS_COLUMN, numeric_only=True) / currentDf.select_dtypes(include="number").count(axis=0)  # manual mean
    asignatureAverage = currentDf.mean(axis=AXIS_COLUMN, numeric_only=True)
    newDf = pd.concat(
        [currentDf, pd.DataFrame([asignatureAverage], index=[NEW_ROW_NAME])],
        ignore_index=False
    )

    return newDf