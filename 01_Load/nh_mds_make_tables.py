'''
Make tables for nursing home mds data in database
JD Linares
2025 01 11
'''

import mysql.connector

cxn = mysql.connector.connect(user='diego', host='localhost', database='nh_mds')
cursor = cxn.cursor()


make_table_2023_q4 = ("CREATE TABLE 2023_q4"
    "("
#    "entry_id int(11) NOT NULL AUTO_INCREMENT,"
    "ccn VARCHAR(128),"
    "provider_name VARCHAR(128),"
    "city VARCHAR(128),"
    "state VARCHAR(128),"
    "zip_code VARCHAR(128),"
    "report_date VARCHAR(128),"
    "mds_code_item VARCHAR(256),"
    "mds_response VARCHAR(256),"
    "overall_percent VARCHAR(256),"
    "total_residents VARCHAR(256),"
    "short_stay_percent VARCHAR(64),"
    "short_stay_residents VARCHAR(64),"
    "long_stay_percent VARCHAR(64),"
    "long_stay_residents VARCHAR(64)"
#    "PRIMARY KEY(entry_id)"
    ")")

#print(make_table_2023_q4)
cursor.execute(make_table_2023_q4)




make_table_2024_q1 = ("CREATE TABLE 2024_q1"
    "("
#    "entry_id int(11) NOT NULL AUTO_INCREMENT,"
    "ccn VARCHAR(128),"
    "provider_name VARCHAR(128),"
    "city VARCHAR(128),"
    "state VARCHAR(128),"
    "zip_code VARCHAR(128),"
    "report_date VARCHAR(128),"
    "mds_code_item VARCHAR(256),"
    "mds_response VARCHAR(256),"
    "overall_percent VARCHAR(256),"
    "total_residents VARCHAR(256),"
    "short_stay_percent VARCHAR(64),"
    "short_stay_residents VARCHAR(64),"
    "long_stay_percent VARCHAR(64),"
    "long_stay_residents VARCHAR(64)"
#    "PRIMARY KEY(entry_id)"
    ")")

#print(make_table_2024_q1)
cursor.execute(make_table_2024_q1)


make_table_2024_q2 = ("CREATE TABLE 2024_q2"
    "("
#    "entry_id int(11) NOT NULL AUTO_INCREMENT,"
    "ccn VARCHAR(128),"
    "provider_name VARCHAR(128),"
    "city VARCHAR(128),"
    "state VARCHAR(128),"
    "zip_code VARCHAR(128),"
    "fips_county_code VARCHAR(64),"
    "county_name VARCHAR(128),"
    "report_date VARCHAR(128),"
    "mds_code_item VARCHAR(256),"
    "mds_response VARCHAR(256),"
    "overall_percent VARCHAR(256),"
    "total_residents VARCHAR(256),"
    "short_stay_percent VARCHAR(64),"
    "short_stay_residents VARCHAR(64),"
    "long_stay_percent VARCHAR(64),"
    "long_stay_residents VARCHAR(64)"
#    "PRIMARY KEY(entry_id)"
    ")")

#print(make_table_2024_q2)
cursor.execute(make_table_2024_q2)


make_table_2024_q3 = ("CREATE TABLE 2024_q3"
    "("
#    "entry_id int(11) NOT NULL AUTO_INCREMENT,"
    "ccn VARCHAR(128),"
    "provider_name VARCHAR(128),"
    "city VARCHAR(128),"
    "state VARCHAR(128),"
    "zip_code VARCHAR(128),"
    "fips_county_code VARCHAR(64),"
    "county_name VARCHAR(128),"
    "report_date VARCHAR(128),"
    "mds_code_item VARCHAR(256),"
    "mds_response VARCHAR(256),"
    "overall_percent VARCHAR(256),"
    "total_residents VARCHAR(256),"
    "short_stay_percent VARCHAR(64),"
    "short_stay_residents VARCHAR(64),"
    "long_stay_percent VARCHAR(64),"
    "long_stay_residents VARCHAR(64)"
#    "PRIMARY KEY(entry_id)"
    ")")

#print(make_table_2024_q3)
cursor.execute(make_table_2024_q3)





cursor.close()
cxn.close()


