import sqlalchemy

def create_engine():
    """
    Engine to be created for bulk insertion into database 
    """
    # testLog("Database Engine Initiated")
    server_name = 'DESKTOP-T3T90T0\SQLEXPRESS'
    db_name = 'leave_tracker'
    con_string = 'mssql+pyodbc://@' + server_name + '/'+ db_name + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'           #get this connection string from json file
#/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.0.so.1.1
    # try:
    engine = sqlalchemy.create_engine(con_string,pool_pre_ping=True)
    #     testLog("Database Engine Created")
    # except Exception as e:
    #     testLog(str(e))
    return engine