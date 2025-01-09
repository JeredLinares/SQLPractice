'''
Load subset of  CMS MDS for nursing homes from year 2019-2024
Save in pickle for export to sql
JD Linares
Created: 2025 01 07
Updated: 2025 01 08
'''

import pandas as pd

folder_loc = "../00_Data/cms/"
file_names = ("MDS_Nov2019.csv",
        "MDS_Nov2020.csv",
        "MDS_Nov2021.csv",
        "MDS_Nov2022.csv",
        "MDS_Nov2023.csv",
        "MDS_Nov2024.csv"
        )

dfs = list()

for element in file_names:
    print(folder_loc+element)
    df = pd.read_csv(folder_loc+element,encoding="latin1",low_memory=False)
    print(df.columns)
    print(df.dtypes)
    print(df.shape)
    dfs.append(df)

print(len(dfs))     # NOTE: dfs is a list, not a df
print()

# Match Variables from each year
# 2019
'''
PROVNUM                    object
PROVNAME                   object
ADDRESS                    object
CITY                       object
STATE                      object
ZIP                         int64
MSR_CD                      int64
MSR_DESCR                  object
STAY_TYPE                  object
Q1_MEASURE_SCORE          float64
Q1_MEASURE_FN             float64
Q2_MEASURE_SCORE          float64
Q2_MEASURE_FN             float64
Q3_MEASURE_SCORE          float64
Q3_MEASURE_FN             float64
Q4_MEASURE_SCORE          float64
Q4_MEASURE_FN             float64
MEASURE_SCORE_4QTR_AVG    float64
SCORE4QTR_FN              float64
FIVE_STAR_MSR              object
MEASURE_PERIOD             object
FILEDATE                   object

'''
# NOTE: .loc is the correct way to call the data, not "chained indexing"
df_2019 = dfs[0].loc[:,
        [
            "PROVNUM",
            "MSR_DESCR",
            "STAY_TYPE",
            "Q1_MEASURE_SCORE",
            "Q2_MEASURE_SCORE",
            "Q3_MEASURE_SCORE",
            "Q4_MEASURE_SCORE",
            "MEASURE_SCORE_4QTR_AVG"
    ]]
df_2019.loc[:,"year"]="2019"

print(df_2019)



# 2020
'''
Federal Provider Number                      object
Provider Name                                object
Provider Address                             object
Provider City                                object
Provider State                               object
Provider Zip Code                             int64
Measure Code                                  int64
Measure Description                          object
Resident type                                object
Q1 Measure Score                            float64
Footnote for Q1 Measure Score               float64
Q2 Measure Score                            float64
Footnote for Q2 Measure Score               float64
Q3 Measure Score                            float64
Footnote for Q3 Measure Score               float64
Q4 Measure Score                            float64
Footnote for Q4 Measure Score               float64
Four Quarter Average Score                  float64
Footnote for Four Quarter Average Score     float64
Used in Quality Measure Five Star Rating     object
Measure Period                               object
Location                                     object
Processing Date                              object

'''
df_2020 = dfs[1].loc[:,
        [
            "Federal Provider Number",
            "Measure Description",
            "Resident type",
            "Q1 Measure Score",
            "Q2 Measure Score",
            "Q3 Measure Score",
            "Q4 Measure Score",
            "Four Quarter Average Score",
    ]]
df_2020.loc[:,"year"]="2020"

print(df_2020)



#2021
'''
Federal Provider Number                      object
Provider Name                                object
Provider Address                             object
Provider City                                object
Provider State                               object
Provider Zip Code                             int64
Measure Code                                  int64
Measure Description                          object
Resident type                                object
Q1 Measure Score                            float64
Footnote for Q1 Measure Score               float64
Q2 Measure Score                            float64
Footnote for Q2 Measure Score               float64
Q3 Measure Score                            float64
Footnote for Q3 Measure Score               float64
Q4 Measure Score                            float64
Footnote for Q4 Measure Score               float64
Four Quarter Average Score                  float64
Footnote for Four Quarter Average Score     float64
Used in Quality Measure Five Star Rating     object
Measure Period                               object
Location                                     object
Processing Date                              object

'''
df_2021 = dfs[2].loc[:,
        [
            "Federal Provider Number",
            "Measure Description",
            "Resident type",
            "Q1 Measure Score",
            "Q2 Measure Score",
            "Q3 Measure Score",
            "Q4 Measure Score",
            "Four Quarter Average Score",
    ]]
