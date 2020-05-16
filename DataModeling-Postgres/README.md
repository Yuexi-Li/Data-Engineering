
# Data Modeling with Postgres & ETL Pipeline

### Introduction 
Sparkify is an starup and the analytics team is particularly interested in understanding what songs users are listening to on their new music streaming app. Currently, their data resides in a directory of **JSON logs** on user activity on the app, as well as a directory with JSON metadata on the songs in their app. However, this cannot provid an easy way to query the data.

This project aims to create Postgres database with tables designed to optimize queries on song play analysis as a data engineer. The task is to create a star schema for Postgres and develop an ETL pipleine which will transfer the data from local files to the database.

### Requirements and Framework 
- Python 3  *(pandas| numpy| psycopg2 | glob) 
- Postgre SQL Database 
-  Jupyter Notebook

### Workspace Structure 
The structure below shows how the files in first project of DEND organized. 
``` 
data-modeling-postgre 
|      README.md    # Project Description 
|
└----- data         # Data Source in JSON  (Not provided)
|	   |     
|    └----- song_data   
|	   |            |...   
|    └----- log_data   
|	   |...   
|   
└------scr          # Source Code 
|		     |   
|       └------ sql_queries.py        # Drop/Create/Insert sql queries 
|       └------ create_tables.py      # Schema create sript
|       └------ elt.py                # ETL script
|       └------ etl.ipynb             # Data check and reference for elt.py
|       └------ test.ipynb            # Test Postgre queries 
```
 
### Database Schema 
![Star Schema](https://github.com/Yuexi-Li/Data-Engineering/blob/master/DataModeling-Postgres/star_schema.jpg)

