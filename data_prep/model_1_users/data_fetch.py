import json
from datetime import datetime
# from this import d
from labels_fetch import sql_insert

p = "../../../datasets/"

paths = [
    "botometer-feedback-2019/botometer-feedback-2019_tweets.json",
    "pronbots-2019/pronbots-2019_tweets.json", 
    "verified-2019/verified-2019_tweets.json", 
    "vendor-purchased-2019/vendor-purchased-2019_tweets.json", 
    "political-bots-2019/political-bots-2019_tweets.json", 
    "celebrity-2019(1)/celebrity-2019_tweets.json", 
    "botwiki-2019/botwiki-2019_tweets.json", 
    "cresci-rtbust-2019(1)/cresci-rtbust-2019_tweets.json", 
    "gilani-2017/gilani-2017_tweets.json",
    # "midterm-2018(1)/midterm-2018_processed_user_objects.json"
]



print("Acessing User Data:")
diff_format_filename = "midterm-2018(1)/midterm-2018_processed_user_objects.json"
# Opening JSON files
master_data = []
for path in paths:
    print(path)
    with open(p+path) as file:
        f = open(p+path)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        for row in data:
            if diff_format_filename == path:
                UID = row['user_id']
            else:
                UID = row['user']['id']
            
            #### New Features - user metadata
            statuses_count                = 0
            followers_count               = 0
            friends_count                 = 0
            favourite_count               = 0
            listed_count                  = 0
            default_profile_binary        = 0
            profile_use_background_image  = 0
            verified                      = 0

            #### New Features - derived features

            tweet_freq                    = 0
            followers_growth_rate         = 0
            friends_growth_rate           = 0
            favourites_growth_rate        = 0
            listed_growth_rate            = 0
            followers_friends_ratio       = 0
            screen_name_length            = 0 
            num_digits_in_screen_name     = 0
            name_length                   = 0
            num_digits_in_name            = 0
            description_length            = 0
            # screen_name_likelihood        = 0

            if diff_format_filename == path:
                user_obj = row
            else:
                user_obj = row['user']
            
            
        
            #account age
            if diff_format_filename == path:
                dtime_raw = user_obj['user_created_at']
                created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S %Y')
            else:
                dtime_raw = user_obj['created_at']
                created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S +0000 %Y')
            
            
            diff = datetime.now() - created_at
            duration_in_s = diff.total_seconds() 
            AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]




            #User Meta Data - Counts
            statuses_count                = int(user_obj['statuses_count'])
            followers_count               = int(user_obj['followers_count'])
            friends_count                 = int(user_obj['friends_count'])
            favourite_count               = int(user_obj['favourites_count'])
            listed_count                  = int(user_obj['listed_count'])

            #User Meta Data - Binary Values
            if user_obj['default_profile']:
                default_profile_binary = 1

            if user_obj['profile_use_background_image']:
                profile_use_background_image = 1
            
            if user_obj['verified']:
                verified = 1

            

            #Derived features

            tweet_freq                    = int(user_obj['statuses_count'])/AGE_ACCOUNT
            followers_growth_rate         = int(user_obj['followers_count'])/AGE_ACCOUNT
            friends_growth_rate           = int(user_obj['friends_count'])/AGE_ACCOUNT
            favourites_growth_rate        = int(user_obj['favourites_count'])/AGE_ACCOUNT
            listed_growth_rate            = int(user_obj['listed_count'])/AGE_ACCOUNT

            followers_friends_ratio = 0
            if int(user_obj['friends_count']) > 0:
                followers_friends_ratio       = int(user_obj['followers_count'])/int(user_obj['friends_count'])
            

            #description
            DESC_WORDS = 0
            desc = user_obj['description']
            if desc and len(desc) > 1 :
                word_list = user_obj['description'].split()
                DESC_WORDS = len(word_list)

            #screen_name
            LEN_SCREEN_NAME = 0
            scr_name = user_obj['screen_name']
            SCREEN_NAME_DIGS = sum(c.isdigit() for c in scr_name)
            if len(scr_name) > 1:
                word_list = scr_name.split()
                LEN_SCREEN_NAME = len(word_list)

            #name
            LEN_NAME = 0
            name = user_obj['name']
            NAME_DIGS = sum(c.isdigit() for c in name)
            if len(name) > 1:
                word_list = name.split()
                LEN_NAME = len(word_list)
            

            screen_name_length            = LEN_SCREEN_NAME 
            num_digits_in_screen_name     = SCREEN_NAME_DIGS
            name_length                   = LEN_NAME
            num_digits_in_name            = NAME_DIGS
            description_length            = DESC_WORDS
            # screen_name_likelihood        = 

            #IS A BOT?
            if UID in sql_insert:
                IS_BOT = sql_insert[UID]
                to_append = [
                    statuses_count                ,
                    followers_count               ,
                    friends_count                 ,
                    favourite_count               ,
                    listed_count                  ,
                    default_profile_binary        ,
                    profile_use_background_image  ,
                    verified                      ,
                    tweet_freq                    ,
                    followers_growth_rate         ,
                    friends_growth_rate           ,
                    favourites_growth_rate        ,
                    listed_growth_rate            ,
                    followers_friends_ratio       ,
                    screen_name_length            , 
                    num_digits_in_screen_name     ,
                    name_length                   ,
                    num_digits_in_name            ,
                    description_length            ,
                    IS_BOT
                ]
                # print(to_append)
                master_data.append(to_append)
                    



        
        # Closing file
        f.close()
    print("Done")