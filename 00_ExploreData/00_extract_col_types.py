'''
Extract csv column types based on first 1000 rows
JD Linares
Created: 2025 01 12
'''

import sys
import pandas as pd


try:
    data_chunk = pd.read_csv(sys.argv[1],chunksize=1000)
except:
    print("Must use a parameter with CSV filename")

data_chunk.get_chunk().dtypes.to_csv("cols_"+sys.argv[1])

