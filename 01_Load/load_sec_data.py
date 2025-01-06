'''
Load csv to new database
JD Linares
Create: 2025 01 04
'''

import numpy as np
import pandas as pd
import mysql.connector

df = pd.read_csv("data.csv",sep="\t")
#print(df.info())


connection = mysql.connector.connect(host="localhost",user="diego") #Do NOT add pw here
cur = connection.cursor()
cur.execute("USE sec")
cur.fetchall()

# Only call once
cur.execute("CREATE TABLE companies "\
        "(company_name VARCHAR(255), "\
        "sic INT,"\
        "address VARCHAR(255),"\
        "city VARCHAR(255),"\
        "state VARCHAR(255),"\
        "zip_code VARCHAR(255))")
cur.fetchall()


print()

for row in df.itertuples():

    print()
    print(row)
    print()

    # May need a NULL if no int for sic
    sic = None
    try: 
        sic = int(row[4])
    except ValueError:
        print("NULL value for SIC")


    address = ""
    if row[9] is not np.nan:
        address = row[9]

    city = ""
    if row[7] is not np.nan:
        city = row[7]

    state = ""
    print(row[6])
    if row[6] is not np.nan:
        state = row[6]

    zip_code = ""
    if row[8] is not np.nan:
        zip_code = row[8]


    print()
    print(row[3])
    print(sic)
    print(address)
#    print(row[10])     #Mostly empty second address line
    print(city)        #row[7]
    print(state)  
    print(zip_code)

    statement = "INSERT INTO companies VALUES (%s,%s,%s,%s,%s,%s)"
    statement_data = (row[3],sic,address,city,state,zip_code)
    print(statement)

    cur.execute(statement,statement_data)
    print(cur.fetchall())


connection.commit()
connection.close()


'''
Index([
'adsh', 'cik', 'name', 'sic', 'countryba',
'stprba', 'cityba', 'zipba', 'bas1', 'bas2', 
'baph', 'countryma', 'stprma', 'cityma', 'zipma',
'mas1', 'mas2', 'countryinc', 'stprinc', 'ein', 
'former', 'changed', 'afs', 'wksi', 'fye',
'form', 'period', 'fy', 'fp', 'filed', 
'accepted','prevrpt', 'detail', 'instance', 'nciks', 
'aciks'],
      dtype='object')
'''
