import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix

df = pd.read_csv("../data_prep/model_1_users/labelled_data.csv")

X_train, X_test, y_train, y_test = train_test_split(df[['statuses_count'                ,
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
'description_length'            ]],
df.IS_BOT,
train_size=0.7)

X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, train_size=0.6)
print(len(X_train), len(y_train))
print(len(X_val), len(y_val))
print(len(X_test), len(y_test))

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
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