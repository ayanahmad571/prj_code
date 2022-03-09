
import pandas as pd
import numpy as np


# Model 1
from model1 import model
path = "../data_prep/presidential_data/extract/partial_2020-09.csv"

# Model 2
# from model2 import model
# path = "../data_prep/presidential_data/extract/2020-09.csv"



df_president = pd.read_csv(path)
y_pres = model.predict(df_president)

y_pres = np.asarray(y_pres)
(unique, counts) = np.unique(y_pres, return_counts=True)
frequencies = np.asarray((unique, counts)).T
print(frequencies)