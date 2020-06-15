# Data Engineering Capstone Project
**Project Summary**
The goal of this project is to create an ETL pipeline for creating a database from four different datsets. Ultimately, we'll use the database to analyze immigration related scenarios.

The project follows the follow steps:

### Step 1: Scope the Project and Gather Data
- pull data from four different sources as below to create fact and dimension tables. 

### Step 2: Explore and Assess the Data
**Explore the Data**
The goal of this section is to identify data quality issues, like missing values, duplicate data, etc.


|                     | Step1:<br>    Gather Data                                                                                     | Step2: <br> Cleaning Data                                                                                                                                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Immigration Data    | [the US National Tourism and Trade Offic](https://travel.trade.gov/research/reports/i94/historical/2016.html) | <li>  get country_name, visatype, port(city/state) information from `I94_SAS_Labels_Descriptions.SAS`  <li>  remove nulls based on i94addr and i94res col   <li>  convert the i94yr to date type   <li>  select only needed columns |
| US Demographic Data | [OpenSoft](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).                   |  <li>  retrieve the columns needed    <li>  calculate the percentage of foreign born person out of total population   <li>  convert the male and female population in percentage                                                    |
| US Airport Data     | [DataHub.io](https://datahub.io/core/airport-codes#data)                                                      | <li>  filter data ` iata_code isnull` AND `iso_country = 'US' `      <li>  count the number of flights in each states       <li>  get the country and state information                                                                 |
| US temperature Data | [Kaggle](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)                  | <li>  filter data without in only US and drop the records without temperature information      <li>  get the average monthly temperature by states data      <li>  add a column of abbreviation state                               |
### Step 3: Define the Data Model
- #### 3.1 Conceptual Data Model
 
Here we choose **Star Schema** for this database since we have clear fact and dimension table here.     
An ultimate goal is to do analaysis based on immigration data to answer the follow possible questions, for example:   
- 1:  Is there a higher possibility for people to land the state which has more foreign people? (higher pct_foregn percentage than other states) 
- 2:  Does people prefer to go to states with higher temperature in winter and lower temperature in summer? (for vocation) 

**Fact Table**     
    
 - US_immigration_table 
 >  civid  
 year, 
 month,  
 origin_country,   
 i94port,   
 city_port_name,   
 state_code,   
 dest_state_name   
 
        
    
**Dimension Tables**   

 - airport_table   
 > State,    country,   number_of_flights 

- demographic_table   
> State Code,
pct_male, 
pct_female, 
pct_foreign, 
Total Population

- temperature_table   
> State Code, 
month, 
AverageTemperature 

- i94_table
 
 >  civid   year, month,   origin_country,    i94port,    city_port_name,    state_code,    dest_state_name   
- #### 3.2 Mapping Out Data Pipelines
List the steps necessary to pipeline the data into the chosen data model
- Dimension tables will be created from processed dataset (3 from pandas dataframe + 1 pyspark dataframe).
- Fact table will be created by joining the dimensions tables. 
- Fact table is written as final parquet file.
### Step 4: Run ETL to Model the Data
- #### 4.1 Create DataModel
- Build the data pipelines to create the data model.
- #### 4.2 Data Quality Checks
Explain the data quality checks you'll perform to ensure the pipeline ran as expected. These could include:
 * Integrity constraints on the relational database (e.g., unique key, data type, etc.)
 * Unit tests for the scripts to ensure they are doing the right thing
 * Source/Count checks to ensure completeness
- #### 4.3 Data Dictionaries
Create a data dictionary for your data model. For each field, provide a brief description of what the data is and where it came from. You can include the data dictionary in the notebook or in a separate file.
**Dimension Tables** 

airport  
```
-  State  (StringType) - two digit Sate code 
-  country (StringType) - country name 
-  number_of_flights (LongType) - Aggregated by IATA_code to get number of flights in that Stats
```
temperature
```
- Code (StringType)  -two digit Sate code 
- month (LongType)   - Month presents in number 
- AverageTemperature (DoubleType) - the average historical temperature of that given month, in Celsius 
```

demographic
```
- pct_male (DoubleType)  - male percentage of that states 
- pct_foreign (DoubleType)   - foreign bron people percentage of that states 
- pct_female (DoubleType) - female percentage of that states 
- State_Code (StringType) - two digit Sate code   
- Total_Population (LongType) - Number of people in that state 
```

i94
```
- cicid (DoubleType)  - ID number of each individual
- year (IntegerType)   - year of immigration
- month (IntegerType) - month of immigration
- i94port (StringType) - City Port Code where Immigrant entered
- city_port_name (StringType) - City Port Code name 
- state_code (StringType) - two digit Sate code
- dest_state_name (StringType) - Detstination State name 
```

**Fact Table**
immigration_stats  
- year (IntegerType)   - year of immigration
- immig_month (IntegerType) - month of immigration
- to_immig_state (StringType) - Detstination State name 
- to_immig_state_count (IntegerType) -Total count of people immigrated per state from immigration table 
- AverageTemperature (DoubleType) - the average historical temperature of that given month, in Celsius 
- pct_foreign (DoubleType)   - foreign bron people percentage of that states 
-  number_of_flights (LongType) - Aggregated by IATA_code to get number of flights in that Stats
### Step 5: Complete Project Write Up

