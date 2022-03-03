import pandas as pd
import csv
# from this import d
# from labels_fetch import sql_insert

p = "../../../datasets/cresci-2017.csv/datasets_full.csv/"

paths = [
    ("genuine_accounts.csv",0),
    ("social_spambots_3.csv",1),
    ("social_spambots_1.csv",1),
    # ("traditional_spambots_1.csv",1), # Too Many Null Values
    ("fake_followers.csv",1),
    ("social_spambots_2.csv",1)
]

# #### Tweet Features
# - Num Hashtags per post        real-valued
# - Num URLs per post            real-valued
# - Num Mentions per post        real-valued
# - Num of Words per post        real-valued






# def getDataRow(col):
#     return df[col][row_ind]

print("Acessing Cresci Tweet Data:")
# Opening JSON files
tweet_data_user = {}
for path in paths:
    print(path[0])
    csv_path = p+path[0]+"/tweets.csv"
    line = 1
    with open(csv_path, 'r',  encoding="utf8", errors="ignore") as file:
        reader = csv.reader(x.replace('\0', '') for x in file)
        for row in reader:
            if line > 1 and len(row) > 4:    
                # text	            - 1
                # user_id	        - 3
                # num_hashtags	    - 18
                # num_urls	        - 19
                # num_mentions	    - 20
                if path[0] == "fake_followers.csv":
                    user_id = int(row[4])
                    tweet_text = row[2]
                    num_hashtags = int(row[19])
                    num_urls = int(row[20])
                    num_mentions = int(row[21])
                else:
                    user_id = int(row[3])
                    tweet_text = row[1]
                    num_hashtags = int(row[18])
                    num_urls = int(row[19])
                    num_mentions = int(row[20])

                # print(line, user_id, len(row))


                
                # array( text_len, hashtags, urls, mentions, tweet_count )
                if user_id in tweet_data_user:
                    current_data = tweet_data_user[user_id]
                    to_insert = [len(tweet_text.split()), num_hashtags, num_urls, num_mentions, 1] 
                    tweet_data_user[user_id] = [
                        current_data[0]+to_insert[0],
                        current_data[1]+to_insert[1],
                        current_data[2]+to_insert[2],
                        current_data[3]+to_insert[3],
                        current_data[4]+to_insert[4]]
                else:
                    tweet_data_user[user_id] = [len(tweet_text.split()), num_hashtags, num_urls, num_mentions, 1]
            line +=1
# print(tweet_data_user)
print("Done")

