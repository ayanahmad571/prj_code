import csv
from twi_bot.feature_extraction import master_data_twi
# from cresci.feature_extraction import master_data_cresci

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
'hashtags_per_post'             ,
'urls_per_post'                 ,
'mentions_per_post'             ,
'words_per_post'                ,
'IS_BOT']

# data = master_data_twi + master_data_cresci
data = master_data_twi


with open('2_no_cresci.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)