import csv
from doctest import master
from data_fetch import master_data


header = ['HAS_BACK_IMAGE', 
'IS_VERIFIED', 
'HAS_PHOTO',
'FOLLOW_COUNT',
'LIST_COUNT', 
'DESC_WORDS', 
'FRIENDS', 
'AGE_ACCOUNT', 
'HAS_LOCATION', 
'IS_GEO', 
'LEN_SCREEN_NAME', 
'FAVORITES', 
'IS_BOT']

data = master_data

with open('data_saved.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)