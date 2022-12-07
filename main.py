import download_file,sharepoint_connection,file_preprocessing,read_file_and_create_dict_of_dfs,Bulk_insert

import toolz,pandas as pd

download_file.download_sharepoint_file(sharepoint_connection.get_sharepoint_connection())

df = pd.read_excel(r'C:\Users\Paritosh.Sharma\Downloads\test_file.xlsx',sheet_name='NOV')

processed_df = file_preprocessing.file_preprocessing(df)
print(processed_df)
# dict_processed_dfs = toolz.valmap(file_preprocessing.file_preprocessing(), read_file_and_create_dict_of_dfs.read_file_and_create_dict_of_dfs())

# toolz.valmap(Bulk_insert.bulk_insert(),dict_processed_dfs)