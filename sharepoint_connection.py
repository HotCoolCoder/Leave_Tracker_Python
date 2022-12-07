import sharepy
from sharepy import connect
from sharepy import SharePointSession
import pandas as pd 
 
 
 
 
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





def create_connection():    #                     
    """
    For establishing connection to database
    """
    # server_name = config.server_name
    # db_name = config.db_name
    # db_conn = pyodbc.connect('Driver={SQL Server};'
    # 'Server={};'
    # 'Database={};'
    # 'Trusted_Connection=yes;').format(str(server_name),str(db_name))
    # testLog("Database Connection  Intiated")
    # start_time = time.time()
    # try:
    #     # server = '10.23.212.77,1433'
    #     server = config.server_name
    #     database = 'TaxHarvest'
    #     username = 'DevUser'
    #     password = '9SfzgS7Q4k'
    #     # fpkt12amdb1



    #     db_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    #     # db_conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};''Server=t12ewmdba;''Database=TaxHarvest;''UID=DevUser';'PWD= 9SfzgS7Q4k')
    #     connection_duration = start_time - time.time()
    #     testLog("Database Connection established in {} seconds".format(connection_duration))
    # except Exception as e:
    #     testLog("Error in Database Connection : {}".format(e))
    # return db_conn









#import json 
def get_sharepoint_connection():
    SPUrl = "https://assetmark-my.sharepoint.com"
    # username ="Praveen.Singh@assetmark.com"
    # password ="Welcome208435!" 
    username = "Paritosh.Sharma@assetmark.com"
    password = "Welcome208319!"

    conn = sharepy.connect(SPUrl,username,password)
    return conn


#convert excel into dataframe
# month_name='NOV'
# try:
#     df=pd.read_excel(local_file_path,sheet_name=month_name)
#     print('dataframe creation succesfull for Nov month data')
#     print('the length of df generated : ', len(df))
#     #print(df)
# except Exception as e:
#     print(e)
    