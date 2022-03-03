import os.path
from random import randint, random

url = "https://raw.githubusercontent.com/echen102/"

months_2020 = ["2020-08","2020-09","2020-10","2020-11","2020-12", "2021-01","2021-02","2021-03","2021-04"]
intervals = {1,3}
    

for m in months_2020:
    filenames = list()
    print(m,"_________")
    for d in range(31):
        new_d = d + 1
        for t in intervals:
            padded_d = new_d
            if len(str(new_d)) < 2:
                padded_d = f"0{new_d}"
            file_name = f'D:/KINGS CS/YEAR 3/PRJ/presidential_tweet_ids/us-presidential-tweet-id-{m}-{padded_d}-0{t}.txt'
            filenames.append(file_name)

    with open(f'D:/KINGS CS/YEAR 3/PRJ/presedential_tweet_data/{m}.txt', 'w') as outfile:
        for fname in filenames:
            lets_do_it = (randint(1,10)==5)
            if os.path.exists(fname) and lets_do_it:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)