import numpy as np
import pandas as pd
from train_test_split import get_split,get_bot_percentage,models_to_run
from k_build_optimised_model import models_trained

for variant in models_to_run:
    print("")
    print("==================================================")
    print("Detecting Bots: ",variant[1])


    model = models_trained[variant[0]]

    list_names_partial = ["partial_2020-09", "partial_2020-10", "partial_2020-11", "partial_2020-12", "partial_2021-01", "partial_2021-02", "partial_2021-03"
    ]
    list_names_full = ["2020-09", "2020-10", "2020-11", "2020-12", "2021-01", "2021-02", "2021-03"
    ]

    list_names = list_names_full if (variant[2] == 2) else list_names_partial
    bot_vals = []
    for y in list_names:
        print(" Scanning: ",y)
        path = f"../data_prep/presidential_data/extract/{y}.csv"

        df_pres = pd.read_csv(path)
        y_pres = model.predict(df_pres)
        y_pres = np.asarray(y_pres)
        (unique, counts) = np.unique(y_pres, return_counts=True)
        frequencies = np.asarray((unique, counts)).T
        bot_vals.append(frequencies)

    print(bot_vals)
    result_split = get_split(bot_vals)
    print("Bot Percentage:", get_bot_percentage(result_split))