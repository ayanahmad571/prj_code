import json
import pandas as pd

import numpy as np

# from this import d
# from labels_fetch import sql_insert

p = "../../../datasets/"

# (Path, Bot?)
paths = [
    "Twibot-20/train.json",
    "Twibot-20/dev.json",
    "Twibot-20/test.json"
]

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
    "midterm-2018(1)/midterm-2018_processed_user_objects.json"
]


print("Null Checking Other Datasets:")
diff_format_filename = "midterm-2018(1)/midterm-2018_processed_user_objects.json"
# Opening JSON files
for path in paths:
    print(path)
    with open(p+path) as file:
        f = open(p+path)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        nulls_in_path = []
        total_row = len(data)
        for row in data:
            if diff_format_filename == path:
                user_obj = row
            else:
                user_obj = row['user']
            
            def getDataRow(col):
                return user_obj[col]

            def isNull(col):
                val_to_check = user_obj[col]
                nulls = ["nan", np.nan, "NULL", ' ', " "]
                if val_to_check in nulls:
                    return int(1)
                else:
                    return int(0)

            col_names = ['statuses_count',
                        'followers_count',
                        'friends_count',
                        'favourites_count',
                        'listed_count',
                        'default_profile',
                        'profile_use_background_image',
                        'verified',
                        'screen_name',
                        'name',
                        'description']

            
            
            colNan = []
            for colV in col_names:
                colNan.append(isNull(colV))
            
            nan_val = (np.sum(colNan))
            
            if nan_val > 0:
                nulls_in_path.append(nan_val)

        
        print("Null Score", np.sum(nulls_in_path)/total_row)
        print()


print("Done")
