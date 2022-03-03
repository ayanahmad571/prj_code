import pandas as pd
from datetime import datetime
from types import NoneType
# from this import d
from cresci.tweets_features_extractor import tweet_data_user

p = "../../../datasets/cresci-2017.csv/datasets_full.csv/"

paths = [
    ("genuine_accounts.csv",0),
    ("social_spambots_3.csv",1),
    ("social_spambots_1.csv",1),
    # ("traditional_spambots_1.csv",1), # Too Many Null Values
    ("fake_followers.csv",1),
    ("social_spambots_2.csv",1)
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

# #### Tweet Features
# - Num Hashtags per post        real-valued
# - Num URLs per post            real-valued
# - Num Mentions per post        real-valued
# - Num of Words per post        real-valued



# text	
# user_id	
# num_hashtags	
# num_urls	
# num_mentions	


print("Acessing Cresci User Data:")
# Opening JSON files
master_data_cresci = []
for path in paths:
    print(path[0])
    csv_path = p+path[0]+"/users.csv"
    df = pd.read_csv(csv_path)

    df["description"] = df['description'].astype(str)
    df["name"] = df['name'].astype(str)
    df["screen_name"] = df['screen_name'].astype(str)
    

    for row_ind in df.index:
        def getDataRow(col):
            return df[col][row_ind]

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

        #### Tweet Features
        hashtags_per_post             = 0 
        urls_per_post                 = 0
        mentions_per_post             = 0
        words_per_post                = 0

        if(path[0] == "traditional_spambots_1.csv"):
            #account age
            dtime_str = getDataRow('created_at')
            dtime_raw = int(dtime_str.replace("L", ""))/1000 # Ms to S
            created_at = datetime.fromtimestamp(dtime_raw)
            diff = datetime.now() - created_at
            duration_in_s = diff.total_seconds() 
            AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]
        
        else:
            #account age
            dtime_raw = getDataRow('created_at')
            created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S +0000 %Y')
            diff = datetime.now() - created_at
            duration_in_s = diff.total_seconds() 
            AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]




        #User Meta Data - Counts
        statuses_count                = getDataRow('statuses_count')
        followers_count               = getDataRow('followers_count')
        friends_count                 = getDataRow('friends_count')
        favourite_count               = getDataRow('favourites_count')
        listed_count                  = getDataRow('listed_count')

        #User Meta Data - Binary Values
        if getDataRow('default_profile'):
            default_profile_binary = 1

        if getDataRow('profile_use_background_image'):
            profile_use_background_image = 1
        
        if getDataRow('verified'):
            verified = 1

        

        #Derived features

        tweet_freq                    = int(getDataRow('statuses_count'))/AGE_ACCOUNT
        followers_growth_rate         = int(getDataRow('followers_count'))/AGE_ACCOUNT
        friends_growth_rate           = int(getDataRow('friends_count'))/AGE_ACCOUNT
        favourites_growth_rate        = int(getDataRow('favourites_count'))/AGE_ACCOUNT
        listed_growth_rate            = int(getDataRow('listed_count'))/AGE_ACCOUNT

        followers_friends_ratio = 0
        if int(getDataRow('friends_count')) > 0:
            followers_friends_ratio       = int(getDataRow('followers_count'))/int(getDataRow('friends_count'))
        

        #description
        DESC_WORDS = 0
        desc = getDataRow('description')
        
        if len(desc) > 1:
            word_list = desc.split()
            DESC_WORDS = len(word_list)

        #screen_name
        LEN_SCREEN_NAME = 0
        scr_name = getDataRow('screen_name')
        SCREEN_NAME_DIGS = sum(c.isdigit() for c in scr_name)
        if len(scr_name) > 1:
            word_list = scr_name.split()
            LEN_SCREEN_NAME = len(word_list)

        #name
        LEN_NAME = 0
        name = getDataRow('name')
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
        
        UID = int(getDataRow("id"))
        #IS A BOT?
        if UID in tweet_data_user:
            tdr = tweet_data_user[UID]
            #### Tweet Features
            # array( text_len, hashtags, urls, mentions, tweet_count )
            words_per_post                = tdr[0]/tdr[4]
            hashtags_per_post             = tdr[1]/tdr[4]
            urls_per_post                 = tdr[2]/tdr[4]
            mentions_per_post             = tdr[3]/tdr[4]

            IS_BOT = path[1]
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
                hashtags_per_post             ,
                urls_per_post                 ,
                mentions_per_post             ,
                words_per_post                ,
                IS_BOT
            ]
            # print(to_append)
            master_data_cresci.append(to_append)    

    print("Done")
# print(master_data_cresci)

