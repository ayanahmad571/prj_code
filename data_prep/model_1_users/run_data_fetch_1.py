import csv
from doctest import master
from data_fetch import master_data
from data_fetch_twi_bot import master_data_twi
from data_fetch_cresci import master_data_cresci


header = [
'statuses_count'                ,
'followers_count'               ,
'friends_count'                 ,
'favourite_count'               ,
'listed_count'                  ,
'default_profile_binary'        ,
'profile_use_background_image'  ,
'verified'                      ,
'tweet_freq'                    ,
'followers_growth_rate'         ,
'friends_growth_rate'           ,
'favourites_growth_rate'        ,
'listed_growth_rate'            ,
'followers_friends_ratio'       ,
'screen_name_length'            , 
'num_digits_in_screen_name'     ,
'name_length'                   ,
'num_digits_in_name'            ,
'description_length'            ,
'IS_BOT']

data = master_data + master_data_twi + master_data_cresci
# data = master_data + master_data_twi 
# data = master_data_twi

# the datasets to make
with open('labelled_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)