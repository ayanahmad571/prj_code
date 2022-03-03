
import pandas as pd
import csv
from model2 import model
# from this import d
# from labels_fetch import sql_insert

path = "../data_prep/presidential_data/extract/presidential_data.csv"
# path = "test_data.csv"

df = pd.read_csv(path)
y_predicted = model.predict(df)

print(y_predicted)

