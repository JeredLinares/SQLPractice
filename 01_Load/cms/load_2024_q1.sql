USE nh_mds;

LOAD DATA INFILE '/data/nh_mds/Facility_Level_MDS_Frequency_Q1_2024.csv' 
INTO TABLE 2024_q1 
FIELDS terminated by ',' 
enclosed by '"' 
lines terminated by '\n' 
ignore 1 rows;
