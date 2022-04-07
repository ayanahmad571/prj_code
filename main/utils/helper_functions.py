import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

models_to_run = [
    (1,"Model-1 No-Mid-Cresci", 1, "./utils/training_data/m1/1_no_mid_cresci.csv"),
    (2,"Model-1 All", 1, "./utils/training_data/m1/1_all.csv"),
    (3,"Model-2 No-Mid-Cresci", 2, "./utils/training_data/m2/2_no_cresci.csv"),
    (4,"Model-2 All", 2, "./utils/training_data/m2/2_all.csv")
]

# Essential Function
def get_split(holder):
  humans = 0
  bots = 0
  for row in holder:
    humans += row[0][1]
    bots += row[1][1]
  return [humans, bots]

def get_bot_percentage(y):
  y = np.asarray(y)
  return ((y[1]*100)/(y[0] + y[1]))

def debug_print(X,y):
    pass
#   print(len(X), len(y), get_bot_percentage(y))

def get_train_test_split(path, m):
    df = pd.read_csv(path)

    essential_cols = ['statuses_count' ,'followers_count', 'friends_count', 'favourite_count', 'listed_count', 'default_profile_binary', 'profile_use_background_image',
    'verified', 'tweet_freq', 'followers_growth_rate', 'friends_growth_rate', 'favourites_growth_rate', 'listed_growth_rate', 'followers_friends_ratio', 'screen_name_length', 'num_digits_in_screen_name','name_length', 'num_digits_in_name', 'description_length']
    extra_cols = ['hashtags_per_post', 'urls_per_post', 'mentions_per_post', 'words_per_post']

    feature_set = essential_cols + extra_cols if (m==2) else essential_cols

    X_raw_data = df[feature_set]
    y_raw_data = df.IS_BOT

    X_train, X_test, y_train, y_test = train_test_split(X_raw_data, y_raw_data,train_size=0.7)
    X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, train_size=0.6)

    sm = SMOTE(random_state=2)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train.ravel())

    debug_print(X_raw_data, y_raw_data)
    debug_print(X_train, y_train)
    debug_print(X_val, y_val)
    debug_print(X_test, y_test)
    debug_print(X_train_res, y_train_res)
    
    return X_raw_data, y_raw_data, X_train, y_train, X_val, y_val, X_test, y_test, X_train_res, y_train_res