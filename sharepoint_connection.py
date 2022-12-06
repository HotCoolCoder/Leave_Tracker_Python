 # try:
        #     data_added = df.to_sql('TestAPLNavIDs', con=engine , if_exists = 'append' , index = False) 
        #     if data_added==0:
        #         testLog("Error no data added in TestNav")
        #     else:
        #         testLog("Data added in Table TestNav")
        #         testLog("Number of Records added in TestNav are : %s"%len(df))# get the DB name from JSON for bulk insertion of data
        # except Exception as e:

        #     testLog(e)
        
        
        
        
        
def create_engine():
    """
    Engine to be created for bulk insertion into database 
    """
#     testLog("Database Engine Initiated")
#     server_name = config.server_name
#     db_name = config.db_name
#     #con_string = 'mssql+pyodbc://@' + server_name + '/'+ db_name + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'           #get this connection string from json file
# #/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.0.so.1.1
#     try:
#         engine = sqlalchemy.create_engine(con_string,pool_pre_ping=True)
#         testLog("Database Engine Created")
#     except Exception as e:
#         testLog(str(e))
#     return engine




