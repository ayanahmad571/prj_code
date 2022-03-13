import pandas as pd
from sklearn.model_selection import train_test_split
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
from imblearn.over_sampling import SMOTE

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
  return (y.sum()/len(y))

def debug_print(X,y):
  print(len(X), len(y), get_bot_percentage(y))

df = pd.read_csv("/content/drive/MyDrive/PRJ/learning_data/labelled_data.csv")

X_raw_data = df[['statuses_count'                ,
'followers_count'               ,
'friends_count'                 ,
'favourite_count'               ,
'listed_count'                  ,
'default_profile_binary'        ,
'profile_use_background_image'  ,
'verified'                      ,
'tweet_freq'                    ,
'followers_growth_rate'         ,
'friends_growth_rate'           ,
'favourites_growth_rate'        ,
'listed_growth_rate'            ,
'followers_friends_ratio'       ,
'screen_name_length'            , 
'num_digits_in_screen_name'     ,
'name_length'                   ,
'num_digits_in_name'            ,
'description_length'            ]]
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


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=1400, min_samples_split= 5, min_samples_leaf=1, max_features= 'sqrt', max_depth= 80, bootstrap= False)
model.fit(X_train, y_train)

#Test Data
y_predicted = model.predict(X_test)
print("Accuracy Test:",metrics.accuracy_score(y_test, y_predicted))

#Val Data
y_predicted_val = model.predict(X_val)
print("Accuracy Val:",metrics.accuracy_score(y_val, y_predicted_val))

#Train Data
y_predicted_train = model.predict(X_train)
print("Accuracy Train:",metrics.accuracy_score(y_train, y_predicted_train))

# print(confusion_matrix(y_test,y_predicted))
# print(classification_report(y_test,y_predicted))

from sklearn.model_selection import RandomizedSearchCV# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]

# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)


# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestClassifier()
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)# Fit the random search model
rf_random.fit(X_train, y_train)
print(rf_random.best_params_)

list_names = ["partial_2020-09", "partial_2020-10", "partial_2020-11", "partial_2020-12", "partial_2021-01", "partial_2021-02", "partial_2021-03"]
bot_vals = []
for y in list_names:
  path = f"/content/drive/MyDrive/PRJ/presi_data/{y}.csv"

  df_pres = pd.read_csv(path)
  y_pres = model.predict(df_pres)
  y_pres = np.asarray(y_pres)
  (unique, counts) = np.unique(y_pres, return_counts=True)
  frequencies = np.asarray((unique, counts)).T
  bot_vals.append(frequencies)
  print(frequencies)
  
result_split = get_split(bot_vals)
print("Bot Percentage:", ((result_split[1]*100)/(result_split[0] + result_split[1])))