df_2021.loc[:,"year"]="2021"

print(df_2021)




#2022
'''
Federal Provider Number                      object
Provider Name                                object
Provider Address                             object
Provider City                                object
Provider State                               object
Provider Zip Code                             int64
Measure Code                                  int64
Measure Description                          object
Resident type                                object
Q1 Measure Score                            float64
Footnote for Q1 Measure Score               float64
Q2 Measure Score                            float64
Footnote for Q2 Measure Score               float64
Q3 Measure Score                            float64
Footnote for Q3 Measure Score               float64
Q4 Measure Score                            float64
Footnote for Q4 Measure Score               float64
Four Quarter Average Score                  float64
Footnote for Four Quarter Average Score     float64
Used in Quality Measure Five Star Rating     object
Measure Period                               object
Location                                     object
Processing Date                              object

'''
df_2022 = dfs[3].loc[:,
        [
            "Federal Provider Number",
            "Measure Description",
            "Resident type",
            "Q1 Measure Score",
            "Q2 Measure Score",
            "Q3 Measure Score",
            "Q4 Measure Score",
            "Four Quarter Average Score",
    ]]
df_2022.loc[:,"year"]="2022"

print(df_2022)






#2023
'''
CMS Certification Number (CCN)               object
Provider Name                                object
Provider Address                             object
City/Town                                    object
State                                        object
ZIP Code                                      int64
Measure Code                                  int64
Measure Description                          object
Resident type                                object
Q1 Measure Score                            float64
Footnote for Q1 Measure Score               float64
Q2 Measure Score                            float64
Footnote for Q2 Measure Score               float64
Q3 Measure Score                            float64
Footnote for Q3 Measure Score               float64
Q4 Measure Score                            float64
Footnote for Q4 Measure Score               float64
Four Quarter Average Score                  float64
Footnote for Four Quarter Average Score     float64
Used in Quality Measure Five Star Rating     object
Measure Period                               object
Location                                     object
Processing Date                              object

'''
df_2023 = dfs[4].loc[:,
        [
            "CMS Certification Number (CCN)",
            "Measure Description",
            "Resident type",
            "Q1 Measure Score",
            "Q2 Measure Score",
            "Q3 Measure Score",
            "Q4 Measure Score",
            "Four Quarter Average Score",
    ]]
df_2023.loc[:,"year"]="2023"

print(df_2023)








#2024
'''
CMS Certification Number (CCN)               object
Provider Name                                object
Provider Address                             object
City/Town                                    object
State                                        object
ZIP Code                                      int64
Measure Code                                  int64
Measure Description                          object
Resident type                                object
Q1 Measure Score                            float64
Footnote for Q1 Measure Score               float64
Q2 Measure Score                            float64
Footnote for Q2 Measure Score               float64
Q3 Measure Score                            float64
Footnote for Q3 Measure Score               float64
Q4 Measure Score                            float64
Footnote for Q4 Measure Score               float64
Four Quarter Average Score                  float64
Footnote for Four Quarter Average Score     float64
Used in Quality Measure Five Star Rating     object
Measure Period                               object
Location                                     object
Processing Date                              object

'''
df_2024 = dfs[5].loc[:,
        [
            "CMS Certification Number (CCN)",
            "Measure Description",
            "Resident type",
            "Q1 Measure Score",
            "Q2 Measure Score",
            "Q3 Measure Score",
            "Q4 Measure Score",
            "Four Quarter Average Score",
    ]]
df_2024.loc[:,"year"]="2024"

print(df_2024)


# Use first column name for all datasets
df_2020.columns = df_2019.columns
df_2021.columns = df_2019.columns
df_2022.columns = df_2019.columns
df_2023.columns = df_2019.columns
df_2024.columns = df_2019.columns


# 5 year dataset
output_data = pd.concat([df_2019,df_2020,df_2021,df_2022,df_2023,df_2024])




# save pickle
output_data.to_pickle("../00_Data/cms/data_subset.pickle")








