import csv
from write_txt import write_txt
import numpy as np

files = [0,1,2,3,4]
result_holder = list()
for f in files:
    with open(f'../2_data_analysis/results_{f}.txt', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            result_holder.append(float(row[0]))
        
result_holder = np.asarray(result_holder)
mean = np.average(result_holder)
write_txt("combined.txt", str(mean))