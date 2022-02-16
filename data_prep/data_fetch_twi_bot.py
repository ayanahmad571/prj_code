import json
from datetime import datetime
# from this import d
# from labels_fetch import sql_insert

p = "../../datasets/"

paths = [
    "Twibot-20/train.json",
    "Twibot-20/dev.json",
    "Twibot-20/test.json"
]

# #### New Features - user metadata
# - statuses_count                count
# - followers_count               count
# - friends_count                 count
# - favourite_count               count
# - listed_count                  count
# - default_profile_binary        binary
# - profile_use_background_image  binary
# - verified                      binary

# #### New Features - derived features

# - tweet_freq                    real-valued
# - followers_growth_rate         real-valued
# - friends_growth_rate           real-valued
# - favourites_growth_rate        real-valued
# - listed_growth_rate            real-valued
# - followers_friends_ratio       real-valued
# - screen_name_length            count 
# - num_digits_in_screen_name     count
# - name_length                   count
# - num_digits_in_name            count
# - description_length            count
# - screen_name_likelihood        real-valued


print("Acessing TwiBot User Data:")
# Opening JSON files
for path in paths:
    print(path)
    with open(p+path) as file:
        f = open(p+path)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        master_data_twi = []
        for row in data:
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

            
            user_obj = row['profile']

            #account age
            dtime_raw = user_obj['created_at']
            created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S +0000 %Y ')
            diff = datetime.now() - created_at
            duration_in_s = diff.total_seconds() 
            AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]




            #User Meta Data - Counts
            statuses_count                = user_obj['statuses_count']
            followers_count               = user_obj['followers_count']
            friends_count                 = user_obj['friends_count']
            favourite_count               = user_obj['favourites_count']
            listed_count                  = user_obj['listed_count']

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
            if len(desc) > 1:
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
            IS_BOT = row['label']
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
            master_data_twi.append(to_append)
                



        
        # Closing file
        f.close()
    print("Done")