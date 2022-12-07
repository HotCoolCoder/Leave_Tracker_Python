import pandas as pd

def read_file_and_create_dict_of_dfs():
    """
    This function will read the excel file and returns a dictionary containing {Month:Df}
    """
    dict_dfs = pd.read_excel('QA_Leave_Tracker_2022.xlsx',sheet_name=['JAN','FEB','MARCH','APRIL','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC'],header=1)
    return dict_dfs