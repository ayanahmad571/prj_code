import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report,confusion_matrix

from helper_functions import get_train_test_split,models_to_run
from sklearn.ensemble import RandomForestClassifier

for variant in models_to_run:
	print("###########################################")
	print("Running: ",variant[1])
	path_to_training_data = variant[3]
	model_type = variant[2]

	X_raw_data, y_raw_data, X_train, y_train, X_val, y_val, X_test, y_test, X_train_res, y_train_res = get_train_test_split(path_to_training_data,model_type)

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

	print(confusion_matrix(y_test,y_predicted))
	print(classification_report(y_test,y_predicted))
