import json
import numpy as np

from helper_functions import get_train_test_split,models_to_run
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV# Number of trees in random forest


for variant in models_to_run:
    print("###########################################")
    print("Optimizing: ",variant[1])
    path_to_training_data = variant[3]
    model_type = variant[2]

    X_raw_data, y_raw_data, X_train, y_train, X_val, y_val, X_test, y_test, X_train_res, y_train_res = get_train_test_split(path_to_training_data,model_type)

    # Number of trees in random forest
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

    # Use the random grid to search for best hyperparameters
    # First create the base model to tune
    rf = RandomForestClassifier()
    # Random search of parameters, using 3 fold cross validation, 
    # search across 100 different combinations, and use all available cores
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)# Fit the random search model
    rf_random.fit(X_train, y_train)

    jsonString = json.dumps(rf_random.best_params_)
    jsonFile = open(f"{variant[0]}.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    print(rf_random.best_params_)
