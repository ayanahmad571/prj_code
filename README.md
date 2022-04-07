
# Detecting Suspicious Accounts in Online Social Networks (Politics) - Code ReadMe
  

### Pre-Requisites

The following libraries must be installed on the system with the respective minimum versions.

 - botometer>=1.6.1 
 - imbalanced_learn>=0.9.0 
 - imblearn>=0.0 
 - numpy>=1.22.3
 - pandas>=1.4.2 
 - pip>=22.0.4 
 - requests>=2.27.1 
 - scikit_learn>=1.0.2
 - tweepy>=4.8.0 
 - urllib3>=1.26.9

  
 
### Folder Structure
At the root of the folder, there will be 4 sub-directories.

 1. data_check
 2. data_prep
 3. evaluation
 4. main

Out of the four, only **main** can be run without the datasets stored in a parent folder.

### How to run?
After all the required libraries are installed, follow the steps below:

 - Run Terminal/CMD
 - cd into the root folder of this project
 - cd into main
 - type ```py main.py```

The script may take a few hours to run but displays output as it processes data.

### Directory Contents
This section outlines the contents of each directory 
#### 1. data_check
There are three subfolders within the data_check directory:

 - cresci
 - others
 - twi_bot

Each subfolder contains python scripts to traverse through respective datasets and produce null scores.
	
#### 2. data_prep
 - model_1_users
 - model_2_user_tweets
	 - twi_bot
	 - cresci
 - presidential_data
	 - extract
	 - fetch

**model_1_users** contains files to extract and produce a two csv files. Namely:

 1. 1_all.csv
 2. 1_no_mid_cresci

These csv files are feature sets with only User Data, with the difference being the number of datasets produced.

**model_2_user_tweets** contains files to extract and produce a two csv files. Namely:

 1. 2_all.csv
 2. 2_no_cresci

These csv files are feature sets with User Data and Tweet Data, with the difference being the number of datasets produced.


**presidential_data** contains two sub-directories. Directory Fetch connects to Github and downloads the required raw files. Directory extract reads each downloaded file and combines them into monthly csv files containing row-column like data (described in the research paper). 

#### 3. evaluation
 - 1_data_prep
 - 2_data_analysis
 - 3_data_combine

Each of these directories performs tasks related to botometer. **1_data_prep** extracts random 10000 rows of data from the complete presidential dataset, splits them into files of 2000 rows and saves them. **2_data_analysis** connects to the botometer API to fetch the bot percentage results from each file. **3_data_combine** combines the results from botomter and takes an average over the complete result set. 

#### 4. main

 - utils
	 - training_data

This folder contains essential scripts used to run our models. Utils contains all the essential helper scripts and training_data contains all the labelled feature sets. The file main.py is stored at the root of this folder.
## Further Reading
This project is further elaborated in the research paper submitted to Kings College London by Ayan Ahmad.

