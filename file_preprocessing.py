import pandas as pd

def file_preprocessing(df:pd.DataFrame)->pd.DataFrame:
    # df=dataframe_creation()
    col_list=['Emp_Id','Emp_name','BD_1','BD_2','BD_3','BD_4','BD_5','BD_6','BD_7','BD_8','BD_9','BD_10',
        'BD_11','BD_12','BD_13','BD_14','BD_15','BD_16','BD_17','BD_18','BD_19','BD_20','BD_21','BD_22','BD_23','BD_24',
        'BD_25','BD_26','BD_27','BD_28','BD_29','BD_30','BD_31']  #To match with DB Schema
    push_db=pd.DataFrame(columns=col_list)       #temp df
    df.drop(['S.No.','Unnamed: 3'],axis=1,inplace=True)
    l1=df.columns.tolist() #to store the column names in a list
    
    #to handle weekends
    df.loc[:,[i for i in l1 if (i.startswith('Saturday') or i.startswith('Sunday'))]]='WH'
    df.fillna('Y', inplace=True)  #replacing nan with 'Y'
    
    #handle removal of legends and team location name from Name attribute rows
    df=df[(df.Name!='Y') & (df.Name!='Gurgaon Team') & (df.Name!='Chennai Team') & (df.Name!='Interns') & (df.Name!='Mexico Team') & (df.Name!='LEGEND') & (df.Name!='Planned Leave') &  (df.Name!='Sick Leave') & (df.Name!='Unplanned Leave') & (df.Name!='Public Holiday')]
    df = df.reset_index(drop=True).rename(columns={'Name':'Emp name'})
    
    #Location list to handle the location of resources
    l3=['Gurgaon']*26
    l3.extend(['Chennai']*9)
    l3.extend(['Intern']*3)
    l3.extend(['Mexico']*24)
    
    #Handle of varying month dates like 28,30,31
    if len(df.columns)==32:
        df.insert(loc=len(df.columns),column='BD_31',value=['']*len(df.index))
    elif len(df.columns)==28:
        df = df.assign(BD_29=['']*len(df.index), BD_30=['']*len(df.index), BD_31=['']*len(df.index))
    
    df.columns=push_db.columns                      #assigning name of temp df to our df to match with table schema column names.
    
    month_name='NOV'    #month of script run
    year='2022'  #year of script run
    df=df.assign(Month=[month_name]*len(df.index), Year=[year]*len(df.index),Location=l3)
    df = df.astype(str).replace(r'\.0$', '', regex=True)
    # df.replace('Working from Mexico','Y',inplace=True)  #handle PH of India but working day for Mexico
    # Date columns
    date_columns=['BD_1','BD_2','BD_3','BD_4','BD_5','BD_6','BD_7','BD_8','BD_9','BD_10',
         'BD_11','BD_12','BD_13','BD_14','BD_15','BD_16','BD_17','BD_18','BD_19','BD_20','BD_21','BD_22','BD_23','BD_24',
          'BD_25','BD_26','BD_27','BD_28','BD_29','BD_30','BD_31']
    
    #calculation of present and absent of a resource in a month
    df['Present_count'] = (df[date_columns] == 'Y').sum(axis=1) + (df[date_columns] == 'Working from Mexico').sum(axis=1)             
    df['Absent_count'] = (df[date_columns] == 'PL').sum(axis=1) + (df[date_columns] == 'UL').sum(axis=1) + (df[date_columns] == 'SL').sum(axis=1)
    df['Public_holidays'] = (df[date_columns] == 'PH').sum(axis=1)
    df['Other_holidays'] = (df[date_columns] == 'Travelling to India').sum(axis=1)
    df['Absent_date']=df[date_columns].applymap(lambda x: 'PL' in x).dot(df[date_columns].columns + ',').str[:-1] + ',' + df[date_columns].applymap(lambda x: 'UL' in x).dot(df[date_columns].columns + ',').str[:-1] + df[date_columns].applymap(lambda x: 'SL' in x).dot(df[date_columns].columns + ',').str[:-1]
    df['Absent_date']=df['Absent_date'].str.lstrip(',')
    df['Absent_date']=df['Absent_date'].str.rstrip(',')
    df.to_excel(r'C:\Users\Admin\Downloads\df1_file.xlsx',index=False)
    return df