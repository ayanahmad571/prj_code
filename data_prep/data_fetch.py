import json
from datetime import datetime

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
    "gilani-2017/gilani-2017_tweets.json", 
    "midterm-2018(1)/midterm-2018_tweets.json"
]

# Opening JSON file
f = open(p+paths[0])

# returns JSON object as
# a dictionary
data = json.load(f)
master_data = []
for row in data:
    UID = 1
    NUM_LIKES_PER_NUM_FRIENDS = 1
    FOLLOW_FRIENDS_RATIO = 1
    MAX_TIME_BW_TWEETS = 1
    RE_PER_TWEET = 1
    NUM_LIKES = 1
    NUM_LIKES_PER_FOLLOWER = 1
    AGE_ACCOUNT = 1
    NUM_TWEETS = 1
    LOCATION = 1
    LEN_USERNAME = 1
    HAS_PHOTO = 1
    LIKES_PER_DAY = 1
    
    #uid
    UID = row['user']['id']

    #acount age
    dtime_raw = row['created_at']
    created_at = datetime.strptime(dtime_raw,'%a %b %d %H:%M:%S +0000 %Y')
    diff = datetime.now() - created_at
    duration_in_s = diff.total_seconds() 
    AGE_ACCOUNT = divmod(duration_in_s, 86400)[0]


    
    to_append = (
        UID, 
        NUM_LIKES_PER_NUM_FRIENDS, 
        FOLLOW_FRIENDS_RATIO, 
        MAX_TIME_BW_TWEETS, 
        RE_PER_TWEET, 
        NUM_LIKES, 
        NUM_LIKES_PER_FOLLOWER, 
        AGE_ACCOUNT, 
        NUM_TWEETS, 
        LOCATION, 
        LEN_USERNAME, 
        HAS_PHOTO, 
        LIKES_PER_DAY
    )
    print(to_append)
    master_data.append(to_append)



 
# Closing file
f.close()