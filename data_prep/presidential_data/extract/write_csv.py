import csv

def write_to_file(file_name, data):
    print(f"Writing {file_name} to file")
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
    'words_per_post'                ]


    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

def write_to_file2(file_name, data):
    print(f"Writing {file_name} to file - Partial")
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
    'description_length'            ]


    with open("partial_"+file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)