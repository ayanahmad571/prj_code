import csv
import pandas as pd
from datetime import datetime
from write_csv import write_to_file,write_to_file2
# from this import d
# from labels_fetch import sql_insert

p = "../../../../presedential_tweet_data/"

# (Path, Bot?)
paths = [
    "2020-09.csv",
    "2020-10.csv",
    "2020-11.csv",
    "2020-12.csv",
    "2021-01.csv",
    "2021-02.csv",
    "2021-03.csv"
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

print("Acessing PRESIDENTIAL Data:")
# Opening JSON files

for path in paths:
    all_presidential_tweets = []
    partial_presidential_data = []
    print(path)
    csv_path = p+path
    df = pd.read_csv(csv_path)

    df["user_description"] = df['user_description'].astype(str)
    df["user_name"] = df['user_name'].astype(str)
    df["user_screen_name"] = df['user_screen_name'].astype(str)
    

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

        #account age
        dtime_raw = getDataRow('user_created_at')
        created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S +0000 %Y')
        diff = datetime.now() - created_at
        duration_in_s = diff.total_seconds() 
        AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]




        #User Meta Data - Counts
        statuses_count                = getDataRow('user_statuses_count')
        followers_count               = getDataRow('user_followers_count')
        friends_count                 = getDataRow('user_friends_count')
        favourite_count               = getDataRow('user_favourites_count')
        listed_count                  = getDataRow('user_listed_count')

        #User Meta Data - Binary Values
        if getDataRow('user_default_profile_image'):
            default_profile_binary = 1

        # if getDataRow('profile_use_background_image'):
        #     profile_use_background_image = 1
        
        if getDataRow('user_verified'):
            verified = 1

        

        #Derived features

        tweet_freq                    = int(getDataRow('user_statuses_count'))/AGE_ACCOUNT
        followers_growth_rate         = int(getDataRow('user_followers_count'))/AGE_ACCOUNT
        friends_growth_rate           = int(getDataRow('user_friends_count'))/AGE_ACCOUNT
        favourites_growth_rate        = int(getDataRow('user_favourites_count'))/AGE_ACCOUNT
        listed_growth_rate            = int(getDataRow('user_listed_count'))/AGE_ACCOUNT

        followers_friends_ratio = 0
        if int(getDataRow('user_friends_count')) > 0:
            followers_friends_ratio       = int(getDataRow('user_followers_count'))/int(getDataRow('user_friends_count'))
        

        #description
        DESC_WORDS = 0
        desc = getDataRow('user_description')
        
        if len(desc) > 1:
            word_list = desc.split()
            DESC_WORDS = len(word_list)

        #screen_name
        LEN_SCREEN_NAME = 0
        scr_name = getDataRow('user_screen_name')
        SCREEN_NAME_DIGS = sum(c.isdigit() for c in scr_name)
        if len(scr_name) > 1:
            word_list = scr_name.split()
            LEN_SCREEN_NAME = len(word_list)

        #name
        LEN_NAME = 0
        name = getDataRow('user_name')
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

        u_tweet = getDataRow("text")
        t_hashtags = u_tweet.count("#")

        t_urls_http = u_tweet.count("http://")
        t_urls_https = u_tweet.count("https://")
        t_urls = t_urls_http + t_urls_https
        
        t_mentions = u_tweet.count("@")
        t_words = len(u_tweet.split())
            

        hashtags_per_post             = t_hashtags
        urls_per_post                 = t_urls
        mentions_per_post             = t_mentions
        words_per_post                = t_words


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
            words_per_post               
        ]

        to_append_partial = [
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
            description_length            
        ]
        # print(to_append)
        all_presidential_tweets.append(to_append)    
        partial_presidential_data.append(to_append_partial)

    write_to_file(path, all_presidential_tweets)
    write_to_file2(path, all_presidential_tweets)

    print("Done")
# print(all_presidential_tweets)

