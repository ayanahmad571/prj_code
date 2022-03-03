from cmath import nan
import csv
from numpy import NaN, empty
import pandas as pd
from datetime import datetime
from email import header

from pip import List
import numpy as np

# from this import d
# from labels_fetch import sql_insert

p = "../../../datasets/cresci-2017.csv/datasets_full.csv/"

# (Path, Bot?)
paths = [
    ("genuine_accounts.csv", 0),
    ("social_spambots_3.csv", 1),
    ("traditional_spambots_3.csv", 1),
    ("social_spambots_1.csv", 1),
    ("traditional_spambots_1.csv", 1),
    ("traditional_spambots_4.csv", 1),
    ("fake_followers.csv", 1),
    ("social_spambots_2.csv", 1),
    ("traditional_spambots_2.csv", 1)
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
for path in paths:
    print(path[0])
    csv_path = p+path[0]+"/users.csv"
    df = pd.read_csv(csv_path)

    df["description"] = df['description'].astype(str)
    df["name"] = df['name'].astype(str)
    df["screen_name"] = df['screen_name'].astype(str)

    nulls_in_path = []
    total_row = len(df.index)
    for row_ind in df.index:
        def getDataRow(col):
            return df[col][row_ind]

        def isNull(col):
            val_to_check = df[col][row_ind]
            # nulls = ["nan", nan, 0, "NULL"]
            if val_to_check != val_to_check:
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
        nulls_in_path.append(nan_val)
    
    print("Null Score", np.sum(nulls_in_path)/total_row)
    print()


print("Done")
# print(master_data_cresci)
