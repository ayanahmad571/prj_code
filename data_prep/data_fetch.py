import json
from datetime import datetime
# from this import d
from labels_fetch import sql_insert

p = "../../datasets/"

paths = [
    "botometer-feedback-2019/botometer-feedback-2019_tweets.json",
    "pronbots-2019/pronbots-2019_tweets.json", 
    "verified-2019/verified-2019_tweets.json", 
    "vendor-purchased-2019/vendor-purchased-2019_tweets.json", 
    "political-bots-2019/political-bots-2019_tweets.json", 
    "celebrity-2019(1)/celebrity-2019_tweets.json", 
    "botwiki-2019/botwiki-2019_tweets.json", 
    "cresci-rtbust-2019(1)/cresci-rtbust-2019_tweets.json", 
    "gilani-2017/gilani-2017_tweets.json"
]


print("Acessing User Data:")
# Opening JSON files
for path in paths:
    print(path)
    with open(p+path) as file:
        f = open(p+path)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        master_data = []
        for row in data:
            UID = 1
            HAS_BACK_IMAGE = 0
            IS_VERIFIED = 0
            HAS_PHOTO = 0
            FOLLOW_COUNT = 0
            LIST_COUNT = 0
            DESC_WORDS = 0
            FRIENDS = 0
            HAS_LOCATION = 0
            IS_GEO = 0
            LEN_SCREEN_NAME = 0
            FAVORITES = 0
            AGE_ACCOUNT = 1 
            
            
            user_obj = row['user']

            #uid
            UID = user_obj['id']
            
            #back image?
            if user_obj['profile_background_image_url_https'] != None:
                HAS_BACK_IMAGE = 1
            
            #verified
            if user_obj['verified']:
                IS_VERIFIED = 1

            #profile photo ?
            if user_obj['profile_image_url_https'] != None:
                HAS_PHOTO = 1

            #followers_count
            FOLLOW_COUNT = user_obj['followers_count']

            #listed_count
            LIST_COUNT = user_obj['listed_count']

            #description
            desc = user_obj['description']
            if len(desc) > 1:
                word_list = user_obj['description'].split()
                DESC_WORDS = len(word_list)
                
            #friends_count
            FRIENDS = user_obj['friends_count']

            #location?
            if len(user_obj['location']) > 1:
                HAS_LOCATION = 1

            #geo_enabled
            if user_obj['geo_enabled']:
                IS_GEO = 1

            #screen_name
            scr_name = user_obj['description']
            if len(scr_name) > 1:
                word_list = scr_name.split()
                LEN_SCREEN_NAME = len(word_list)

            #favourites_count
            FAVORITES = user_obj['favourites_count']


            #acount age
            dtime_raw = row['user']['created_at']
            created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S +0000 %Y')
            diff = datetime.now() - created_at
            duration_in_s = diff.total_seconds() 
            AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]

            #IS A BOT?
            if UID in sql_insert:
                IS_BOT = sql_insert[UID]
                to_append = [
                    # UID, 
                    HAS_BACK_IMAGE, 
                    IS_VERIFIED, 
                    HAS_PHOTO,
                    FOLLOW_COUNT,
                    LIST_COUNT, 
                    DESC_WORDS, 
                    FRIENDS, 
                    AGE_ACCOUNT, 
                    HAS_LOCATION, 
                    IS_GEO, 
                    LEN_SCREEN_NAME, 
                    FAVORITES, 
                    IS_BOT
                ]
                # print(to_append)
                master_data.append(to_append)



        
        # Closing file
        f.close()
    print("Done")