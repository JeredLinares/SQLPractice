

import pandas as pd
import numpy as np

df = pd.read_csv("MDS_Facility_Level_2024_Q3.csv",chunksize=10000)

mds_items = pd.Series().to_numpy()
count = 0

for atom in df:
    print(count)

    mds_items = np.unique(np.concatenate((mds_items,atom.loc[:,"MDS Item Question/Description"].unique())))
    count += 1

pd.DataFrame(mds_items).to_csv("Distinct_MDS_Items2.csv",index=False)


