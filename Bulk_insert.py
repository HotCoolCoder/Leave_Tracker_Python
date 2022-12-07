import pandas as pd

def bulk_insert(df:pd.DataFrame,engine):
    """
    This function is used fro bulk insertion of dataframe into the DB
    """
    df.to_sql('attendance', con=engine , if_exists = 'append' , index = False) 
    # if data_added==0:
    #     testLog("Error no data added in TestNav")
    # else:
    #     testLog("Data added in Table TestNav")
    #     testLog("Number of Records added in TestNav are : %s"%len(df))# get the DB name from JSON for bulk insertion of data