LOAD DATA INFILE '/data/nh_mds/Facility_Level_MDS_Frequency_Q4_2023.csv' 
INTO TABLE 2023_q4 
FIELDS terminated by ',' 
enclosed by '"' 
lines terminated by '\n' 
ignore 1 rows
