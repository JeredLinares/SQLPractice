'''
Load SEC 2024 Q3 data to database
JD Linares
Created: 2025 01 04
'''

import pandas as pd
import mysql.connector

companies = pd.read_csv("data.csv",sep="\t")
print(companies.head())




