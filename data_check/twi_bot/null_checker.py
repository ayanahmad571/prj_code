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


print("Acessing Cresci User Data:")
# Opening JSON files
master_data_cresci = []
ns = 0
n_is = 0
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
            user_obj = row['profile']
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
            # colVals = []
            for colV in col_names:
                colNan.append(isNull(colV))
                # colVals.append(getDataRow(colV))
            
            nan_val = (np.sum(colNan))
            
            if nan_val > 0:
                nulls_in_path.append(nan_val)

            # add vals to variable
            ns += int(row["label"])
            n_is +=1
        
        print("Null Score", np.sum(nulls_in_path)/total_row)
        print()


print("Done")
print(ns)
print(n_is)
# print(master_data_cresci)
