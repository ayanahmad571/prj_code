import json
import numpy as np


p = "../../../datasets/"

# (Path, Bot?)
paths = [
    "Twibot-20/train.json",
    "Twibot-20/dev.json",
    "Twibot-20/test.json"
]



print("Acessing Cresci User Data:")

for path in paths:
    print(path)
    with open(p+path) as file:
        f = open(p+path)

        # returns JSON object as a dictionary
        data = json.load(f)
    
        # Holds the null values in a dataset
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
            for colV in col_names:
                colNan.append(isNull(colV))            
            
            nan_val = (np.sum(colNan))
            
            if nan_val > 0:
                nulls_in_path.append(nan_val)

        
        print("Null Score", np.sum(nulls_in_path)/total_row)
        print()


print("Done")