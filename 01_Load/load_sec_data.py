'''
Load csv to new database
JD Linares
Create: 2025 01 04
'''


import pandas as pd
import mysql.connector

df = pd.read_csv("data.csv",sep="\t")

connection = mysql.connector.connect(host="localhost",user="diego")
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


for row in df.itertuples():
    # May need a NULL if no int for sic
    sic = 'NULL'
    try: 
        sic = int(row[4])
    except ValueError:
        print("NULL value for SIC")


    print()
    print(row[3])
    print(sic)
    print(row[9])
#    print(row[10])     #Mostly empty second address line
    print(row[7])
    print(row[6])  
    print(row[8])

    statement = f'''INSERT INTO companies VALUES ("{row[3]}",{sic},+"{row[9]}","{row[7]}","{row[6]}","{row[8]}")'''
    print(statement)

    cur.execute(statement)
    print(cur.fetchall())



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
