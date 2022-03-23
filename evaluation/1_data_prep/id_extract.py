import pandas as pd
import random
from write_txt import write_txt

p = "../../../presedential_tweet_data/"

# (Path, Bot?)
paths = [
    "2020-09.csv",
    "2020-10.csv",
    "2020-11.csv",
    "2020-12.csv",
    "2021-01.csv",
    "2021-02.csv",
    "2021-03.csv"
]

rand_user_ids = list()
print("Acessing PRESIDENTIAL Data for BotOMeter Evaluation:")
# Opening JSON files
prob_threshold = 10
for path in paths:
    print(path)
    csv_path = p+path
    df = pd.read_csv(csv_path)
    
    for row_ind in df.index:
        checker = random.randrange(0, 1000, 2)
        if checker <= prob_threshold:
            rand_user_ids.append(df["user_id"][row_ind])


# print(rand_user_ids)
id_holder = []
num_buckets = int(len(rand_user_ids)/2000) + 1 #size of botometer
for _ in range(num_buckets):
    id_holder.append(list())

counter = 1
for uid in rand_user_ids:
    bucket_id = int(counter/2000)
    id_holder[bucket_id].append(uid)
    counter +=1

for b in range(num_buckets):
    print(len(id_holder[b]))
    write_txt(f'uid_{b}.txt', id_holder[b])