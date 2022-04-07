import pandas as pd
import numpy as np

# Root Directory
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




print("Acessing Cresci User Data:")


for path in paths:
    print(path[0])
    csv_path = p+path[0]+"/users.csv"

    df = pd.read_csv(csv_path)

    # Change the Data Types
    df["description"] = df['description'].astype(str)
    df["name"] = df['name'].astype(str)
    df["screen_name"] = df['screen_name'].astype(str)

    # Holds the null values in a dataset
    nulls_in_path = []
    total_row = len(df.index)
    for row_ind in df.index:
        def getDataRow(col):
            return df[col][row_ind]

        def isNull(col):
            val_to_check = df[col][row_ind]
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
