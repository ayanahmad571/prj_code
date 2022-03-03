
import pandas as pd
import numpy as np
from model2 import model

# from this import d
# from labels_fetch import sql_insert

path = "../data_prep/presidential_data/extract/2020-09.csv"
# path = "test_data.csv"

df_president = pd.read_csv(path)
y_pres = model.predict(df_president)

y_pres = np.asarray(y_pres)
(unique, counts) = np.unique(y_pres, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)