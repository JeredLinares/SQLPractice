'''
Load tables for nursing home mds data in database
JD Linares
2025 01 11
'''

import mysql.connector
import sys
import pandas as pd

cxn = mysql.connector.connect(user='diego', host='localhost', database='nh_mds')

df_chunks = pd.read_csv("/data/nh_mds/Facility_Level_MDS_Frequency_Q3_2024.csv",chunksize=1000)

chunk_num = 0
for df in df_chunks:
    for index,row in df.iterrows():
        query_string = "INSERT INTO 2024_q3 VALUES ("
        for item in row.keys():
            query_string += "'" + str(row[item]).replace("'","") + "',"
        #print()
        query_string = query_string[0:-1]
        query_string += ")"
        #print(query_string)
        #print()

        cursor = cxn.cursor()
        cursor.execute(query_string)
        cursor.close()
        cxn.commit()

    print(chunk_num,end='\r')
    chunk_num+=1

cxn.close()


